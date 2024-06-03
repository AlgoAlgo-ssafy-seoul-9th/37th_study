# 3109 빵집
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
ground = tuple(input().strip() for _ in range(R))


def makePipeLine(row):
    stack = [(row,0)] # i, j, cnt

    while stack:
        i, j = stack.pop()
        visited[i][j] = 1
        if j == C-1:
            return 1
        

        for di in range(1, -2, -1):
            ni,nj = i+di, j+1
            if 0 <=ni < R and nj < C:
                if ground[ni][nj] != 'x' and not visited[ni][nj]:
                    stack.append((ni,nj))
    
    return 0

ans = 0
visited = [[0] * C for _ in range(R)]

for i in range(R):
    maxv = 0
    if ground[i][0] != "x":
        visited[i][0] = 1
        ans += makePipeLine(i)
# [print(visited[k]) for k in range(R)]
print(ans)     



'''
# 방향 배열
direction = [(-1,-1), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 1)]

R, C = map(int, input().split())
ground = tuple(tuple(input().strip()) for _ in range(R))

stack = []       # startj, i, j, cnt, visited_set

for i in range(C-1, -1, -1):
    if ground[0][i] != "x":
        stack.append((i, 0, i, 0, set([i])))

maxv = 0

while stack:
    startj, i, j, cnt, visited_set = stack.pop()
    print(i,j)
    if i == R-1:
        stack.append((startj+1, 0, startj+1, cnt+1, visited_set))
        continue

    if (i, j) == (0, C): 
        maxv = max(cnt+1, maxv)
        tmp = [[0]*C for _ in range(R)]
        for t in tuple(visited_set):
            tmp[t//C][t%C] = 1
        [print(tmp[u]) for u in range(R)]
        print()
        continue 

    if cnt < maxv:
        continue

    if ground[i][j] == 'x':
        continue

    for di, dj in direction:
        ni, nj = i+di, j+dj
        if (i, di) == (0, 0):
            continue
        
        if 0 <= ni < R and 0 <= nj < C:
            if ground[ni][nj] == '.' and (ni*C+nj) not in visited_set and ni > 0:
                if abs(ni) == abs(nj):
                    if ni*C+j not in visited_set and i*C+nj not in visited_set:
                        stack.append((startj, ni, nj, cnt, visited_set.union({ni*C+nj,})))
                else:
                    stack.append((startj, ni, nj, cnt, visited_set.union({ni*C+nj,})))
print(maxv)
'''