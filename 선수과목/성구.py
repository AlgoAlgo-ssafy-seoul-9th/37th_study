# 14567 선수과목
import sys
from collections import deque
input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    visited = [0] * (N+1)
    prerequisite = [set() for _ in range(N+1)]
    for _ in range(M):
        A, B = map(int, input().split())
        prerequisite[A].add(B)
        visited[B] += 1
    
    ans = [0] * N
    que = deque()
    for i in range(1, N+1):
        if not visited[i]:
            que.append((i, 1))
            ans[i-1] = 1
    
    while que:
        spot, deg = que.popleft()
        for node in tuple(prerequisite[spot]):
            visited[node] -= 1
            if not visited[node]:
                que.append((node, deg+1))
                ans[node-1] = deg+1

    print(*ans)
    return

if __name__ == "__main__":
    main()