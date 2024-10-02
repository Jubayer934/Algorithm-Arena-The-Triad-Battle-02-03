def solve():
    s = []

    for i in range(8):
        row = list(input().strip()) 
        s.append(row)

    for i in range(8):
        for j in range(8):
            if s[i][j] == '.':  
                continue
            print(s[i][j], end='')
    print()

t = int(input())
for _ in range(t):
    solve()
