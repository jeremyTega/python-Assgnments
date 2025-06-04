import pprint
all_employee = []

def display_menu():
    print("""
                       MAIN MENU
            ======================================
            Welcome to semicolon employee payroll:
            ======================================

                  1  -> add employee payroll
                  2  -> view employee payroll
                  3  -> update employee payroll
                  4  -> Exit

            ======================================
                Kindly enter your choice below:
            ======================================
    """)
    user_input = int(input("Choose one: "))
    return user_input



def addemployee(name, hours_worked, hourly_pay, federal_tax_rate, state_tax_rate):

    name = name.lower()

    for employee_name in all_employee:

        if employee_name.get("name") == name:
            return ("name already exists")




    gross_pay = hours_worked * hourly_pay
    federal_tax = gross_pay * federal_tax_rate
    state_tax = gross_pay * state_tax_rate
    total_deductions = federal_tax + state_tax
    net_pay = gross_pay - total_deductions

    employee = {
        'name': name,
        'hours_worked': hours_worked,
        'hourly_pay': hourly_pay,
        'gross_pay': gross_pay,
        'federal_tax': federal_tax,
        'state_tax': state_tax,
        'total_deductions': total_deductions,
        'net_pay': net_pay
    }

    all_employee.append(employee)
    print("====employee added=====")
    return employee


def view_employee_list():
    pprint.pprint(all_employee)




def edit_employee_details(name):
    name = name.lower()
    for employee in all_employee:
        if employee.get("name") == name:
            pprint.pprint(employee)
            print("\nEnter new details (leave blank to keep current value):")


            hours_worked = input(f"Hours Worked ({employee['hours_worked']}): ")
            if hours_worked:
                hours_worked = int(hours_worked)
                employee['hours_worked'] = hours_worked

            hourly_pay = input(f"Hourly Pay ({employee['hourly_pay']}): ")
            if hourly_pay:
                hourly_pay = float(hourly_pay)
                employee['hourly_pay'] = hourly_pay


            federal_tax_rate = input(f"Federal Tax Rate ({employee['federal_tax']}): ")
            if federal_tax_rate:
                federal_tax_rate = float(federal_tax_rate)
                employee['federal_tax'] = federal_tax_rate


            state_tax_rate = input(f"State Tax Rate ({employee['state_tax']}): ")
            if state_tax_rate:
                state_tax_rate = float(state_tax_rate)
                employee['state_tax'] = state_tax_rate


            gross_pay = employee['hours_worked'] * employee['hourly_pay']
            federal_tax = gross_pay * employee['federal_tax']
            state_tax = gross_pay * employee['state_tax']
            total_deductions = federal_tax + state_tax
            net_pay = gross_pay - total_deductions


            employee.update({
                'gross_pay': gross_pay,
                'federal_tax': federal_tax,
                'state_tax': state_tax,
                'total_deductions': total_deductions,
                'net_pay': net_pay
            })

            print("==== Employee details updated successfully ====")
            return employee

    print("Employee not found.")
    return None















