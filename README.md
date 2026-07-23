# FileGuard

## File Integrity Monitoring Tool

FileGuard is a lightweight cybersecurity tool developed in Python for monitoring the integrity of files and folders.

It uses **SHA-256 cryptographic hashing** to create a trusted baseline of files and later compares the current state of the folder against that baseline.

FileGuard can detect:

* Unchanged files
* Modified files
* Newly created files
* Deleted files

It also provides scan statistics, severity classification, user confirmation for baseline updates, and a visual HTML security report.

---

## Features

### SHA-256 File Hashing

FileGuard calculates a SHA-256 hash for every monitored file.

A hash acts as a digital fingerprint of the file. If the contents of a file change, its SHA-256 hash will normally also change.

### Recursive Folder Scanning

FileGuard can scan a folder and all of its subfolders.

Example:

```text
Main Folder/
├── file1.txt
├── image.jpg
│
├── Documents/
│   ├── report.pdf
│   └── notes.txt
│
└── Backup/
    └── config.json
```

### File Modification Detection

If the current hash of a file is different from its stored baseline hash, the file is classified as:

```text
MODIFIED
```

### New File Detection

If a file exists during the current scan but does not exist in the baseline, it is classified as:

```text
NEW
```

### Deleted File Detection

If a file exists in the baseline but is missing during the current scan, it is classified as:

```text
DELETED
```

### User Confirmation

FileGuard asks the user whether:

* A new file should be added to the baseline.
* A deleted file was intentionally deleted.

This prevents the tool from automatically trusting every change.

### Severity Classification

The tool calculates an overall security status based on the detected changes.

| Severity | Description                                                       |
| -------- | ----------------------------------------------------------------- |
| LOW      | No changes detected                                               |
| MEDIUM   | New or deleted files detected                                     |
| HIGH     | Existing files have been modified                                 |
| CRITICAL | Multiple significant changes, such as modifications and deletions |

### HTML Security Report

After a scan, FileGuard generates a visual HTML report containing:

* Scan time
* Scanned folder
* Total files checked
* Unchanged files
* Modified files
* New files
* Deleted files
* Security severity
* Detailed findings

The report can be opened in any modern web browser.

---

# How It Works

FileGuard follows this workflow:

```text
User selects folder
        ↓
Folder is scanned recursively
        ↓
SHA-256 hash is calculated for every file
        ↓
Hashes are compared with the baseline
        ↓
Changes are classified
        ↓
User confirmation is requested
        ↓
Severity is calculated
        ↓
HTML security report is generated
```

---

# Requirements

FileGuard requires:

* Python 3.8 or newer
* Git

The project primarily uses Python's standard library, so no external Python packages are required.

---

# Installation

## 1. Clone the Repository

Open your terminal or command prompt and run:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with the actual URL of your GitHub repository.

Example:

```bash
git clone https://github.com/your-username/fileguard.git
```

Move into the project directory:

```bash
cd fileguard
```

---

# Windows Installation

## Command Prompt

Open Command Prompt and run:

```cmd
git clone YOUR_GITHUB_REPOSITORY_URL
cd fileguard
```

Check whether Python is installed:

```cmd
python --version
```

Run the program:

```cmd
python main.py
```

## PowerShell

Open PowerShell and run:

```powershell
git clone YOUR_GITHUB_REPOSITORY_URL
cd fileguard
python main.py
```

---

# Linux Installation

Open the terminal and run:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd fileguard
```

Check the Python version:

```bash
python3 --version
```

Run the program:

```bash
python3 main.py
```

On some Linux systems, the following command may also work:

```bash
python main.py
```

---

# macOS Installation

Open Terminal and run:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd fileguard
```

Check the Python version:

```bash
python3 --version
```

Run the program:

```bash
python3 main.py
```

---

# Usage

After starting the program, FileGuard provides the available options.

Example:

```text
====================================
          FILEGUARD
  FILE INTEGRITY MONITORING TOOL
====================================

1. Create Baseline
2. Scan Folder

Enter your choice:
```

