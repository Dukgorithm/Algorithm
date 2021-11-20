def solution(N):
    index_one = []
    bin_str = str(bin(N))[2:]
    max_gap = 0
    
    for i in range(len(bin_str)):
        if bin_str[i]=='1':
            index_one.append(i)

    for i in range(len(index_one)-1):
        if index_one[i+1]-index_one[i]-1>max_gap:
            max_gap = index_one[i+1]-index_one[i]-1

    return max_gap


print(solution(1041)) #5
print(solution(15)) #0
print(solution(32)) #0