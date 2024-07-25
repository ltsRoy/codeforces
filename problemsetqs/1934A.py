
w=int(input())
for i in range(w):
    n = int(input())  
    a = sorted(list(map(int, input().split())))
    ans = 2 * (a[n - 1] + a[n - 2] - a[1] - a[0])
    print(ans)