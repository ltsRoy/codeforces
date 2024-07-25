w=int(input())
for i in range(w):
    a,b = input().split()   
    n,k=int(a),int(b)
    g,s=0,1
    while (g<n-1):
        s=s+k
        g=g+1
    else:
        print(s)
