def findMedian(arr):
    # Write your code here
    return sorted(arr)[len(arr)//2]

print(findMedian([0, 1, 2, 4, 6, 5, 3]))