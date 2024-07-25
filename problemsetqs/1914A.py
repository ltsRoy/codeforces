import string
w=int(input())
for i in range(w):
    n = int(input())
    s=input()
    count=0
    for l in string.ascii_uppercase:
        sum=0
        for k in s:
            if k==l:
                sum+=1
        if sum>=(ord(l)-64):
            count+=1
    
    print(count)
  
    
"""
    for l in s:
        if ord(l)-64<=c:
            sum=sum+1
            c=c+1
    print(sum)
    """
    
