Student={}
n=int(input("enter the number of students:"))

for i in range(n):
	name=input("NAME:")
	age=int(input("AGE:"))
	grade=input("GRADE:")
	Student[name]=age,grade
print (Student)

l=list(Student.items())
l.sort()
print("sorted items in ascending order",l)
l.sort(reverse=True)
print("sorted items in decending order",l)
dict=dict(l)
