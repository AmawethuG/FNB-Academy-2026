#The South African Fuel Cost Calculator

Kilometers = float(input("Enter the distance you will travel in kilometers: "))
Price_per_liter = float(input("Enter the price of fuel per liter in Rands: "))
liters_needed = Kilometers / 10
Total_cost = liters_needed * Price_per_liter
print(f"The total cost of fuel for your trip is: R{Total_cost:.2f}")