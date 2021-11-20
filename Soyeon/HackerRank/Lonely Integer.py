from collections import defaultdict

def lonelyinteger(a):
    dic = defaultdict(int)
    result = 101
    
    for num in a:
        dic[num]+=1
    for key, value in dic.items():
        if value == 1:
            return key