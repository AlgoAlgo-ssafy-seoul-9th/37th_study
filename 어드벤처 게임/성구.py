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