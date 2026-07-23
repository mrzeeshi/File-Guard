# FileGuard

### File Integrity Monitoring Tool

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Cybersecurity](https://img.shields.io/badge/Category-Cybersecurity-red)](https://github.com/mrzeeshi/File-Guard)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

FileGuard is a lightweight cybersecurity tool developed in Python for monitoring the integrity of files and folders.

It uses SHA-256 cryptographic hashing to create a trusted baseline of files and later compares the current state of the folder against that baseline.

FileGuard can detect:

* Unchanged files
* Modified files
* Newly created files
* Deleted files

The tool also provides scan statistics, severity classification, user confirmation for baseline updates, and a visual HTML security report.

---

## Features

### SHA-256 File Hashing

FileGuard calculates a SHA-256 hash for every monitored file.

A hash acts as a digital fingerprint of a file. If the contents of a file change, its SHA-256 hash will normally also change.

### Recursive Folder Scanning

FileGuard scans the selected folder and its subfolders recursively.

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

The user is then asked whether the hash of the new file should be added to the baseline.

### Deleted File Detection

If a file exists in the baseline but is missing during the current scan, it is classified as:

```text
DELETED
```

The user is asked whether the deletion was intentional. If the user confirms the deletion, the file is removed from the baseline. Otherwise, it remains in the baseline as a possible unauthorized deletion.

### User Confirmation

FileGuard asks the user to confirm important changes before updating the trusted baseline.

This helps prevent the tool from automatically trusting every detected change.

### Severity Classification

The tool calculates an overall security status based on the detected changes.

| Severity | Description                                  |
| -------- | -------------------------------------------- |
| LOW      | No changes detected                          |
| MEDIUM   | New or deleted files detected                |
| HIGH     | Existing files have been modified            |
| CRITICAL | Both modified and deleted files are detected |

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

The project uses Python's standard library and does not require external Python packages.

---

# Installation

## Clone the Repository

Open a terminal or command prompt and run:

```bash
git clone https://github.com/mrzeeshi/File-Guard.git
```

This will create a folder named:

```text
File-Guard
```

Move into the project directory:

```bash
cd File-Guard
```

---

# Running FileGuard

## Windows

Open Command Prompt or PowerShell inside the `File-Guard` folder and run:

```bash
python file_guard.py
```

## Linux

Open the terminal and run:

```bash
python3 file_guard.py
```

## macOS

Open Terminal and run:

```bash
python3 file_guard.py
```

If `python3` is not available, try:

```bash
python file_guard.py
```

---

# Quick Start

```bash
git clone https://github.com/mrzeeshi/File-Guard.git
cd File-Guard
python file_guard.py
```

On Linux and macOS:

```bash
git clone https://github.com/mrzeeshi/File-Guard.git
cd File-Guard
python3 file_guard.py
```

After launching the program:

1. Select the required operation.
2. Provide the complete path of the folder to monitor.
3. Create a baseline or scan an existing baseline.
4. Review the detected changes.
5. Confirm legitimate new or deleted files when prompted.
6. Review the generated HTML security report.

---

# Program Options

When the program starts, it provides two options:

```text
========================================
             FILEGUARD
     File Integrity Monitoring Tool
========================================

1. Create Baseline
2. Scan Folder
```

---

# Creating a Baseline

A baseline represents the trusted state of a folder.

When creating a baseline, provide the complete path of the folder that you want to monitor.

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

FileGuard scans the folder and all of its subfolders. It calculates a SHA-256 hash for every file and stores the results in:

```text
baseline.json
```

Example:

```json
{
    "file1.txt": "sha256_hash_value",
    "Documents/report.pdf": "sha256_hash_value",
    "Images/photo.jpg": "sha256_hash_value"
}
```

---

# Scanning a Folder

After creating a baseline, select the scan option.

The tool will:

1. Scan the selected folder.
2. Calculate current hashes.
3. Load the trusted baseline.
4. Compare current hashes with baseline hashes.
5. Detect changes.
6. Classify the results.
7. Ask for confirmation where required.
8. Update the baseline when confirmed.
9. Generate a security report.

Example output:

```text
========================================
        FILEGUARD SECURITY SCAN
========================================

[UNCHANGED]  report.pdf
[MODIFIED]   config.txt
[NEW]        new_file.txt
[DELETED]    old_file.docx

========================================
              SCAN SUMMARY
========================================

Files checked: 25
Unchanged:     22
Modified:      1
New:           1
Deleted:       1
Severity:      CRITICAL
========================================
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

1. Create a baseline.
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

The tool will ask:

```text
Do you want to save the hash of this new file? (y/n):
```

If the user enters `y`, the file's hash is added to the baseline.

---

## Test 4: Deleted File

1. Create a baseline.
2. Delete one of the files.
3. Run FileGuard.

Expected result:

```text
[DELETED] file2.txt
```

The tool will ask:

```text
Did you intentionally delete this file? (y/n):
```

If the user enters `y`, the file is removed from the baseline.

If the user enters `n`, the file remains in the baseline and the deletion is treated as a possible unauthorized deletion.

---

# Generated Files

FileGuard automatically creates and updates the following files during operation.

## baseline.json

This file stores the trusted baseline of the monitored folder.

It contains:

* Relative file paths
* SHA-256 hashes

Example:

```json
{
    "file1.txt": "sha256_hash_value",
    "Documents/report.pdf": "sha256_hash_value"
}
```

When a new baseline is created, the file is generated or overwritten.

During scanning, the file may be updated when the user confirms new files or intentional deletions.

---

## fileguard_report.html

This file is automatically generated after a scan.

It contains:

* Scan time
* Monitored folder
* Number of files checked
* Unchanged file count
* Modified file count
* New file count
* Deleted file count
* Overall security severity
* Detailed security findings

The report can be opened directly in a web browser.

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

```text
File-Guard/
├── file_guard.py
├── baseline.json
├── fileguard_report.html
├── Report File Guard.pdf
└── README.md
```

## File Descriptions

| File                    | Description                                         |
| ----------------------- | --------------------------------------------------- |
| `file_guard.py`         | Main Python source code                             |
| `baseline.json`         | Stores trusted file paths and SHA-256 hashes        |
| `fileguard_report.html` | Generated visual security report                    |
| `Report File Guard.pdf` | Complete project report and technical documentation |
| `README.md`             | Project documentation and usage instructions        |

> `baseline.json` and `fileguard_report.html` are generated and updated automatically by the program during operation.

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

The complete project report is included in the repository:

```text
Report File Guard.pdf
```

The report explains:

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

# Repository

The complete source code and project documentation are available on GitHub:

https://github.com/mrzeeshi/File-Guard

---

## FileGuard

### Monitor. Compare. Detect. Protect.
