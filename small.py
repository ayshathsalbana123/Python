n=int(input("enter the number of elements in array:"))
lst=[]
for i in range(0,n):
    lst.append(int(input(f"enter element {i+1}:")))
lst.sort()
print(f"smallest:{lst[0]},second largest:{lst[n-2]},largest:{lst[n-1]}")
print("\n sorted list::\n",lst)

