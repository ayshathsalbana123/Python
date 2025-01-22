n=int(input("enter the size of the array:"))
lst=[]
for i in range(0,n):
    lst.append (int(input(f"enter the element {i+1}:")))
max=0
num=[]
for k in lst:
    if(k not in num):
        if(lst.count(k)>=max):
            max=lst.count(k)
            num.append(k)
print(f"{num}has the highest frequency of {max}")
