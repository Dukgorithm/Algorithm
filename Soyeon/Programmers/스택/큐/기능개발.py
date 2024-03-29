def solution(progresses, speeds):
    answer = []
    days = 0
    count = 0

    while len(progresses) != 0:
        if progresses[0] + days * speeds[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0 
            days += 1    
    

    answer.append(count)
    print(answer)
    return answer


# solution([93, 30, 55], [1, 30, 5]) # [2, 1]
# solution([93, 30, 55, 66], [1, 30, 5, 5]) # [2, 2]
# solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]) # [1, 3, 2]
