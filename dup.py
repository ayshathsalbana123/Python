n=int(input("enter the number of elements in array:"))
lst=[]
for i in range(0,n):
    lst.append(int(input(f"enter the element {i+1}:")))
lst.reverse()
for i in lst:
    if(lst.count(i)>1):
        lst.remove(i)
print(lst)
