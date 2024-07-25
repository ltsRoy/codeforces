
"""n=int(input("Enter length of pass: "))
p=input("Enter pass: ")

for i in range(n-1):
    if p[i].isalpha():
        if p[i+1].isdigit():
            print("NO")
            break
        elif p[i].isalpha():
            if p[i+1]<p[i]:
                print("NO")
                break
    elif p[i].isdigit():
        if p[i+1].isalpha():
            print("NO")
            break   
        elif p[i+1]<p[i]:
            print("NO")
            break
else:
    print("YES")
    
"""
n=int(input())
for i in range(n):
	j = int(input())
	inp = input()
	print("YES" if list(inp) == sorted(inp) else "NO")
