# [silver-3] N과 M (1)
# algorithm  재귀
# 메모리:    29452 KB
# 시간:      248 ms
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
res = []

def dfs(L):
    if L == M:
        print(*res)
        return
    for i in range(1, N+1):
        if i not in res: # 뽑은 요소와 겹치지 않는다면
            res.append(i)
            dfs(L+1)
            res.pop()
dfs(0)
