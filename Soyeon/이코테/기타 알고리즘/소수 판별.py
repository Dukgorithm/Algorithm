# 제곱근 대칭 아이디어 => O(N^1/2)
# def is_prime_number(x):
#     for i in range(2, int(pow(x, 1/2))+1):
#         if x % i == 0:
#             return False
#     return True

# 에라토스테네스의 체 => O(NloglogN)
n = 1000 # 2부터 1,000까지의 모든 수에 대하여 소수 판별
def is_prime_number(n):
    array = [True for i in range(n+1)] # 처음엔 모든 수가 소수(True)인 것으로 초기화(0, 1은 제외)

    # 에라토스테네스의 체 알고리즘
    for i in range(2, int(pow(n,1/2))+1): # 2부터 n의 제곱근까지의 모든 수를 확인하며
        if array[i] == True: # i가 소수인 경우(남은 수인 경우)
            # i를 제외한 i의 모든 배수를 지우기
            j=2
            while i*j <= n:
                array[i*j] = False
                j+= 1

    # 모든 소수 출력
    count =0
    for i in range (2, n+1):
        if array[i]:
            count+=1
            print(i, end='')