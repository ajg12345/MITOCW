#ps1c.py
import sys
annual_salary = int(input('Enter the startin salary:'))
total_cost = 1000000
semi_annual_raise = 0.07
portion_down_payment = total_cost * .25

def find_months_to_get_down_payment(portion_saved, annual_salary):
    monthly_savings = (annual_salary /12) * portion_saved
    current_savings = 0
    month = 0
    while current_savings < portion_down_payment:
        current_savings += monthly_savings + (current_savings*0.04)/12
        month += 1
        if month % 6 == 0:
            annual_salary += annual_salary*semi_annual_raise
            monthly_savings = (annual_salary /12) * portion_saved
    return month, current_savings-portion_down_payment

low = 0
high = 10000
savings_guess = 5000
month, epsilon = find_months_to_get_down_payment(savings_guess/10000, annual_salary)
steps = 1
epsilon = 0
if month == 36:
    print('Best savings rate: ' + savings_guess/10000)
    print('Steps in bisection search: ' + str(steps))
else:
    while month != 36 or epsilon > 100:
        prev_guess = savings_guess
        steps += 1
        if savings_guess >= 9999:
            print('it is not possible to save for the down payment in three years')
            sys.exit()
        if month <= 36:
            high = savings_guess
        else:
            low = savings_guess
        savings_guess = (high + low) // 2
        month, epsilon = find_months_to_get_down_payment(savings_guess/10000, annual_salary)

#aim for 36 months
print('Best savings rate: '+ str(savings_guess/10000))
print('steps in bisection search: ' + str(steps) )


