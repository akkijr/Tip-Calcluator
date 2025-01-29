#tip calculator

print("welcome to Tip Calculator!")

amount = float(input("What was the total amount of your bill? \n"))

tip = int(input("what percentage tip would you like to give?\n"))

people = int(input("how many people are splitting the bill togeather? \n"))

tip_amount = amount * (round(tip / 100 ,2 ))
total_amount = amount + tip_amount
print("total_amount")

print(f"each person has to pay {total_amount / people}") 

