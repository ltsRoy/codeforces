
w=int(input())
for i in range(w):
    n = int(input())
    s=input()
    x=s.rindex('B')-s.index('B')+1
    if x>0:
        print(x)
    else:
        print("0")
  