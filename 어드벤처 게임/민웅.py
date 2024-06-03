# 2310_어드벤처게임_Adventure game
import sys
from collections import deque
input = sys.stdin.readline

while True:
    N = int(input())

    if N == 0:
        break

    bang = {}
    adjL = [[] for _ in range(N+1)]
    for i in range(1, N+1):
        b, *info = input().split()
        cost = int(info[0])
        bang[i] = [b, cost]

        for j in range(1, len(info)-1):
            adjL[i].append(int(info[j]))

    visited = [float('inf')]*(N+1)
    ans = "No"

    q = deque()
    q.append([1, 0])
    visited[1] = 0

    while q:
        idx, money = q.popleft()
        if idx == N:
            ans = "Yes"
            break

        for maze in adjL[idx]:
            m, c = bang[maze]
            if m == "L" and money < c:
                new_m = c
            elif m == "T":
                new_m = money - c
            else:
                new_m = money

            if new_m < 0:
                continue

            if visited[maze] == float('inf') or visited[maze] < new_m:
                visited[maze] = new_m
                q.append([maze, new_m])

    print(ans)