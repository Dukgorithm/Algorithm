# [bronze-2] 2292 벌집
# algorithm  수학
# 메모리:    29200 KB
# 시간:      72 ms

import sys
input = sys.stdin.readline

N = int(input())
room=1

if N<2:
    print(1)
else:
    for i in range(1, N+1):
        room+=(6*(i-1))

        if N<=room:
            print(i)
            break

