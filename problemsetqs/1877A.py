w=int(input())
for i in range(w):
    n=int(input())
    s=0
    z=input().split()
    for i in range(n-1):
        s=s+int(z[i])
    
    print(s*-1)
        