---

# Creating a Baseline

A baseline represents the trusted state of a folder.

Select the baseline creation option and provide the folder path.

Example on Windows:

```text
C:\Users\User\Documents\ImportantFiles
```

Example on Linux:

```text
/home/user/Documents/ImportantFiles
```

Example on macOS:

```text
/Users/user/Documents/ImportantFiles
```

FileGuard scans the folder and calculates a SHA-256 hash for every file.

The baseline is then stored.

Example:

```text
Baseline created successfully.

Files scanned: 25
```

---

# Scanning a Folder

After a baseline has been created, run the scan option.

FileGuard will:

1. Scan the selected folder.
2. Calculate current hashes.
3. Load the trusted baseline.
4. Compare current hashes with baseline hashes.
5. Detect changes.
6. Classify the results.
7. Generate the security report.

Example output:

```text
====================================
        FILEGUARD SCAN RESULTS
====================================

[UNCHANGED] report.pdf
[MODIFIED]  config.txt
[NEW]       suspicious.exe
[DELETED]   old_file.docx

====================================
           SCAN SUMMARY
====================================

Total files checked: 25
Unchanged files: 22
Modified files: 1
New files: 1
Deleted files: 1

Security Status: CRITICAL
```

---

# Testing the Tool

The recommended way to test FileGuard is to create a controlled test folder.

Example:

```text
test_folder/
├── file1.txt
├── file2.txt
└── image.jpg
```

## Test 1: Unchanged File

1. Create the baseline.
2. Do not change anything.
3. Run the scan.

Expected result:

```text
[UNCHANGED] file1.txt
[UNCHANGED] file2.txt
[UNCHANGED] image.jpg
```

---

## Test 2: Modified File

1. Create a baseline.
2. Open one file.
3. Change its contents.
4. Save the file.
5. Run FileGuard again.

Expected result:

```text
[MODIFIED] file1.txt
```

---

## Test 3: New File

1. Create a baseline.
2. Create a new file inside the monitored folder.
3. Run FileGuard.

Expected result:

```text
[NEW] new_file.txt
```

The tool will ask whether the new file should be added to the baseline.

---

## Test 4: Deleted File

1. Create a baseline.
2. Delete one of the files.
3. Run FileGuard.

Expected result:

```text
[DELETED] file2.txt
```

The tool will ask whether the deletion was intentional.

---

# Baseline File

The baseline stores the relative path and SHA-256 hash of each file.

Example:

```json
{
    "file1.txt": "sha256_hash_value",
    "Documents/report.pdf": "sha256_hash_value",
    "Images/photo.jpg": "sha256_hash_value"
}
```

The relative path is used instead of only the filename so that files with identical names in different folders can be distinguished.

For example:

```text
Folder1/report.pdf
Folder2/report.pdf
```

These are treated as two different files.

---

# Supported File Types

FileGuard is file-type independent.

It can calculate hashes for files such as:

* `.txt`
* `.pdf`
* `.jpg`
* `.png`
* `.gif`
* `.docx`
* `.xlsx`
* `.zip`
* `.exe`
* `.mp4`
* `.json`
* `.py`
* `.conf`

The tool does not need to understand the internal format of a file.

It reads the file's binary content and calculates its SHA-256 hash.

---

# Important Path Usage Note

The same folder path should be used when creating and scanning a baseline.

For example, if the baseline is created using:

```text
Documents/Test
```

the same path structure should be used during the scan.

Using a different path representation, such as:

```text
Test
```

may cause the tool to treat the folder differently because the current version relies on the path provided by the user.

This is a known limitation of the current version.

Future versions could improve this by storing the original absolute folder path in the baseline and automatically validating or normalizing paths.

---

# Project Structure

A typical project structure is:

```text
FileGuard/
├── main.py
├── baseline.json
├── report.html
├── README.md
└── LICENSE
```

The exact structure may vary depending on the implementation.

---

# Technologies Used

