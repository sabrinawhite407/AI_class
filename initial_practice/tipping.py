# This line asks the user for the total cost of the meal before tax.
# input() lets the program read text typed by the user.
meal_total = float(input("Enter the total meal cost: "))

# This line asks the user for the tax rate as a percentage.
# We divide by 100 so the value becomes a decimal, such as 10 for 10% -> 0.10.
tax_rate = float(input("Enter the tax rate as a percentage: ")) / 100

# This line asks the user how many people are sharing the meal.
# int() changes the entered value into a whole number.
number_of_people = int(input("Enter the number of people: "))

# This line creates a list to store each person's chosen tip percentage.
# A list is a collection of values that we can loop through.
tip_percentages = []

# This line starts a loop that asks for each guest's tip percentage.
# range(number_of_people) creates a number sequence from 0 up to the number of guests minus 1.
for guest in range(number_of_people):
    # This line asks for one guest's tip percentage and stores it in the list.
    # The value is divided by 100 so it can be used in a percentage calculation.
    tip_percentages.append(float(input(f"Enter the tip percentage for guest {guest + 1}: ")) / 100)

# This line calculates the cost of each person's meal share.
# The total meal cost is divided evenly among all guests.
meal_share = meal_total / number_of_people

# This line calculates the tax for one person's portion of the meal.
# tax_rate is a decimal, so multiplying gives the correct tax amount for that share.
tax_share = meal_share * tax_rate

# This line starts a loop so each guest can be calculated one at a time.
# The loop goes through each tip percentage in the list.
for guest_number, tip_percentage in enumerate(tip_percentages, start=1):
    # This line calculates the tip amount for this guest based on their meal share.
    # The tip percentage is a decimal, so multiplying gives the correct tip amount.
    tip_amount = meal_share * tip_percentage

    # This line adds the meal, tax, and tip together for this guest.
    # The total must include all three parts of the cost.
    total_for_guest = meal_share + tax_share + tip_amount

    # This line prints the amount owed by this guest.
    # :.2f keeps the number to two decimal places, like money.
    print(f"Guest {guest_number} pays ${total_for_guest:.2f}")
