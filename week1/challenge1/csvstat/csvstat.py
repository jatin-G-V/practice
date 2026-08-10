import argparse
from datetime import datetime

parser = argparse.ArgumentParser()

# Return the number of rows in the CSV file
def rows(path):
    with open(path, 'r') as file:
        count = 0
        for line in file:
            count += 1
    return count

# Return the number of columns in the CSV file
def columns(path):
    with open(path, 'r') as file:
        first_line = file.readline()
        return len(first_line.split(','))

# Return the column names and their types in the CSV file
def table_info(path):
    with open(path, 'r') as file:
        first_line = file.readline()
        column_names = first_line.strip().split(',')
        types = {}
        i = 0
        for value in file.readline().strip().split(','):
            name = column_names[i];
            types[name] = value_type(value)
            i += 1
        return types

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

# Return the  type of particular column in the CSV file
def column_type(path,column_name):
    with open(path, 'r') as file:
        first_line = file.readline()
        column_names = first_line.strip().split(',')
        if column_name not in column_names:
            return f"Error: Column '{column_name}' not found in the CSV file."
        index = column_names.index(column_name)
        value = file.readline().strip().split(',')[index]
        return value_type(value)

# Return the minimum value of a particular column in the CSV file
def column_min(path,column_name):
    with open(path, 'r') as file:
        first_line = file.readline()
        column_names = first_line.strip().split(',')
        if column_name not in column_names:
            return f"Error: Column '{column_name}' not found in the CSV file."
        index = column_names.index(column_name)
        min_value = None
        for line in file:
            if line.strip().split(',')[index] == '':
                continue
            value = float(line.strip().split(',')[index])

            if min_value is None or value < min_value:
                min_value = value
        return min_value

# Return the maximum value of a particular column in the CSV file
def column_max(path,column_name):
    with open(path, 'r') as file:
        first_line = file.readline()
        column_names = first_line.strip().split(',')
        if column_name not in column_names:
            return f"Error: Column '{column_name}' not found in the CSV file."
        index = column_names.index(column_name)
        max_value = None
        for line in file:
            if line.strip().split(',')[index] == '':
                continue
            value = float(line.strip().split(',')[index])
            if max_value is None or value > max_value:
                max_value = value
        return max_value

# Return the mean value of a particular column in the CSV file
def column_mean(path,column_name):
    with open(path, 'r') as file:
        first_line = file.readline()
        column_names = first_line.strip().split(',')
        if column_name not in column_names:
            return f"Error: Column '{column_name}' not found in the CSV file."
        index = column_names.index(column_name)
        total = 0
        count = 0
        for line in file:
            value = line.strip().split(',')[index]
            try:
                total += float(value)
                count += 1
            except ValueError:
                continue
        if count == 0:
            return "No valid numbers found."
        return total / count

# Return the mean of all numeric columns in the CSV file    
def numeric_columns_mean(path):
    with open(path, 'r') as file:
        first_line = file.readline()
        column_names = first_line.strip().split(',')
        numeric_columns = []
        s = file.readline().strip().split(',')
        for value in s:
            if value_type(value) in ["int", "float"]:
                numeric_columns.append(column_names[s.index(value)])
        means = {}
        for column in numeric_columns:
            means[column] = column_mean(path, column)
        return means

# Return the minimum of all numeric columns in the CSV file
def numeric_columns_min(path):
    with open(path, 'r') as file:
        first_line = file.readline()
        column_names = first_line.strip().split(',')
        numeric_columns = []
        s = file.readline().strip().split(',')
        for value in s:
            if value_type(value) in ["int", "float"]:
                numeric_columns.append(column_names[s.index(value)])
        mins = {}
        for column in numeric_columns:
            mins[column] = column_min(path, column)
        return mins        

# Return the maximum of all numeric columns in the CSV file
def numeric_columns_max(path):
    with open(path, 'r') as file:
        first_line = file.readline()
        column_names = first_line.strip().split(',')
        numeric_columns = []
        s = file.readline().strip().split(',')
        for value in s:
            if value_type(value) in ["int", "float"]:
                numeric_columns.append(column_names[s.index(value)])
        maxes = {}
        for column in numeric_columns:
            maxes[column] = column_max(path, column)
        return maxes  
      
# Return the most frequent values of a particular column in the CSV file
def most_frequent_values(path, column_name, limit):
    with open(path, 'r') as file:
        if limit is None:
            return "Error: Please provide a value for the --top argument."
        if limit <= 0:
            return "Error: Please provide a positive integer for the --top argument."
        first_line = file.readline()
        column_names = first_line.strip().split(',')
        if column_name not in column_names:
            return f"Error: Column '{column_name}' not found in the CSV file."
        index = column_names.index(column_name)
        frequency = {}
        for line in file:
            value = line.strip().split(',')[index]
            if value == '':
                continue
            if value in frequency:
                frequency[value] += 1
            else:
                frequency[value] = 1
        sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
        return sorted_frequency[0:limit:1]

# Return the most frequent values of all columns in the CSV file
def frequent_values_all_columns(path, limit):
    with open(path, 'r') as file:
        if limit is None:
            return "Error: Please provide a value for the --top argument."
        if limit <= 0:
            return "Error: Please provide a positive integer for the --top argument."
        first_line = file.readline()
        column_names = first_line.strip().split(',')
        frequency_all_columns = {}
        for column_name in column_names:
            if column_type(path, column_name) in ["int", "float", "date"]:
                continue
            frequency_all_columns[column_name] = most_frequent_values(path, column_name, limit)
        return frequency_all_columns

    
# Return the count and percentage of missing values for each column in the CSV file
def missing_values(path):
    with open(path, "r") as file:
        first_line = file.readline()
        column_names = first_line.strip().split(",")

        missing = {}

        # Initialize all columns
        for column in column_names:
            missing[column] = 0

        total_rows = 0

        for line in file:
            total_rows += 1
            values = line.strip().split(",")

            i = 0

            for value in values:
                if value.strip() == "":
                    missing[column_names[i]] += 1
                i += 1

        result = {}

        for column in column_names:
            count = missing[column]

            if total_rows == 0:
                percentage = 0
            else:
                percentage = (count / total_rows) * 100

            result[column] = {
                "count": count,
                "percentage": percentage
            }

        return result

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("csv_path")
    parser.add_argument("--top", type=int)

    args = parser.parse_args()

    path = args.csv_path
    limit = args.top

    if limit is None:
        limit = 5

    try:
        with open(path, "r") as file:
            if not path.endswith(".csv"):
                print("Error: The file is not a CSV file.")
                exit(1)
            
            print("Number of rows:", rows(path) ,'\n')
            print("Number of columns:", columns(path),'\n')
            print("Table info:", table_info(path),'\n')
            print("Numeric columns mean:", numeric_columns_mean(path),'\n')
            print("Numeric columns min:", numeric_columns_min(path),'\n')
            print("Numeric columns max:", numeric_columns_max(path),'\n')
            print("Most frequent values of all columns:", frequent_values_all_columns(path, limit),'\n')
            print("Missing values:", missing_values(path),'\n')

    except FileNotFoundError:
        print(f"Error: The file '{path}' was not found.")
        exit(1)
      
if __name__ == "__main__":
    main()