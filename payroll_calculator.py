# Name
# Employee ID
# The number of hours worked during the week
# The wage by hour
# If the employee is unionized
def payroll():
    name = input("Hello, please enter your name in the following format. (first last) : ")
    empid = input(f"Welcome {name}, please enter your employee id. :")
    hours_worked = float(input("Now enter the number of hours you worked during the week. : "))
    wage = float(input("Please enter your hourly wage. : "))
    union = input("Are you unionized? Please answer with 'Y' or 'N'. : ").lower()

    # Wages

    if hours_worked > 40:
        overtime = hours_worked - 40
        hours_worked = 40
        overtime_weekly = overtime * (wage * 1.5)
        regular_weekly = hours_worked * wage
        gross_weekly_wage = regular_weekly + overtime_weekly
        gross_bi_weekly_wage = gross_weekly_wage * 2
        regular_bi_weekly_wage = regular_weekly * 2
        bi_overtime = overtime_weekly * 2
        yearly_wage = gross_bi_weekly_wage * 26
        yearly_overtime = overtime_weekly * 26
        yearly_regular = regular_bi_weekly_wage * 26
    else:
        gross_weekly_wage = hours_worked * wage 
        gross_bi_weekly_wage = gross_weekly_wage * 2
        yearly_wage = gross_bi_weekly_wage * 26
        overtime = 0
        overtime_weekly = 0
        regular_weekly = gross_weekly_wage
        regular_bi_weekly_wage = gross_bi_weekly_wage
        bi_overtime = overtime_weekly * 2
        yearly_overtime = 0
        yearly_regular = regular_bi_weekly_wage * 26


    # Deductions

    # Union
    if union == "y":
        union_fee = yearly_wage * 0.01
    else:
        union_fee = 0
    bi_union_fee = union_fee / 26

    # Retirement
    retirement = yearly_wage * 0.045
    bi_retirement = retirement / 26

    # State
    state_tax = yearly_wage * 0.06
    bi_state_tax = state_tax / 26

    # Federal 
    tax_brackets = [(0, 11600), (11600, 47150), (47150, 100525), (100525, 191950), (191950, 243725)]
    tax_rates = [0.1, 0.12, 0.22, 0.24, 0.32]
    federal_tax = 0
    for bracket, rate in zip(tax_brackets, tax_rates):
        lower, upper = bracket
        if yearly_wage > upper:
            federal_tax += (upper - lower + 1) * rate
        elif yearly_wage >= lower:
            federal_tax += (yearly_wage - lower + 1) * rate
    bi_federal_tax = federal_tax / 26

    # Social Security
    if yearly_wage > 147000:
        sosec = 147000 * 0.062
    elif yearly_wage < 147000:
        sosec = yearly_wage * 0.062
    bi_sosec = sosec / 26

    # Medicaid
    if yearly_wage > 147000:
        medical = 147000 * 0.062
    elif yearly_wage < 147000:
        medical = yearly_wage * 0.0145
    bi_medical = medical / 26

    # Net pay
    deductions = union_fee + retirement + state_tax + federal_tax + sosec + medical
    net_pay = yearly_wage - deductions
    bi_deductions = bi_union_fee + bi_retirement + bi_state_tax + bi_federal_tax + bi_sosec + bi_medical
    bi_net_pay = gross_bi_weekly_wage - bi_deductions

    # Bi-Weekly Output
    print("Bi-Weekly Pay")
    print("Employee ID:", empid)
    print("Name:", name)
    print("\nWages total:")
    print("    Regular time: ${:.2f}".format(regular_bi_weekly_wage))
    print("    Overtime: ${:.2f}".format(bi_overtime))
    print("    Gross income: ${:.2f}".format(gross_bi_weekly_wage))
    print("\nDeductions:")
    print("    Union fees: ${:.2f}".format(bi_union_fee))
    print("    Retirement fund: ${:.2f}".format(bi_retirement))
    print("    State taxes: ${:.2f}".format(bi_state_tax))
    print("    Federal taxes: ${:.2f}".format(bi_federal_tax))
    print("    Social Security: ${:.2f}".format(bi_sosec))
    print("    Medicaid: ${:.2f}".format(bi_medical))
    print("\nNet-pay: ${:.2f}".format(bi_net_pay))

    # Annual Output
    print("\nAnnual Gross Pay")
    print("Employee ID:", empid)
    print("Name:", name)
    print("\nWages total:")
    print("    Regular time: ${:.2f}".format(yearly_regular))
    print("    Overtime: ${:.2f}".format(yearly_overtime))
    print("    Gross income: ${:.2f}".format(yearly_wage))
    print("\nDeductions:")
    print("    Union fees: ${:.2f}".format(union_fee))
    print("    Retirement fund: ${:.2f}".format(retirement))
    print("    State taxes: ${:.2f}".format(state_tax))
    print("    Federal taxes: ${:.2f}".format(federal_tax))
    print("    Social Security: ${:.2f}".format(sosec))
    print("    Medicaid: ${:.2f}".format(medical))
    print("\nNet-pay: ${:.2f}".format(net_pay))

payroll()
