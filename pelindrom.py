a=int(input("enter any number"))
b=a
rev=0
while(a>0):
    k=a%10
    rev=rev*10+k
    a=a//10
if(b
   ==rev):
    print("it is pelindrom number")
else:
    print("it is not pelindrom numbet")
