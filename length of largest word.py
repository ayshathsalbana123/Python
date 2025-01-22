n=int(input("enter number of elemts in the list:"))
lst=[]
for i in range(1,n+1):
	element=str(input("enter an element:"))
	lst.append(element)
max=len(lst[0])
temp=lst[0]
for i in lst:
	if len(i)>max:
		temp=i
print (temp,"is the largest word")


