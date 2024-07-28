import math
n=int(input())
for i in range(n):
    no=int(input())
    # f = input().split().sort() # wrong
    f = input().split()
    f = [int(x) for x in f]
   # f = list(map(int, f))
    s=0
    for i in range(len(f)-1):
        if f[i+1]<f[i] and f[i+2]>f[i]:
            s+=(f[i]-f[i+1])
    
    print(s)



