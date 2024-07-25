"""n=int(input())
for i in range(n):
    f = input().split()
    a = input().split()
    if (f[1]) in a:
        print("YES")
    else:
        print("NO")"""
    
print('\n'.join("YES" if input().split()[1] in input().split() else "NO" for _ in range(int(input()))))

"""print("YES" if input().split()[1] in input().split() else "NO" for i in range(int(input())))
 WRONG """
    """
    b=False
    if y>=-1:
        b=True  
    if b==True:
        print("YES")
    else:
        print("NO")"""