T = int(input())

result = []
for _ in range(T):
    N, M = map(int, input().split())
    nums=list(map(int, input().split()))
    mine=[]

    # M x N 그래프로 저장
    for n in range(N):
        mine.append(nums[n*M:n*M+M])
     
    for m in range(1, M):
        maxValue = 0
        for n in range(N):
            next = []
            if n-1>=0:
                next.append(mine[n-1][m-1])
            if n+1<N:
                next.append(mine[n+1][m-1])
            next.append(mine[n][m-1])
            
            mine[n][m] = max(next)+mine[n][m]
            
            # 열 마다 max 값 저장
            if maxValue < mine[n][m]:
                maxValue = mine[n][m]
    result.append(maxValue)

print(*result, sep='\n')