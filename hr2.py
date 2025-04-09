def compute_wage(hours_worked,rate):
    wage = hours_worked * rate
    return wage

def compute_allowance(wage,allowance_rate):
    allowance = wage * allowance_rate
    return allowance

def compute_grosswage(wage,allowance):
    grosswage = wage + allowance
    return grosswage

def compute_tax(wage,tax_rate):
    tax = wage * tax_rate
    return tax

def compute_netwage(wage,tax):
    netwage = wage - tax
    return netwage

hours = int(input("Enter Hours Worked: "))
rate = int(input("Enter Rate: "))

wage = compute_wage(hours,rate)
allowance = compute_allowance(wage,0.1)
grosswage = compute_grosswage(wage,allowance)
tax = compute_tax(wage,0.01)
netwage = compute_netwage(wage,tax)

print(f"Wage = {wage}")