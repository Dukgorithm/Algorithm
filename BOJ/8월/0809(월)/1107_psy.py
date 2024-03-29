# [gold-5] 1107 리모컨
# algorithm 구현, 시뮬레이션
# 메모리: 	 KB
# 시간:      ms

import sys
input = sys.stdin.readline

def check(num):
    num = list(str(num))
    for i in num:
        if i in nums: 
            return False
    return True

n = int(input())
m = int(input())
nums = list(input().strip())

result = abs(n - 100)
for i in range(1000001):
    if check(i): 
        result = min(result, len(str(i)) + abs(i - n))

print(result)
