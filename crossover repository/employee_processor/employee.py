employee_records = []
department_summary = {}

def process_record(record):
    parts = [p.strip() for p in record.split('|')]
    if len(parts) != 4:
        print("Invalid record format. Please use: ID | Name | Department | Salary")
        return

    emp_id, name, department, salary_str = parts
    try:
        salary = int(salary_str)
    except ValueError:
        print("Salary must be a number.")
        return

    employee = {
        "ID": emp_id,
        "Name": name,
        "Department": department,
        "Salary": salary
    }
    employee_records.append(employee)

    if department not in department_summary:
        department_summary[department] = {
            "total_salary": 0,
            "employee_count": 0
        }

    department_summary[department]["total_salary"] += salary
    department_summary[department]["employee_count"] += 1
    print("Record added successfully.\n")

def show_menu():
    print("\n--- Options ---")
    print("1. Add new employee record")
    print("2. Show number of employees in a department")
    print("3. Show average salary of a department")
    print("4. Show all departments")
    print("5. Show number of employees in each department")
    print("6. Show average salary for each department")
    print("7. Show all employee records")
    print("8. Quit")

while True:
    show_menu()
    choice = input("Enter your choice (1-8): ").strip()

    if choice == "1":
        new_record = input("Enter employee record (ID | Name | Department | Salary): ")
        process_record(new_record)

    elif choice == "2":
        dept = input("Enter department name: ").strip()
        if dept in department_summary:
            print(f"Number of employees in {dept}: {department_summary[dept]['employee_count']}\n")
        else:
            print(f"No data available for department '{dept}'.\n")

    elif choice == "3":
        dept = input("Enter department name: ").strip()
        if dept in department_summary:
            info = department_summary[dept]
            avg_salary = info['total_salary'] // info['employee_count']
            print(f"Average salary in {dept}: {avg_salary}\n")
        else:
            print(f"No data available for department '{dept}'.\n")

    elif choice == "4":
        if not department_summary:
            print("No departments available yet.\n")
        else:
            print("Departments with data:")
            for dept in department_summary:
                print(f"- {dept}")
            print()

    elif choice == "5":
        if department_summary:
            print("\n--- Number of Employees in Each Department ---")
            for dept, info in department_summary.items():
                print(f"{dept}: {info['employee_count']} employees")
            print()
        else:
            print("No data available yet.\n")

    elif choice == "6":
        if department_summary:
            print("\n--- Average Salary for Each Department ---")
            for dept, info in department_summary.items():
                avg_salary = info["total_salary"] // info["employee_count"]
                print(f"{dept}: Average Salary = {avg_salary}")
            print()
        else:
            print("No data available yet.\n")

    elif choice == "7":
        if employee_records:
            print("\n--- All Employee Records ---")
            for emp in employee_records:
                print(emp)
            print()
        else:
            print("No employee records found.\n")

    elif choice == "8":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 8.\n")
