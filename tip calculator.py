print("Welcome to the tip calculator")
total = float(input("What was the total bill?$"))
percentage = int(input("What percentage tip would you like to give ?10,12, or 15?"))
members = int(input("How many people to split the bill?"))
result = percentage/100
total_amt=result*total
final=total_amt+total
print(final)