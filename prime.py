upper=int(input("Enter the upper limit:"))
lower=int(input("Enter the lower limit:"))
print("Prime number between",lower,"and",upper,"are:")
for i in range(lower,upper+1):
   f=0
   j=2
while(j<=(1/2)):
    if((i%j)==0):
     break
     j=j+1
     if(f==0):
 print(i)
