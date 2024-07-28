
n=int(input())

for i in range(n):
    short=""
    f = input()
    if len(f)>10:
        short=f[0]+str(len(f)-2)+f[-1]
        print(short)
    else:
        print(f)
