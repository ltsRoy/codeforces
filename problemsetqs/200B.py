n=int(input())
s=0

f = input().split()
f = [int(x) for x in f]
s+=sum(f)
print(s/n)

