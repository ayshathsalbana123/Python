n=int(input("enter no of students:"))
td=int(input("total no of classes:"))
student={}

for i in range(1,n+1):
	name=str(input("enter name of student:"))
	d=int(input("no of classes attended:"))
	percentage=((d/td)*100)
	student[name]=percentage
	
desc=sorted(student.items(),key=lambda x:x[1],reverse=True)
print(dict(desc))
