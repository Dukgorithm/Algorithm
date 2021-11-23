# [9, 3, 9, 3, 9, 7, 9]
# 짝이 없는 수 리턴

from collections import defaultdict

def solution(A):
    dic = defaultdict(int)

    for a in A:
        dic[a]+=1
    
    for key, value in dic.items():
        if value%2==1:
            return key