# 3109_빵집_bakery
import sys
input = sys.stdin.readline
dxy = [(-1, 1), (0, 1), (1, 1)]


def pipe_line(row, c, v):
    global cnt

    if c == C-1:
        return True

    for d in dxy:
        nr = row + d[0]
        nc = c + d[1]
        if 0 <= nr <= R-1 and 0 <= nc <= C-1:
            if bakery[nr][nc] == "." and not v[nr][nc]:
                v[nr][nc] = 1
                if pipe_line(nr, nc, v):
                    return True
    else:
        return False


R, C = map(int, input().split())

bakery = [list(input().strip()) for _ in range(R)]

visited = [[0]*C for _ in range(R)]
cnt = 0

for r in range(R):
    if bakery[r][0] == ".":
        visited[r][0] = 1
        if pipe_line(r, 0, visited):
            cnt += 1

print(cnt)