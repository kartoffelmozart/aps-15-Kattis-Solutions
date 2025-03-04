nT = int(input())

for t in range(1,nT+1):
    input()
    A = sorted(map(int,input().split()))
    B = sorted(map(int,input().split()),reverse=True)
    print(f'Case #{t}: {sum([a*b for a,b in zip(A,B)])}')