# [Weekly Chanllenge] 전력망을 둘로 나누기
# 획득 포인트 
minNum = 0
nodes = []

def dfs(i, minNum, n):
    if len(nodes[i]) < 1: # 리프 노드는 1을 리턴
        return 1
    else: 
        # 자식이 있다면 자손 노드의 갯수랑 (N-자손 노드의 갯수)의 차이가 min보다 작으면 min에 저장
        num = 0
        for node in nodes[n]:
            num += dfs(node, minNum, n)
            
        diffNum = abs((num+1)-(n-(num+1)))
        if diffNum<minNum:
            minNum = diffNum
        
        return num
        

def solution(n, wires):
    minNum = n
    maxIndex, size = 0, 0
    
    nodes = [[] for _ in range(n+1)]
    
    for w in wires:
        nodes[w[0]].append(w[1])
        nodes[w[1]].append(w[0])
    
    print("nodes", nodes)
    for i in range(len(nodes)):
        if size<len(nodes[i]):
            maxIndex = i
            size = len(nodes[i])
            
    return dfs(maxIndex, minNum, n)
    
    # dfs로 node들의 count의 차이를 최소로 만들기

solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]])  #	3
#solution(4,	[[1,2],[2,3],[3,4]])    #	0
#solution(7,	[[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]])  #	1