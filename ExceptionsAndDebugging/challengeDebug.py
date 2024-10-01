"""
Challenge 1 is to complete the terminal input for price
calculations for our OdemaxCiniVue customers.

The rules are:
Custom Exceptions/ Validation:
- Children under 3 years old are not permitted into the Cinema.
- No one can earn negative money a year.
Logic:
- Children aged 3 to 12 receive the Child Discount.
- Pensioners receive a special discount.
- If a user earns less than £12,500 a year, and is not a child
or a pensioner, they are entitled to a free ticket.

"""

##########################################
# CONSTANT VALUES FOR OdemaxCiniVue Cinema
# Prices are in pence...
PRICE_PER_TICKET = 1780
CHILD_DISCOUNT_PERCENTAGE = 50
PENSIONER_DISCOUNT_PERCENTAGE = 45
PENSIONER_AGE_CUTOFF = 65
##########################################

## Welcome Screen ########################
print("Welcome to the OdemaxCiniVue Cinema!")
print("Discounts are available at the moment...")
users_age = int(input("How old is the viewer?"))
users_wage = int(input("How much does the viewer earn a year?"))
##########################################

"""
👇   Finish the application  👇
"""

if users_wage < 12500 and users_age > 3:
    print("You are eligible for a free ticket!")
elif users_age >= 3 and users_age <= 12:
    print("You get 50% off!")
elif users_age >= 65:






