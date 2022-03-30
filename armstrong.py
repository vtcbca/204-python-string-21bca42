a=int(input("enter any number"))
sum=0
e=0
no=a
while(a!=0):
    b=a%10
    e=b*b*b
    sum=sum+e
    a=a//10
if(no==sum):
    print("it is armstrong number")
else:
    print("it is not armstrong numbet")
