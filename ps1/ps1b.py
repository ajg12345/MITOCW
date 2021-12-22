#ps1b.py


annual_salary = int(input('what is your annual_salary?'))
portion_saved = float(input('what is your percentage saved?(in decimal form)'))
total_cost = int(input('what is the cost of your dream home?'))
semi_annual_raise = float(input('what is your semi_annual_raise?(in decimal form)'))

monthly_savings = (annual_salary /12) * portion_saved
portion_down_payment = total_cost * .25
current_savings = 0
month = 0
while current_savings < portion_down_payment:
    current_savings += monthly_savings + (current_savings*0.04)/12
    month += 1
    if month % 6 == 0:
        annual_salary += annual_salary*semi_annual_raise
        monthly_savings = (annual_salary /12) * portion_saved
    
print("NUMBER OF MONTHS " + str(month))


