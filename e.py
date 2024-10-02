def solve():
    x,y,z = map(int,input().split())
    sum = x + y + z
    minnumber = min(x,y,z)
    sum -= minnumber
    if sum >= 10:
        print("YES")
    else:
        print("NO")


t = int(input())
for _ in range (t):
    solve()