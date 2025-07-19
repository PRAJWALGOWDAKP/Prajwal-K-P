def series1(a):
    if a%2==0:
        a-=1
    for i in range(1,2*a,2):
        print(i,end=" ")
a=int(input("Enter the number:"))
res=series1(a)
