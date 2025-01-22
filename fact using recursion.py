def fact(n):
    if (n==0):
    	return  1
    elif(n>0):
    	result=n*fact(n-1)
    	return result
    else:
    	print("enter a valid number")
num=int(input("enter a number:"))
print (fact(num))
