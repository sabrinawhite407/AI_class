# Importing the math module allows the ceil() function to be used.
# The math module is a Python library with extra math tools.
# ceil() means "round upward".
# This is useful when we cannot buy part of a bottle, so we need to round up to a full bottle.
import math

# A bottle_cost variable stores the price of one 1L bottle of drink.
# The = sign assigns the value on the right to the name on the left.
bottle_cost = 50

# A tonic_pack_cost variable stores the price of one pack of tonic cans.
# The value is the cost of a whole pack, not one single can.
tonic_pack_cost = 10

# A cans_per_pack variable stores how many cans are in one pack.
# This is a whole number because a pack contains a fixed number of cans.
cans_per_pack = 12

# The drinks_per_bottle variable stores how many drinks can be made from one bottle.
# The value is an integer, which means it is a whole number.
drinks_per_bottle = 10

# The drinks_per_person variable stores how many drinks each guest will have.
# A variable can hold numbers so the value can be reused in calculations.
drinks_per_person = 2

# The guest_count variable stores how many guests are attending the party.
# The variable name clearly describes the data it holds.
guest_count = 20

# The total_drinks_needed variable calculates how many drinks are needed for everyone.
# The * operator multiplies the number of guests by the number of drinks each person gets.
total_drinks_needed = guest_count * drinks_per_person

# The raw_bottles_needed variable finds how many bottles are needed for the total drinks.
# The / operator divides one number by another, so this gives a decimal value.
raw_bottles_needed = total_drinks_needed / drinks_per_bottle

# The bottles_needed variable rounds the bottle count up to the next whole number.
# math.ceil(raw_bottles_needed) checks the decimal result and moves it up to the nearest whole bottle.
# For example, 4.2 becomes 5, because we cannot buy 4.2 bottles in real life.
bottles_needed = math.ceil(raw_bottles_needed)

# The drink_cost variable calculates the cost of all the bottles needed.
# The * operator multiplies the number of bottles by the price per bottle.
drink_cost = bottles_needed * bottle_cost

# The tonic_cans_needed variable calculates how many tonic cans are needed.
# Each drink uses one can, so the total number of drinks equals the number of cans needed.
tonic_cans_needed = total_drinks_needed

# The tonic_packs_needed variable figures out how many 12-packs are needed.
# The / operator divides the cans needed by the number of cans in each pack.
# The ceil() function rounds upward so we buy enough full packs.
tonic_packs_needed = math.ceil(tonic_cans_needed / cans_per_pack)

# The mixer_cost variable calculates the total cost of the tonic packs needed.
# The * operator multiplies the number of packs by the price of one pack.
mixer_cost = tonic_packs_needed * tonic_pack_cost

# The total_cost variable adds the mixer cost to the drink cost.
# The + operator combines both expenses into one total.
total_cost = drink_cost + mixer_cost

# The final print() statement displays the answer for the user.
# Commas separate multiple values in print(), and Python adds spaces between them.
print("The total cost for the party drinks and mixers is $", total_cost)

