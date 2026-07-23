import hashlib
import os
import json
from datetime import datetime

BASELINE_FILE = "baseline.json"
REPORT_FILE = "fileguard_report.html"


def calculate_hash(file_path):

    file = open(file_path, "rb")

    content = file.read()

    file.close()

    file_hash = hashlib.sha256(content).hexdigest()

    return file_hash


def create_baseline(folder):

    baseline = {}

    for root, directories, files in os.walk(folder):

        for file in files:

            file_path = os.path.join(root, file)

            relative_path = os.path.relpath(file_path, folder)

            file_hash = calculate_hash(file_path)

            baseline[relative_path] = file_hash


    with open(BASELINE_FILE, "w") as file:

        json.dump(baseline, file, indent=4)


    print("\n[+] Baseline created successfully.")

    print("[+] Files stored:", len(baseline))


def load_baseline():

    with open(BASELINE_FILE, "r") as file:

        baseline = json.load(file)

    return baseline


def save_baseline(baseline):

    with open(BASELINE_FILE, "w") as file:

        json.dump(baseline, file, indent=4)


def get_current_files(folder):

    current_files = []

    for root, directories, files in os.walk(folder):

        for file in files:

            file_path = os.path.join(root, file)

            relative_path = os.path.relpath(file_path, folder)

            current_files.append(relative_path)


    return current_files


def scan_folder(folder, baseline):

    current_files = get_current_files(folder)


    unchanged_count = 0

    modified_count = 0

    new_count = 0

    deleted_count = 0


    findings = []


    print("\n========================================")

    print("        FILEGUARD SECURITY SCAN")

    print("========================================\n")


    print("[+] Scanning folder:", folder)

    print("[+] Scan started...\n")


    # Check current files

    for relative_path in current_files:


        file_path = os.path.join(folder, relative_path)

        current_hash = calculate_hash(file_path)


        if relative_path in baseline:


            old_hash = baseline[relative_path]


            if current_hash == old_hash:

                print("[UNCHANGED] ", relative_path)

                unchanged_count += 1


            else:

                print("[MODIFIED]  ", relative_path)

                modified_count += 1

                findings.append("[MODIFIED] " + relative_path)


        else:

            print("[NEW]        ", relative_path)

            new_count += 1

            findings.append("[NEW] " + relative_path)


            answer = input(

                "Do you want to save the hash of this new file? (y/n): "

            )


            if answer.lower() == "y":

                baseline[relative_path] = current_hash

                print("[+] File added to baseline.")

            else:

                print("[-] File was not added to baseline.")


    # Check deleted files

    for relative_path in list(baseline):


        if relative_path not in current_files:


            print("\n[DELETED]    ", relative_path)

            deleted_count += 1

            findings.append("[DELETED] " + relative_path)


            answer = input(

                "Did you intentionally delete this file? (y/n): "

            )


            if answer.lower() == "y":

                del baseline[relative_path]

                print("[+] File removed from baseline.")


            else:

                print("[!] File remains in baseline.")

                print("[!] Possible unauthorized deletion.")


    save_baseline(baseline)


    # Calculate severity

    if modified_count > 0 and deleted_count > 0:

        severity = "CRITICAL"

    elif modified_count > 0:

        severity = "HIGH"

    elif new_count > 0 or deleted_count > 0:

        severity = "MEDIUM"

    else:

        severity = "LOW"


    # Display summary

    print("\n========================================")

    print("              SCAN SUMMARY")

    print("========================================")

    print("Files checked: ", len(current_files))

    print("Unchanged:     ", unchanged_count)

    print("Modified:      ", modified_count)

    print("New:           ", new_count)

    print("Deleted:       ", deleted_count)

    print("Severity:      ", severity)

    print("========================================")


    create_html_report(

        folder,

        len(current_files),

        unchanged_count,

        modified_count,

        new_count,

        deleted_count,

        severity,

        findings

    )


def create_html_report(

    folder,

    files_checked,

    unchanged_count,

    modified_count,

    new_count,

    deleted_count,

    severity,

    findings

):


    with open(REPORT_FILE, "w") as report_file:


        report_file.write("""

<!DOCTYPE html>

<html>

<head>

<title>FileGuard Security Report</title>


<style>

body {

    font-family: Arial, sans-serif;

    margin: 40px;

    background-color: #f4f6f8;

}


.container {

    max-width: 1000px;

    margin: auto;

}


.header {

    background-color: #1f2937;

    color: white;

    padding: 25px;

    border-radius: 10px;

}


.cards {

    display: flex;

    gap: 15px;

    margin-top: 20px;

    flex-wrap: wrap;

}


.card {

    background-color: white;

    padding: 20px;

    border-radius: 10px;

    flex: 1;

    min-width: 140px;

    box-shadow: 0 2px 5px #cccccc;

}


.card h2 {

    margin: 0;

}


.status {

    margin-top: 20px;

    padding: 20px;

    background-color: white;

    border-radius: 10px;

    font-size: 22px;

    font-weight: bold;

}


.findings {

    margin-top: 20px;

    background-color: white;

    padding: 20px;

    border-radius: 10px;

}


.finding {

    padding: 10px;

    border-bottom: 1px solid #dddddd;

}


</style>

</head>


<body>


<div class="container">


<div class="header">

<h1>FileGuard Security Report</h1>

<p>File Integrity Monitoring Tool</p>

<p>Scan Time: """ + str(datetime.now()) + """</p>

<p>Folder: """ + folder + """</p>

</div>


<div class="cards">


<div class="card">

<h2>""" + str(files_checked) + """</h2>

<p>Files Checked</p>

</div>


<div class="card">

<h2>""" + str(unchanged_count) + """</h2>

<p>Unchanged</p>

</div>


<div class="card">

<h2>""" + str(modified_count) + """</h2>

<p>Modified</p>

</div>


<div class="card">

<h2>""" + str(new_count) + """</h2>

<p>New</p>

</div>


<div class="card">

<h2>""" + str(deleted_count) + """</h2>

<p>Deleted</p>

</div>


</div>


<div class="status">

Security Status: """ + severity + """

</div>


<div class="findings">

<h2>Security Findings</h2>

""")


        if len(findings) == 0:

            report_file.write(

                "<p>No security changes were detected.</p>"

            )


        else:

            for finding in findings:

                report_file.write(

                    "<div class='finding'>" + finding + "</div>"

                )


        report_file.write("""

</div>


</div>


</body>

</html>

""")


    print("\n[+] HTML report saved as:", REPORT_FILE)


def main():


    print("========================================")

    print("             FILEGUARD")

    print("     File Integrity Monitoring Tool")

    print("========================================")


    print("\n1. Create Baseline")

    print("2. Scan Folder")


    choice = input("\nSelect an option (1/2): ")


    folder = input(

        "\nEnter the complete path of the folder to monitor:\n"

    )


    folder = folder.strip().strip('"')


    if not os.path.exists(folder):

        print("\n[ERROR] Folder does not exist.")

        return


    if not os.path.isdir(folder):

        print("\n[ERROR] The provided path is not a folder.")

        return


    if choice == "1":

        create_baseline(folder)


    elif choice == "2":

        if not os.path.exists(BASELINE_FILE):

            print("\n[ERROR] No baseline found.")

            print("[!] Create a baseline first.")

            return


        baseline = load_baseline()

        scan_folder(folder, baseline)


    else:

        print("\n[ERROR] Invalid option.")


main()
