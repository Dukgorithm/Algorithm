from collections import deque

def solution(A, K):
    A = deque(A)
    A.rotate(K)
    return list(A)
