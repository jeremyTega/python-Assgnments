import employeeList
while True:
    userInput= employeeList.display_menu()
    match userInput:
        case 1:
            while True:
                print("=====welcome to semicolon Employee payroll====")
                name = input("enter employee name: ")
                hours_worked = int(input("enter the hours you worked in hrs(eg 24): "))
                while hours_worked > 40:
                    hours_worked = int(input("you be mumu abeg enter hour we de less that 40: "))
                    if(hours_worked <= 40):
                        break
                hourly_rate = float(input("enter hours pay (eg 9.67): "))
                federal_tax_rate = float(input("enter fedral taxt rate in percent eg. 20:  "))
                state_tax_rate = float(input("enter state taxt rate in percent eg. 20:  "))
                employeeList.addemployee(name,hours_worked,hourly_rate,federal_tax_rate,state_tax_rate)
                # print("====employee added=====")
                employeeList.display_menu()
                break
        case 2:
            employeeList.view_employee_list()
            employeeList.display_menu()
        case 3:
            employee_name = input("enter employee name")
            employee_name.lower()
            employeeList.edit_employee_details(employee_name)
        case 4:
            print("exiciting......")
            break



