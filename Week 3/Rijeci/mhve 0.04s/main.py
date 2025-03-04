k = int(input())

nA,nB = 1,0

for _ in range(k):
    nA,nB = nB,nB + nA

print(nA,nB)
