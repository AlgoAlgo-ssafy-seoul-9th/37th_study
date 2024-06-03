import sys
input = sys.stdin.readline

def dfs(nowin, money):
    type, val, next_rooms = rooms[nowin]
    
    if type == 'L':
        money = max(money, val)
    
    elif type == 'T':
        if money < val:
            return False
        money -= val

    if nowin == N:
        return True
    
    for next in next_rooms:
        if not visited[next]:
            visited[next] = 1
            if dfs(next, money):
                return True
            visited[next] = 0
    
    return False   

while True:
    N = int(input())
    if N == 0:
        break
    rooms = {}
    for i in range(1, N + 1):
        data = input().split()
        type = data[0]
        val = int(data[1])
        next = list(map(int, data[2:-1]))
        rooms[i] = (type, val, next)

    visited = [0] * (N + 1)
    visited[1] = 1
    
    if dfs(1, 0):
        print("Yes")
    else:
        print("No")
