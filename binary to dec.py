binary=str(input("enter a binary number to convert to decimal "))
decimal=1
result=0
sum=0
for i in binary:
	sum=int(i)*decimal
	decimal=decimal*2
	result=result+sum
print("decimal number is:",result)
