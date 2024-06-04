import sys
input = sys.stdin.readline

def dfs(x, y):
    # # 갈 수 없는 경우: 벗어났거나, 이미 방문한 곳이거나, 건물이면 False
    # if x < 0 or x >= R or y < 0 or y >= C or visited[x][y] or arr[x][y] == 'x':
    #     return False
    
    # 마지막 열에 도달하면 True
    if y == C - 1:
        return True
    
    # 현재 위치 방문 표시
    visited[x][y] = 1
    
    # 오른쪽 위, 오른쪽, 오른쪽 아래로 이동
    for dir in [-1, 0, 1]:
        if 0 <= x + dir < R and 0 <= y+1 < C and not visited[x+dir][y+1] and arr[x+dir][y+1] != 'x':
            if dfs(x + dir, y + 1):
                return True
    return False

R, C = map(int, input().split())
arr = [input().strip() for _ in range(R)]
visited = [[0] * C for _ in range(R)]

cnt = 0
for i in range(R):
    if dfs(i, 0):
        cnt += 1

print(cnt)
