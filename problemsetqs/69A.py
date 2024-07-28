import math
n=int(input())
x,y,z=0,0,0
for i in range(n):
    f = input().split()
    f = [int(x) for x in f]
    x+=f[0]
    y+=f[1]
    z+=f[2]

if x==y==z==0:
    print("YES")
else:
    print("NO")