import sys
input = sys.stdin.readline

N, M = map(int, input().split())
sub = [[] for _ in range(N+1)]
ans = [i for i in range(N+1)]
for _ in range(M):
    fir, num = map(int, input().split())
    sub[num].append(fir)

for i in range(1, N+1):
    if not sub[i]:
        ans[i] = 1
    while True:
        for mansub in sub[i]:
            
print(*ans)