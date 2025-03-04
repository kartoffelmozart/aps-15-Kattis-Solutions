T = int(input())
for t in range(T):
    input()
    N = int(input())
    participants = sorted([int(input().split()[1]) for _ in range(N)])
    total = 0
    for i,p in enumerate(participants,1):
        total += abs(p-i)
    print(total)