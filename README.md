# Employee Attendance System

A beginner-friendly console-based Employee Attendance System developed
using **Python 3**. The application lets a user add employees, record
daily attendance, view attendance reports, and save records so they
remain available after the program closes.

## Project Details

-   **Project Number:** PS No. 36
-   **Project Title:** Employee Attendance System
-   **Language:** Python 3
-   **Storage:** Local text file (`attendance.txt`) containing
    JSON-formatted data
-   **Main Concepts:** Lists, dictionaries, functions, loops,
    conditional statements, date validation, and file handling

## Features

1.  **Add Employee**
    -   Enter an employee's name.
    -   The program automatically generates an ID, beginning with
        `E101`.
2.  **Mark Attendance**
    -   Select an employee using their ID.
    -   Enter the date in `YYYY-MM-DD` format.
    -   Enter one of the supported attendance statuses:
        -   `P` --- Present
        -   `A` --- Absent
        -   `L` --- Leave
    -   The program rejects unknown employee IDs, invalid dates, invalid
        statuses, and duplicate attendance entries for the same employee
        and date.
3.  **View Attendance Report**
    -   Displays the employee's present, absent, and leave counts.
    -   Calculates attendance percentage using:

    ``` text
    Attendance (%) = (Present Days / Total Marked Days) × 100
    ```

    -   If no attendance has been recorded, the report displays
        `0.00% (no records)`.
4.  **Save and Load Records**
    -   Records are saved to `attendance.txt`.
    -   Existing records are loaded when the application starts.

## Project Structure

``` text
Employee_Attendance_System/
│
├── attendance_system.py
├── attendance.txt          # Created automatically when data is saved
└── README.md
```

## Requirements

-   Python 3.8 or later recommended
-   VS Code or another Python editor (optional)
-   No third-party Python packages are required; the project uses
    Python's standard library.

## How to Run

1.  Download or clone this project.

2.  Open the project folder in a terminal or VS Code.

3.  Run:

    ``` bash
    python attendance_system.py
    ```

    On some Windows systems, use:

    ``` bash
    py attendance_system.py
    ```

4.  Choose an option from the menu:

    ``` text
    ===== EMPLOYEE ATTENDANCE SYSTEM =====
    1. Add Employee
    2. Mark Attendance
    3. View Attendance Report
    4. Exit
    ```

## Example Usage

### Add an employee

``` text
Enter your choice: 1
Enter employee name: Aman
Employee added: E101 | Aman
```

### Mark attendance

``` text
Enter your choice: 2
Enter employee ID: E101
Enter date (YYYY-MM-DD): 2026-08-01
Enter status (P/A/L): P
Attendance marked successfully!
```

### View report

If Aman has two Present records, one Absent record, and one Leave
record:

``` text
Aman: Present 2 | Absent 1 | Leave 1
Attendance: 50.00%
```

## Test Cases

  -----------------------------------------------------------------------
  Test Case               Input / Scenario        Expected Result
  ----------------------- ----------------------- -----------------------
  1\. Normal input        Add employee named Aman Employee is added with
                                                  ID `E101`

  2\. Minimum input       View E101's report      Present 0, Absent 0,
                          before marking          Leave 0;
                          attendance              `0.00% (no records)`

  3\. Invalid input       Use unknown ID `E999`,  Appropriate error
                          invalid date            message; invalid record
                          `2026-13-45`, or status is not saved
                          `X`                     

  4\. Different valid     Mark P, P, A, L on four Present 2, Absent 1,
  scenario                different dates         Leave 1; attendance
                                                  `50.00%`; duplicate
                                                  date is rejected
  -----------------------------------------------------------------------

**Note:** Run the test cases in the specified order using the same data
file. If you want to repeat the tests from a clean state, close the
program and remove or rename the existing `attendance.txt` file first.

## Data Storage

Employee information is stored in `attendance.txt` in JSON format. A
record contains:

-   Employee ID
-   Employee name
-   Attendance dates and their status codes

Do not delete `attendance.txt` if you want to keep the saved records.
Keep the file in the same project folder as `attendance_system.py`.

## Limitations

-   This is a basic, single-user console application.
-   It stores data locally; it does not use a database or cloud storage.
-   It does not include a graphical user interface or user login system.

## Future Improvements

-   Add employee search and update options.
-   Add monthly attendance reports.
-   Export reports to CSV.
-   Add a graphical user interface.
-   Use a database for larger datasets.

## Author

**Student Project --- Python 3**

Created as an academic project to demonstrate basic Python programming
concepts.
