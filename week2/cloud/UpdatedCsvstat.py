import argparse
import os
import boto3
from datetime import datetime

parser = argparse.ArgumentParser()

# Return the number of rows in the CSV file
def number_Of_Rows(path):
    with open(path, 'r') as file:
        count = 0
        for line in file:
            count += 1
    return count

# Return the number of columns in the CSV file
def number_Of_Columns(path):
    with open(path, 'r') as file:
        first_line = file.readline()
        return len(first_line.split(','))


# Return the type of a value as a string    
def value_type(value):
    try:
        int(value)
        return "int"
    except ValueError:
        try:
            float(value)
            return "float"
        except ValueError:
            try:
                datetime.strptime(value, "%Y-%m-%d")
                return "date"
            except ValueError:
                return "str"
            
# Return the column_header names in the CSV file
def columns(path):
    with open(path, 'r') as file:
        first_line = file.readline()
        column_names = first_line.strip().split(',')
        return column_names
    

# Return the column data of a particular column in the CSV file
def column_values(path, column_name):
    column_names = columns(path)

    if column_name not in column_names:
        return f"Error: Column '{column_name}' not found in the CSV file."

    index = column_names.index(column_name)

    data = []

    with open(path, 'r') as file:
        file.readline()  

        for line in file:
            value = line.strip().split(',')[index]
            if value != "":
                data.append(value)

    return data

def numeric_column_values(path, column_name):
    values = column_values(path, column_name)

    if isinstance(values, str):
        return values

    numeric_values = []
    for value in values:
        try:
            numeric_values.append(float(value))
        except ValueError:
            continue

    return numeric_values

# Return the  type of particular column in the CSV file
def column_type(path,column_name):
    column_names = columns(path)
    if column_name not in column_names:
        return f"Error: Column '{column_name}' not found in the CSV file."
    index = column_names.index(column_name)
    with open(path, 'r') as file:
        file.readline()
        value = file.readline().strip().split(',')[index]
        return value_type(value)

# Return the column names and their types in the CSV file
def table_info(path):
    column_names = columns(path)
    types = {}
    for column in column_names:
        types[column] = column_type(path, column)   
    return types



# Return the statistics of a particular numeric column in the CSV file
def numeric_stats(path, column_name):
    values = numeric_column_values(path, column_name)

    if isinstance(values, str):
        return values

    if not values:
        return "No valid numbers found."

    return {
        "min": min(values),
        "max": max(values),
        "mean": sum(values) / len(values)
    }

# Return the  numeric statistics of all numeric columns in the CSV file
def numeric_columns_stats(path):
    column_names = columns(path)
    numeric_stats_dict = {}

    for column in column_names:
        if column_type(path, column) in ["int", "float"]:
            stats = numeric_stats(path, column)
            numeric_stats_dict[column] = stats

    return numeric_stats_dict
      
# Return the most frequent values of a particular column in the CSV file
def most_frequent_values(path, column_name, limit):
    values = column_values(path, column_name)

    if isinstance(values, str):
        return values

    frequency = {}

    for value in values:
        if value in frequency:
            frequency[value] += 1
        else:
            frequency[value] = 1

    sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

    return dict(sorted_frequency[:limit])

# Return the most frequent values of all columns in the CSV file
def frequent_values_all_columns(path, limit):
    column_names = columns(path)
    frequent_values_dict = {}

    for column in column_names:
        frequent_values = most_frequent_values(path, column, limit)
        frequent_values_dict[column] = frequent_values

    return frequent_values_dict


    
# Return the count and percentage of missing values for each column in the CSV file
def missing_values(path):
    column_names = columns(path)
    missing_values_dict = {}
    for column in column_names:
        missing_count = 0
        values = column_values(path, column)

        if isinstance(values, str):
            return values
             
        total_count = number_Of_Rows(path) - 1
        missing_count = total_count - len(values)
        if total_count > 0:
            missing_percentage = (missing_count / total_count) * 100
        else:
            missing_percentage = 0

        missing_values_dict[column] = {
            "missing_count": missing_count,
            "missing_percentage": missing_percentage
        }

    return missing_values_dict

def main():
    parser = argparse.ArgumentParser()

    # S3 path is required
    parser.add_argument("csv_path")

    # Optional top limit
    parser.add_argument("--top", type=int)

    args = parser.parse_args()

    s3_path = args.csv_path
    limit = args.top if args.top is not None else 5

    # Check that the input is an S3 path
    if not s3_path.startswith("s3://"):
        print("Error: Input path must be an S3 path.")
        return

    # Remove s3://
    s3_location = s3_path.replace("s3://", "", 1)

    # Split bucket and object key
    try:
        bucket, s3_key = s3_location.split("/", 1)
    except ValueError:
        print("Error: Invalid S3 path.")
        return

    # Check that the file is a CSV
    if not s3_key.endswith(".csv"):
        print("Error: The file is not a CSV file.")
        return

    s3 = boto3.client("s3")

    # Temporary local path
    file_name = os.path.basename(s3_key)
    local_path = f"/tmp/{file_name}"

    try:
        # Download the requested S3 file
        s3.download_file(
            bucket,
            s3_key,
            local_path
        )

        output = []

        output.append(f"CSV File: {file_name}")

        output.append(
            f"Number of rows: {number_Of_Rows(local_path)}"
        )

        output.append(
            f"Number of columns: {number_Of_Columns(local_path)}"
        )

        output.append(
            f"Table info: {table_info(local_path)}"
        )

        output.append(
            f"Numeric columns statistics: "
            f"{numeric_columns_stats(local_path)}"
        )

        output.append(
            f"Most frequent values of all columns: "
            f"{frequent_values_all_columns(local_path, limit)}"
        )

        output.append(
            f"Missing values: {missing_values(local_path)}"
        )

        output_content = "\n\n".join(output)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        output_key = (
            f"output/"
            f"{os.path.splitext(file_name)[0]}_"
            f"{timestamp}.txt"
        )

        # Upload result to the same S3 bucket
        s3.put_object(
            Bucket=bucket,
            Key=output_key,
            Body=output_content.encode("utf-8")
        )

        print(f"Processed: {s3_path}")
        print(
            f"Output saved to: "
            f"s3://{bucket}/{output_key}"
        )

    except Exception as error:
        print(f"Error: {error}")

    finally:
        # Remove temporary local file
        if os.path.exists(local_path):
            os.remove(local_path)
      
if __name__ == "__main__":
    main()