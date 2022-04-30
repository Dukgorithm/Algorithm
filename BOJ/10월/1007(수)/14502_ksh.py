N, M = map(int, input().split())
data = []
temp = [[0] * M for _ in range(N)]
result = -1

for _ in range(N):
    data.append(list(map(int, input().split())))

dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def virus(x, y):
    for dx, dy in dir:
        new_x = x + dx
        new_y = y + dy

        if new_x >= 0 and new_x < N and new_y >= 0 and new_y < M:
            if temp[new_x][new_y] == 0:
                temp[new_x][new_y] = 2
                virus(new_x, new_y)

def get_score():
    count = 0
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 0:
                count += 1

    return count

def dfs(count):
    global result
    if count == 3:
        for i in range(N):
            for j in range(M):
                temp[i][j] = data[i][j]

        for i in range(N):
            for j in range(M):
                if temp[i][j] == 2:
                    virus(i, j)

        result = max(result, get_score())
        return

    for i in range(N):
        for j in range(M):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1

dfs(0)
print(result)




















