a=int(input("eneter number:"))
sum=0
no=a
while(a!=0):
    sum=sum+a%10
    a=a//10
    print("sum of digit of{} is {}".format(a,sum))
