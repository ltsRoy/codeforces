import math
n=int(input())
for i in range(n):
    # f = input().split().sort() # wrong
    f = input().split()
    f = [int(x) for x in f]
   # f = list(map(int, f))
    f.sort()
    for i in range(5):
        f[0]+=1
        f.sort()
    print(math.prod(f))
