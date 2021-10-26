N, M = map(int, input().split())
coin = []

for _ in range(N):
    c = int(input())
    if c<=M: 
        coin.append(c)
payment = [10001 for _ in range(M+1)]

for c in coin:
    payment[c]=1

for i in range(min(coin), M+1):
    for c in coin:
        payment[i] = min(payment[i-c]+1, payment[i])
if payment[M] == 10001:
    payment[M] = -1

print(payment[M])