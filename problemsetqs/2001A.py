w=int(input())


for i in range(w):
    n = int(input())
    s = input()
    s = s.split()
    tf=1
    for l in s:
        if s.count(l)>tf:
            tf=s.count(l)
    
    print(n-tf)
        
        