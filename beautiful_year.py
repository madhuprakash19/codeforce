y=input()
y=int(y)+1
#b=[int(x) for x in str(y)]
#print(y)
#print(b)
madhu=1
while(madhu):
    flag=0
    x=0
    b=[int(x) for x in str(y)]
    #print(b)
    for i in range(0,4):
        for i1 in range(0,4):
            if i != i1:
                if b[i] == b[i1]:
                    flag=1
                   
    if(not flag):
        madhu=0
        #print(y)
    else:
        y=int(y)+1
                    
                    
                    
               

print(y)
#print(b)
    

               
                
