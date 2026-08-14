# AWS Assignment – S3 Integration with CSVStat

## Overview

This assignment extends the previous **CSVStat** project by integrating it with AWS.

In the previous assignment, the CSV file was processed locally.

In this assignment, the workflow was changed so that:

* The input CSV file is stored in **Amazon S3**.
* The application accepts the **S3 path** of the CSV file.
* The application downloads and processes the specified file from S3.
* The generated output is uploaded back to **Amazon S3**.
* An **IAM Role** is used to provide the EC2 instance with access to S3.
* The application runs on an **EC2 instance**, which is accessed using SSH.

The existing CSVStat processing functions were reused from the previous assignment.

---

# AWS Architecture

```text
                    Amazon S3
                       │
                       │
                input/test.csv
                       │
                       ↓
                Amazon EC2
                       │
                 csvstat.py
                       │
              Download CSV
                       │
                       ↓
              Process CSV
                       │
              Generate Output
                       │
                       ↓
                Upload Output
                       │
                       ↓
                    Amazon S3
                       │
                output/*.txt
```

---

# 🛠️ AWS Services Used

## Amazon S3

Amazon S3 is used to store:

* Input CSV files
* Generated output files

Bucket used:

```text
jatin-aws-practice-2026-001
```

Bucket structure:

```text
jatin-aws-practice-2026-001/
│
├── input/
│   └── test.csv
│
└── output/
    └── test_<timestamp>.txt
```
<img width="845" height="98" alt="image" src="https://github.com/user-attachments/assets/2eaddff1-4ade-4a2e-93d9-0faafe69ffa5" />

---

## Amazon EC2

An EC2 instance is used as the compute environment.

The Python application runs on the EC2 instance and performs the CSV processing.

---

## IAM Role

An IAM Role is attached to the EC2 instance to allow the application to access S3 securely.

The role provides the required S3 permissions without storing AWS access keys directly inside the Python code.




---

# Connecting to EC2 Using SSH

The EC2 instance was accessed using SSH.

Command:

```bash
ssh -i <key-file>.pem ec2-user@<EC2-PUBLIC-IP>
```

Example:

```bash
ssh -i aws-key.pem ec2-user@<EC2-PUBLIC-IP>
```

After connecting, the Python application and required files were accessed from the EC2 environment.

---

# Python Environment Setup

Python was verified on the EC2 instance:

```bash
python3 --version
```

A virtual environment was created:

```bash
python3 -m venv venv
```

The virtual environment was activated:

```bash
source venv/bin/activate
```

Boto3 was installed:

```bash
pip install boto3
```

---

# Storing Input in S3

The input CSV file was uploaded to the S3 bucket under the `input/` folder.

Example:

```text
s3://jatin-aws-practice-2026-001/input/test.csv
```

The file can be uploaded using AWS CLI:

```bash
aws s3 cp test.csv s3://jatin-aws-practice-2026-001/input/
```

The uploaded file can be verified using:

```bash
aws s3 ls s3://jatin-aws-practice-2026-001/input/
```

---

# Changes Made in `csvstat.py`

The previous CSVStat application accepted a local CSV file.

The application was modified to accept an **S3 path** as input.

### Command

```bash
python3 csvstat.py s3://jatin-aws-practice-2026-001/input/test.csv
```

The S3 path is received using `argparse`:

```python
parser.add_argument("csv_path")
```

The path is then stored:

```python
s3_path = args.csv_path
```

---

## Parsing the S3 Path

The application verifies that the input is an S3 path:

```python
if not s3_path.startswith("s3://"):
    print("Error: Input path must be an S3 path.")
    return
```

The `s3://` prefix is removed:

```python
s3_location = s3_path.replace("s3://", "", 1)
```

The bucket name and object key are extracted:

```python
bucket, s3_key = s3_location.split("/", 1)
```

For example:

```text
s3://jatin-aws-practice-2026-001/input/test.csv
```

becomes:

```text
Bucket:
jatin-aws-practice-2026-001

Key:
input/test.csv
```

This allows the program to process the **exact S3 file provided by the user** instead of scanning or hardcoding the input folder.

---

# Downloading the S3 File

