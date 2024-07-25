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