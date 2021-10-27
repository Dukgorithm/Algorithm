# [silver-3] 14501 퇴사
# algorithm  DP
# 메모리:    29200 KB
# 시간:      76 ms

N = int(input())
value = [0 for _ in range(21)]
T, P = [0], [0]

for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

for i in range(1, N+1):
    value[i+T[i]] = max(value[i+T[i]], value[i]+P[i])

for i in range(2, len(value)):
    value[i] = max(value[:i+1])

print(value[N+1])