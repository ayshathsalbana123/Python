class bank_ac:
	def __init__(self):
		self.balance=0
	def deposit(self):
		amount=int(input("enter amount to be deposited:"))
		self.balance+=amount
		print("your current balance  is",self.balance)
	def withdraw(self):
		amount=int(input("enter amount to be withdrawn:"))
		if amount>self.balance:
			print("Insufficient Balance \n Please check your bank balance")
		else:
			self.balance-=amount
			print(amount,"is withdrawn")
	def display(self):
		print("balance amount is",self.balance)

myaccount=bank_ac()
myaccount.deposit()
myaccount.withdraw()
myaccount.display()
