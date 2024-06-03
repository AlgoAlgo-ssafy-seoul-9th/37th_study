# 37th_study

알고리즘 스터디 37주차

<br/>

# 이번주 스터디 문제

<details markdown="1" open>
<summary>접기/펼치기</summary>

<br/>

## [배열 복원하기](https://www.acmicpc.net/problem/16967)

### [민웅](./배열%20복원하기/민웅.py)

```py
# 16967_배월 복원하기_restoring an array
import sys
input = sys.stdin.readline

H, W, X, Y = map(int, input().split())

original = [list(map(int, input().split())) for _ in range(H+X)]

for i in range(X, H+X):
    for j in range(Y, W+Y):
        if X <= i <= H+X-1 and Y <= j <= W+Y-1:
            original[i][j] = original[i][j] - original[i-X][j-Y]


for i in range(H):
    tmp = original[i][:W]
    print(*tmp)

```

### [상미](./배열%20복원하기/상미.py)

```py
import sys
input = sys.stdin.readline

H, W, X, Y = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(H+X)]

A = [[0] * W for _ in range(H)]

for i in range(H):
    for j in range(W):
        A[i][j] = arr[i][j]
# print(A)
for i in range(X, H):
    for j in range(Y, W):
        A[i][j] -= A[i-X][j-Y]

for row in A:
    print(*row)
```

### [성구](./배열%20복원하기/성구.py)

```py
# 16967 배열 복원하기
import sys
input = sys.stdin.readline


def main():
    # 입력
    H, W, X, Y = map(int, input().split())
    B = tuple(tuple(map(int, input().split())) for _ in range(H+X))
    A = [[0] * W for _ in range(H)]

    # 탐색
    for i in range(H):
        for j in range(W):
            # 저장
            A[i][j] += B[i][j]
            # 이전에 더해진 값만 빼줌
            if 0 <= i-X < H and 0 <= j-Y < W:
                A[i][j] -= A[i-X][j-Y]
        # 완성된 배열은 출력해도 됨
        print(*A[i])

    return


if __name__ == "__main__":
    main()
```

### [영준](./배열%20복원하기/영준.py)

```py

```

<br/>

## [빵집](https://www.acmicpc.net/problem/3109)

### [민웅](./빵집/민웅.py)

```py
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
```

### [상미](./빵집/상미.py)

```py

```

### [성구](./빵집/성구.py)

```py
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


```

### [영준](./빵집/영준.py)

```py

```

<br/>

## [어드벤처 게임](https://www.acmicpc.net/problem/2310)

### [민웅](./어드벤처%20게임/민웅.py)

```py
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
```

### [상미](./어드벤처%20게임/상미.py)

```py

```

### [성구](./어드벤처%20게임/성구.py)

```py
# 2310 어드벤처 게임
import sys
input = sys.stdin.readline


def bt(room, cost, N, doors, indoor, costs):
    if room == N:
        if indoor[room] == "T":
            if cost < costs[room]:
                return 0
        return 1

    if indoor[room] == "L":
        if cost < costs[room]:
            cost = costs[room]

    elif indoor[room] == "T":
        if cost < costs[room]:
            return 0
        cost -= costs[room]


    for door in tuple(doors[room]):
        if visited[door] == 0:
            visited[door] = 1
            if bt(door, cost, N, doors, indoor, costs):
                return 1
            visited[door] = 0
    return 0


visited = []

while True:
    N = int(input())
    if not N:
        break
    doors = [set() for _ in range(N+1)]
    indoor = [''] * (N+1)
    costs = [0] * (N+1)
    doors[0].add(1)
    for idx in range(1, N+1):
        id, cost, *door = input().split()
        indoor[idx] = id
        costs[idx] = int(cost)
        for d in door[:-1]:
            doors[idx].add(int(d))
    visited.clear()
    for _ in range(N+1):
        visited.append(0)

    if bt(0, 0, N, doors, indoor, costs):
        print("Yes")
    else:
        print("No")
```

### [영준](./어드벤처%20게임/영준.py)

```py

```

<br/>

</details>

<br/><br/>

# 지난주 스터디 문제

<details markdown="1">
<summary>접기/펼치기</summary>

<br/>

## [선수과목](https://www.acmicpc.net/problem/14567)

### [민웅](./선수과목/민웅.py)

```py
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
```

### [상미](./선수과목/상미.py)

```py

```

### [성구](./선수과목/성구.py)

```py
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
```

### [영준](./선수과목/영준.py)

```py

```

</details>

<br/><br/>

# 알고리즘 설명

<details markdown="1">
<summary>접기/펼치기</summary>

</details>
