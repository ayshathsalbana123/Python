def fibo(n):
	if (n==0 or n==1):
		return n
	else:
		return fibo(n-1)+fibo(n-2) 
	
num=int(input("enter a number"))
if num<=0:
	print(" enter a positive number")
else:
	print("Fibanocci numbers are:")
	for i in range(0,num):
		print(fibo(i)) 
		            
