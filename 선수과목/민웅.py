# 14567_선수과목_Prerequisite
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

adjL = [[] for _ in range(N+1)]
indegree = [0]*(N+1)

for i in range(M):
    a, b = map(int, input().split())
    adjL[a].append(b)
    indegree[b] += 1

q = deque()

for i in range(1, N+1):
    if not indegree[i]:
        q.append([i, 1])

ans = [0]*(N+1)

while q:
    now, cnt = q.popleft()
    ans[now] = cnt

    for node in adjL[now]:
        indegree[node] -= 1
        if not indegree[node]:
            q.append([node, cnt+1])
ans = ans[1:]
print(*ans)