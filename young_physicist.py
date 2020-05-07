n=input()
row=int(n)
col=3
total=0
arr=[[0 for i in range(col)] for j in range(row)]
#print(arr)
for i in range(row):
    for j in range(col):
        arr[i][j]=input()
#print(arr)
for i in range(3):
    for j in range(row):
        total=total+int(arr[j][i])
#print(total)
if total==0:
    print("YES")
else:
    print("NO")