| Technology | Purpose                       |
| ---------- | ----------------------------- |
| Python     | Main programming language     |
| hashlib    | SHA-256 hash generation       |
| os         | File and directory operations |
| json       | Baseline storage              |
| datetime   | Scan timestamp                |
| HTML       | Report structure              |
| CSS        | Report styling                |
| Git        | Version control               |
| GitHub     | Source code hosting           |

---

# Security Concept

FileGuard is based on the concept of:

## File Integrity Monitoring

File Integrity Monitoring is a security process used to detect unauthorized or unexpected changes to files.

The general process is:

```text
Trusted File
     ↓
Hash Calculation
     ↓
Trusted Baseline
     ↓
Future Scan
     ↓
New Hash Calculation
     ↓
Comparison
     ↓
Change Detection
```

If the hash changes, the file content has changed.

---

# Limitations

## Baseline Path Consistency

FileGuard currently relies on the folder path provided by the user during scanning.

If a baseline is created using one path representation:

```text
Documents/Test
```

and the same folder is later scanned using a different path representation:

```text
Test
```

the tool may treat the files differently because their stored relative paths may not match.

Users should therefore use the same folder path structure when creating and scanning a baseline.

A future version could solve this problem by storing and validating the original absolute folder path and normalizing path representations.

---

## Baseline Protection

If an attacker can modify both the monitored files and the baseline, the integrity monitoring process could potentially be bypassed.

A future version could digitally sign the baseline or store it in a protected location.

---

## Manual Scanning

The current version requires the user to manually run the scan.

Future versions could support scheduled scans.

---

## No Real-Time Monitoring

FileGuard currently detects changes when a scan is performed.

It does not continuously monitor file changes in real time.

---

# Future Improvements

Possible future improvements include:

* Digital signatures for the baseline
* Secure baseline storage
* Real-time file monitoring
* Scheduled automatic scans
* Email notifications
* SIEM integration
* Web dashboard
* Multiple monitored folders
* Database storage
* User authentication
* Configurable file exclusions
* Centralized monitoring

---

# Project Documentation

The project includes a complete project report explaining:

* The objective
* Problem statement
* Features
* System workflow
* Implementation
* Detection logic
* Testing
* Challenges
* Limitations
* Future improvements

---

# Disclaimer

FileGuard is designed for legitimate cybersecurity and educational purposes.

Only monitor files and folders that you own or have explicit permission to monitor.

Do not use this tool to monitor systems, files, or data without proper authorization.

---

# License

This project is released under the MIT License.

You may use, modify, and distribute the software according to the terms of the license.

---

# Author

**Zeeshan Haider**

Cybersecurity Student
COMSATS University Islamabad

---

# Contributing

Contributions are welcome.

To contribute:

1. Fork the repository.
2. Create a new branch:

```bash
git checkout -b feature/new-feature
```

3. Make your changes.
4. Commit your changes:

```bash
git commit -m "Add new feature"
```

5. Push the branch:

```bash
git push origin feature/new-feature
```

6. Create a Pull Request.

---

# Reporting Issues

If you discover a bug or have a feature suggestion, create an issue in the GitHub repository.

When reporting a problem, include:

* Operating system
* Python version
* Steps to reproduce the issue
* Error message
* Expected behavior
* Actual behavior

---

# Quick Start

For Windows:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd fileguard
python main.py
```

For Linux and macOS:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd fileguard
python3 main.py
```

Then:

1. Create a baseline.
2. Modify, add, or delete files for testing.
3. Run a scan.
4. Review the detected changes.
5. Open the generated HTML security report.

---

# Example Workflow

```text
1. Clone Repository
        ↓
2. Enter Project Directory
        ↓
3. Run FileGuard
        ↓
4. Create Baseline
        ↓
5. Files Are Hashed
        ↓
6. Files Are Modified, Added, or Deleted
        ↓
7. Run Scan
        ↓
8. Changes Are Detected
        ↓
9. Severity Is Calculated
        ↓
10. HTML Report Is Generated
```

---

## FileGuard

### Monitor. Compare. Detect. Protect.
