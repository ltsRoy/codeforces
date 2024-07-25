n=int(input())

for i in range(n):
    f = input().split()
    x = int(f[0])
    y = int(f[1])
    b=False
    if y>=-1:
        b=True  
    if b==True:
        print("YES")
    else:
        print("NO")
        
    """if abs(x)<abs(y)+1:
        x1=x
        y1=y
        print("YES")
    else:
        print("NO")
        
    elif y-y1<0:
    
    x1=0
    y1=0

    if abs(x-x1)<=2:
            x1=x
            y1=y
            
            """
    