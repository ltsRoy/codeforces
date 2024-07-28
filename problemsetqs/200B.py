n=int(input())
sum=0
for i in range(n):
    a = input()
    if a.count('1')>=2:
        sum+=1

print(sum)