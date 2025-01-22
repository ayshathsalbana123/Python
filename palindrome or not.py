def is_palindrome(n):
	n_str=str(n)
	n_rev=n_str[::-1]
	if (n_str==n_rev):
		return True
	else:
		return False
num=str(input("enter a number"))
if(is_palindrome(num)==True):
   print("number,is a palindrome")
else:
   print("number,is not a palindrome")
