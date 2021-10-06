# [Weekly Chanllenge] 최소직사각형
# 획득 포인트 1

def solution(sizes):
    w, h = 0, 0
    
    for s in sizes:
        s.sort()
        if s[0] > w:
            w = s[0]
        if s[1] > h:
            h = s[1]
    
    return w*h