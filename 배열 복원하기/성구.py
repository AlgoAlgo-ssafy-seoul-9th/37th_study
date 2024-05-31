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