n=int(input("enter the number of prime number to find:"))
count=0
a=2

while True:
	flag=0
	for i in range(2,a//2+1):
	    if a%i==0:
		    flag=1
		    break
	if flag==0:
		print(a)
		count=count+1
	if count==n:
		break
	a=a+1
