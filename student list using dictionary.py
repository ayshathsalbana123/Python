Student={}
n=int(input("enter the number of students:"))

for i in range(n):
	name=input("NAME:")
	age=int(input("AGE:"))
	grade=input("GRADE:")
	Student[name]=age,grade
print (Student)

