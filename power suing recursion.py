def power(exp,base):
	if exp==0:
		return 1
	elif exp==1:
		return base
	
	else:
		result=base*power(exp-1,base)
	return result
		
base=int(input("enter the base value:"))		
exp=int(input("enter the exponential value:"))
print (power(exp,base))
