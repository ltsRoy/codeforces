w=int(input())
for i in range(w):
    a,b = input().split()
    n,k=int(a),int(b)
    g,s=0,1
    while (g<n):
        s=s+3
        g=g+1
    else:
        print(s)
 