# Samuel Rose
# Road Trip Planner
# Create a Python program that estimates the cost of a road trip. 
# Your program will ask the user for trip information, 
# perform calculations, and display a personalized trip-cost summary.

# Header
print("==========================")
print("Road Trip Planner")
print("==========================")

# Collect Trip Information
name = input("Enter your name: ")
destination = input("Where is your Destination? ")

# Numbers or data inputs
distance = int(input("How many miles is a one-way trip? "))
miles_per_gallon = float(input("What is your vehicle's average miles per gallon? "))
gas_price = float(input("What is the estimated price per gallon? "))
traveler_count = int(input("How many travelers will be going? "))

# Calculate the trip Details from the inputs
total_miles = distance * 2
gallons_needed = total_miles / miles_per_gallon
gas_cost = gallons_needed *gas_price
cost_per_traveler = gas_cost / traveler_count

# Display a trip summary
# Header
print("==========================")
print("Road Trip Planner")
print("==========================")
# Trip Info
print("Name: " + name)
print("Destination: " + destination)
print("Gallons of Gas Needed: " + str(gallons_needed))
print("Total Estimated Cost of Gas: " + str(gas_cost))
print("Cost per Traveler: " + str(cost_per_traveler))
