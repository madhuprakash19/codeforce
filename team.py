n=int(input())
a=[]
count=0
for i in range(0,n):
    b1=int(input())
    b2=int(input())
    b3=int(input())
    sum=b1+b2+b3
    a.append(sum)
for i in range(0,n):
    if a[i]>1:
        count=count+1
print(count)
    
