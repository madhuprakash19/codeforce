n=int(input())
k=int(input())
a = []
count=0
for i in range(0,n):
    new=int(input())
    a.append(new)
for i in range(0,n):
    if a[i]>k:
        count = count + 1
    else:
        break
print(count)    
    
    

