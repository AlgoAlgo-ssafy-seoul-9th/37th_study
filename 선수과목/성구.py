# 14567 선수과목
import sys
from collections import deque
input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    # 연결 노드 개수 배열
    visited = [0] * (N+1)
    # 그래프
    prerequisite = [set() for _ in range(N+1)]

    # 입력
    for _ in range(M):
        A, B = map(int, input().split())
        prerequisite[A].add(B)
        visited[B] += 1
    
    # 최종 배열
    ans = [0] * N
    
    # bfs
    que = deque()
    for i in range(1, N+1):
        if not visited[i]:
            que.append((i, 1))
            ans[i-1] = 1
    
    while que:
        spot, deg = que.popleft()
        for node in tuple(prerequisite[spot]):
            # 연결 노드 제거
            visited[node] -= 1
            # 연결 노드가 모두 제거된 항목 탐색
            if not visited[node]:
                que.append((node, deg+1))
                ans[node-1] = deg+1

    print(*ans)
    return

if __name__ == "__main__":
    main()