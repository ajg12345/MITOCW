#ps1a.py


annual_salary = int(input('what is your annual_salary?'))
monthly_salary = annual_salary/12
portion_saved = monthly_salary*float(input('what is your percentage saved?'))
total_cost = int(input('what is the cost of your dream home?'))
portion_down_payment = total_cost * .25
current_savings = 0
r = 0.04
#at the end of each month, savings = return on investment plus percentage of monthly salary

print('with investment')
month = 1
while current_savings < portion_down_payment:
    return_on_investment = current_savings*r/12
    current_savings += portion_saved + return_on_investment
    #print("month " + str(month) + " and savings are " + str(current_savings))
    month += 1
print("the month is " + str(month))
print("you have saved "+ str(current_savings))
current_savings = 0
print('without investment')
month = 1
while current_savings < portion_down_payment:
    return_on_investment = 0
    current_savings += portion_saved + return_on_investment
    #print("month " + str(month) + " and savings are " + str(current_savings))
    month += 1
print("the month is " + str(month))
print("you have saved "+ str(current_savings))
