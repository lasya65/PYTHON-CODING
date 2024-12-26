# Tax Calculation Program
name = input('Enter the name of the employee: ')
id = input('Enter the ID of the employee: ')
basic_salary = float(input('Enter the monthly basic salary: '))
allowances = float(input('Enter the monthly allowances: '))
bonus_percent = float(input('Enter the employee Bonus(percent): '))

gross_monthly_salary = basic_salary + allowances
gross_annual_salary = (gross_monthly_salary + (gross_monthly_salary * bonus_percent / 100)) * 12

print(f'Gross Monthly Salary = {gross_monthly_salary}')
print(f'Gross Annual Salary = {gross_annual_salary}')


standard_deduction= 50000 # Annually
taxable_amount = gross_annual_salary - standard_deduction
#Level2
print(f'Standard Deduction Amount = {standard_deduction}')
print(f'Taxable Amount = {taxable_amount}')
