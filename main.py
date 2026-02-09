from Employee import main as employee_main
from Salary import main as salary_main


def main_menu():
    print("Welcome to the Employee Management System")
    print("1. Employee Information")
    print("2. Salary Calculation")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        employee_main()
    elif choice == '2':
        salary_main()
    elif choice == '3':
        print("Exiting the program. Goodbye!")
    else:
        print("Invalid choice. Please try again.")
        main_menu()

if __name__ == "__main__":
    main_menu()