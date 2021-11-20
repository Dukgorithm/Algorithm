def countingSort(arr):
    countDic = [0]*100
    
    for a in arr:
        countDic[a]+=1
    
    return countDic