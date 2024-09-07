# initialization all variables
net_income = 0
gross = 0
total_deduction = 0
name_of_the_employee = ""
pagibig_contribution = 100.0


# getting inputs for rates
name_of_the_employee = input("Enter the name of employee")
rate_per_hours = float(input("Enter the employee's rate per hour:"))
number_hours_per_day = float(input("work number of hours per day:"))
number_day_per_week = int(input("Enter employee's working number of days per week:"))
number_weeks_per_month = int(input("Enter employee's number of weeks per month:"))


# getting
gross = round(number_hours_per_day * number_day_per_week * number_weeks_per_month)

# calculation

if 0 <= gross <= 20000:
    sss_contri = 125.5
    philhealth_contri = 100.00
elif 20001 <= gross <= 50000:
    sss_contri = 2200.50
    philhealth_contri = 1200.00
elif 50001 <= gross <= 75000:
    sss_contri = 4800.00
    philhealth_contri = 6800
else:
    sss_contri = 5800
    philhealth_contri = 8800

# formula
total_deduction = sss_contri + philhealth_contri + pagibig_contribution
net_income = gross - total_deduction

# displaying of name of employee, net income, gross , total deduction
print("Employee name:", name_of_the_employee)
print("net income:", f"{net_income: .2f}")
print("gross:", f"{gross: .2f}")
print("total deduction:", total_deduction)
