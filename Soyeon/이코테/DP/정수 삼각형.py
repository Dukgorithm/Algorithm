N = int(input())

triangle = [ [0]*N for _ in range(N) ]

for i in range(N):
    line = list(map(int, input().split()))
    triangle[i][:len(line)] = line

    if i>0:
        for n in range(N):
            nums = []
            if n-1>=0:
                nums.append(triangle[i-1][n-1])
            nums.append(triangle[i-1][n])
            triangle[i][n] += max(nums)

print(max(triangle[N-1]))
