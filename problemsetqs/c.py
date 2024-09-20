w=int(input())
for i in range(w):
    n = int(input())
    s = input()
    s = s.split()
    x=int(s[0])
    y=int(s[1])
    b=0
    sec=0
    while(n>0):
        b=b+y
        b=b-x
        n=n-x
        sec=sec+1
    print(sec)
        
        