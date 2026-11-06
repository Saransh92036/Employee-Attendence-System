from datetime import datetime
from pathlib import Path

DATA_FILE = Path(__file__).with_name("attendance.txt")
employees = []  # Each employee: {"id": "E101", "name": "Aman", "records": [{"date": "...", "status": "P"}]}


def load_data():
    """Load employees and attendance records from the text file."""
    employees.clear()

    if not DATA_FILE.exists():
        return

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            for line in file:
                parts = line.rstrip("\n").split("|")
                if len(parts) != 4:
                    continue

                employee_id, name, date_text, status = parts
                employee = find_employee(employee_id)

                if employee is None:
                    employee = {"id": employee_id, "name": name, "records": []}
                    employees.append(employee)

                # Ignore malformed or duplicate records in an existing file.
                try:
                    datetime.strptime(date_text, "%Y-%m-%d")
                except ValueError:
                    continue

                if status in ("P", "A", "L") and not any(
                    record["date"] == date_text for record in employee["records"]
                ):
                    employee["records"].append({"date": date_text, "status": status})

    except OSError:
        print("Warning: Could not read attendance.txt. Starting with available data.")


def save_data():
    """Save all employees and their attendance records to the text file."""
    try:
        with DATA_FILE.open("w", encoding="utf-8") as file:
            for employee in employees:
                if not employee["records"]:
                    # Keep employees with no attendance records.
                    file.write(f'{employee["id"]}|{employee["name"]}||\n')
                else:
                    for record in employee["records"]:
                        file.write(
                            f'{employee["id"]}|{employee["name"]}|'
                            f'{record["date"]}|{record["status"]}\n'
                        )
    except OSError:
        print("Error: Could not save data to attendance.txt.")


def find_employee(employee_id):
    """Return an employee dictionary, or None if the ID does not exist."""
    for employee in employees:
        if employee["id"] == employee_id:
            return employee
    return None


def next_employee_id():
    """Generate the next ID, beginning with E101."""
    highest_number = 100
    for employee in employees:
        try:
            number = int(employee["id"][1:])
            highest_number = max(highest_number, number)
        except (ValueError, IndexError):
            continue
    return f"E{highest_number + 1}"


def add_employee():
    name = input("Enter employee name: ").strip()

    if not name:
        print("Invalid name. Name cannot be empty.")
        return

    if "|" in name or "\n" in name:
        print("Invalid name. Do not use the | character.")
        return

    employee_id = next_employee_id()
    employees.append({"id": employee_id, "name": name, "records": []})
    save_data()
    print(f"Employee added: {employee_id} | {name}")


def valid_date(date_text):
    """Check that a date is in YYYY-MM-DD format and is a real date."""
    try:
        datetime.strptime(date_text, "%Y-%m-%d")
        return len(date_text) == 10
    except ValueError:
        return False


def mark_attendance():
    employee_id = input("Enter employee ID (e.g., E101): ").strip().upper()
    employee = find_employee(employee_id)

    if employee is None:
        print(f"Employee {employee_id} not found.")
        return

    date_text = input("Enter date (YYYY-MM-DD): ").strip()
    if not valid_date(date_text):
        print("Invalid date. Use YYYY-MM-DD.")
        return

    status = input("Enter status (P=Present, A=Absent, L=Leave): ").strip().upper()
    if status not in ("P", "A", "L"):
        print("Invalid status. Enter P, A or L.")
        return

    for record in employee["records"]:
        if record["date"] == date_text:
            print(f"Attendance for {date_text} is already marked.")
            return

    employee["records"].append({"date": date_text, "status": status})
    employee["records"].sort(key=lambda record: record["date"])
    save_data()
    print(f"Attendance marked: {employee_id} | {date_text} | {status}")


def show_report():
    employee_id = input("Enter employee ID (e.g., E101): ").strip().upper()
    employee = find_employee(employee_id)

    if employee is None:
        print(f"Employee {employee_id} not found.")
        return

    counts = {"P": 0, "A": 0, "L": 0}
    for record in employee["records"]:
        counts[record["status"]] += 1

    total_days = sum(counts.values())
    attendance_percentage = (counts["P"] / total_days * 100) if total_days else 0.0

    print(f"\nAttendance Report: {employee['id']} | {employee['name']}")
    print(f"Present: {counts['P']} | Absent: {counts['A']} | Leave: {counts['L']}")
    if total_days == 0:
        print("Attendance: 0.00% (no records)")
    else:
        print(f"Attendance: {attendance_percentage:.2f}%")
        print("\nDate       Status")
        print("-----------------")
        for record in sorted(employee["records"], key=lambda item: item["date"]):
            status_name = {"P": "Present", "A": "Absent", "L": "Leave"}[record["status"]]
            print(f"{record['date']}  {status_name}")


def main():
    load_data()
    print("=== Employee Attendance System ===")

    while True:
        print("\nMenu")
        print("1. Add employee")
        print("2. Mark attendance")
        print("3. View attendance report")
        print("4. Exit")

        choice = input("Enter menu option: ").strip()

        if choice == "1":
            add_employee()
        elif choice == "2":
            mark_attendance()
        elif choice == "3":
            show_report()
        elif choice == "4":
            save_data()
            print("Data saved. Exiting Employee Attendance System.")
            break
        else:
            print("Invalid menu option. Enter 1, 2, 3 or 4.")


if __name__ == "__main__":
    main()
