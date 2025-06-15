This is a simple menu-driven Python program to manage employee records. It allows you to input employee data, organize them by departments, and retrieve useful summaries such as the number of employees and average salary per department.



/Features

- Add new employee records
-  Show:
  - Number of employees in a department
  - Average salary of a department
  - All departments
  - Number of employees in each department
  - Average salary for each department
  - All employee records
-  Input validation and error messages for incorrect formats
-  Internally stores data using:
  - List of dictionaries for employee records
  - Dictionary for department-wise summaries

/Sample Input & Output

/Input:

Enter employee record (ID | Name | Department | Salary):
101 | Alice Johnson | Sales | 50000

/Output:

Record added successfully.


/Output Example for Menu Option 6 (Average salary for each department):

\ Average Salary for Each Department 
Sales: Average Salary = 50000
HR: Average Salary = 42000


/How the Code Works

- The program keeps running until the user selects **option 8 (Quit)**.
- On each run:
  - It shows a menu of options.
  - Based on the user’s input, it either adds a record or shows processed data.
- Employee records are stored in a list of dictionaries (`employee_records`).
- Department summaries (employee count, total salary) are maintained in a dictionary (`department_summary`).



/Input Format

When adding a record, use the format below:
ID | Name | Department | Salary

/Example:

103 | Mark Lee | IT | 60000


/Invalid Examples:

103, Mark Lee, IT, 60000
103 | Mark Lee | IT


/How to Run the Program

/Requirements:
- Python 3 installed on your system

/Steps to Execute:

1. Open a terminal or command prompt
2. Navigate to the folder where `employee_manager.py` is located
3. Run the following command:

bash
python employee_manager.py

Or if Python 3 is required explicitly:

bash
python3 employee.py


---

/Menu Options

When you run the program, you'll see:


--- Options ---
1. Add new employee record
2. Show number of employees in a department
3. Show average salary of a department
4. Show all departments
5. Show number of employees in each department
6. Show average salary for each department
7. Show all employee records
8. Quit

/Assumptions

Salaries are valid integers.
Input format is consistent (`ID | Name | Department | Salary`).
Data is stored in memory only (not persisted to disk).




