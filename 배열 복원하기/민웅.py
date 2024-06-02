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
