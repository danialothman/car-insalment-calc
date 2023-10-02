"""
monthly instalment calculator

source example: https://www.happy-motoring.com/v3/v3_city/#Gallery

item - units - source
---------------------
"price on the road" ($) [shop]
"down payment" ($) [user]
"loan amount" ($) [app]
"interest rate" (%) [app] (given 4.25%)
"financing period" (years) [user]
"monthly installment" ($/month) [app]

formulas
--------
"loan amount" = "price on the road" - "down payment"

"monthly instalment" = ("loan amount" * (1 + 4.25)) / (12 * "Financing Period") 


"""
import math

price_on_the_road = 27990
down_payment = 20000
loan_amount = price_on_the_road - down_payment
print("loan amount: " + str(loan_amount))
interest_rate = 4.25
financing_period = 2

interest = (interest_rate / 100) * financing_period * loan_amount
print("interest: " + str(interest))

monthly_instalment = math.ceil((loan_amount + interest) / (12 * financing_period))

print("monthly instalment: " + str(monthly_instalment))
