# [gold-5] 9663 N-Queen
# algorithm  백트래킹
# 메모리:    156068 KB
# 시간:      13912 ms

import sys
input = sys.stdin.readline

N = int(input())
count = 0
board = [0]*N
visited = [False]*N

def check(x): # 기존에 있는 퀸들과 대각선 방향 퀸 체크
    for i in range(x):
        if abs(board[x] - board[i]) == x-i:
            return False
    return True

def nQueen(x):
    global count
    if x == N: # 퀸을 끝까지 넣으면
        count+=1
        return
    
    for i in range(N):
        if visited[i]: # i열에 퀸이 있으면 continue
            continue

        board[x] = i
        if check(x):
            visited[i] = True
            nQueen(x+1)
            visited[i] = False
    
nQueen(0)
print(count)