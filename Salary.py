class Salary:
    def __init__(self,basic,allowance):
        self.basic=basic
        self.allowance=allowance

    def calculate_net_salary(self):
        return self.basic+self.allowance
    
def main():  
    basic_salary=input("Enter Basic Salary= ")
    allowance=input("Enter Allowance= ")

    if basic_salary.replace(".","").isdigit() and allowance.replace(".","").isdigit():
        basic_salary=float(basic_salary)
        allowance=float(allowance)

    salary=Salary(basic_salary,allowance)
    net_salary=salary.calculate_net_salary()

    print("Net Salary= ",net_salary)

if __name__=="__main__":
    main()