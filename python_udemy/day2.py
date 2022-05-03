# print("hello"[4])
#tip calculator

print("welcome to tip calculator")

total_bill=float(input("what was the total bill"))

select_percent=int(input("what percentage of tip would you like to give? 10,12 or 15"))

percent=select_percent/100

total_bill+=percent



splitt=int(input("how many people to split the bill?"))

print("each person should pay :")
amt=total_bill/splitt
print(round(amt,2))