A Boto3 S3 client is created:

```python
s3 = boto3.client("s3")
```

The specified file is downloaded from S3:

```python
s3.download_file(
    bucket,
    s3_key,
    local_path
)
```

The file is temporarily stored on EC2:

```text
/tmp/test.csv
```

The existing CSVStat functions can then process this local file.

The important change is that the user does **not** need to manually download the CSV before running the program.

The application handles the S3 download itself.

---

# Running the Application

The application is executed by providing the S3 path:

```bash
python3 csvstat.py s3://jatin-aws-practice-2026-001/input/test.csv
```

The `--top` argument can also be used:

```bash
python3 csvstat.py s3://jatin-aws-practice-2026-001/input/test.csv --top 2
```

If `--top` is not provided, the default value is `5`.


---
<img width="1231" height="191" alt="image" src="https://github.com/user-attachments/assets/9bdd3101-4f2e-4815-ae8f-72570e680f93" />

# Storing Output in S3

After processing the CSV, the application generates the output content.

A timestamp is added to the output filename:

```python
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
```

Example:

```text
test_20260814_080937.txt
```

The output S3 key is generated as:

```text
output/test_20260814_080937.txt
```

The output is uploaded using Boto3:

```python
s3.put_object(
    Bucket=bucket,
    Key=output_key,
    Body=output_content.encode("utf-8")
)
```

The final output is stored at:

```text
s3://jatin-aws-practice-2026-001/output/test_20260814_080937.txt
```

---

# Temporary File Cleanup

After processing and uploading the output, the temporary file downloaded to EC2 is removed:

```python
os.remove(local_path)
```

Therefore, the CSV does not remain unnecessarily on the EC2 instance.

---

# Verifying the Output

The output files can be checked using:

```bash
aws s3 ls s3://jatin-aws-practice-2026-001/output/
```

Example:

```text
2026-08-14 08:09:37    test_20260814_080937.txt
```

---

# Complete Workflow

```text
1. Create S3 bucket
        ↓
2. Upload test.csv to S3/input/
        ↓
3. Launch EC2 instance
        ↓
4. Attach IAM Role with S3 permissions
        ↓
5. Connect to EC2 using SSH
        ↓
6. Set up Python environment
        ↓
7. Install Boto3
        ↓
8. Run csvstat.py with S3 path
        ↓
9. Parse bucket and S3 object key
        ↓
10. Download specified CSV from S3
        ↓
11. Process CSV using existing CSVStat functions
        ↓
12. Generate timestamped output
        ↓
13. Upload output to S3/output/
        ↓
14. Delete temporary local CSV
```

---

# Important Commands

### Connect to EC2

```bash
ssh -i <key-file>.pem ec2-user@<EC2-PUBLIC-IP>
```

### Check Python

```bash
python3 --version
```

### Create virtual environment

```bash
python3 -m venv venv
```

### Activate virtual environment

```bash
source venv/bin/activate
```

### Install Boto3

```bash
pip install boto3
```

### Upload input CSV to S3

```bash
aws s3 cp test.csv s3://jatin-aws-practice-2026-001/input/
```

### Verify input

```bash
aws s3 ls s3://jatin-aws-practice-2026-001/input/
```

### Run CSVStat using S3 input

```bash
python3 csvstat.py s3://jatin-aws-practice-2026-001/input/test.csv
```

### Run with `--top`

```bash
python3 csvstat.py s3://jatin-aws-practice-2026-001/input/test.csv --top 2
```

### Verify output

```bash
aws s3 ls s3://jatin-aws-practice-2026-001/output/
```

---

# Final Result

The previous local CSV processing workflow was extended to a cloud-based workflow using AWS.

The final implementation allows the user to provide an S3 path directly:

```bash
python3 csvstat.py s3://jatin-aws-practice-2026-001/input/test.csv
```

The application then handles the complete flow:

```text
S3 Input
   ↓
EC2
   ↓
Python + Boto3
   ↓
CSV Processing
   ↓
Output Generation
   ↓
S3 Output
```

The EC2 instance accesses S3 using an **IAM Role**, avoiding hardcoded AWS credentials in the application.
