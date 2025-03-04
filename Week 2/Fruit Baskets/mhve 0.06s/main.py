class Solver:
    def __init__(self , n , all_fruits):
        self.n = n
        self.total = sum([all_fruits[i]*2**(n-1) for i in range(n)])
        self.all_fruits = sorted(all_fruits,reverse=True)
        self.solve()

    def solve(self, weight = 0 , depth = 0):
        if weight >= 200: return 
        if depth >= self.n: 
            self.total -= weight
            return
        self.solve(weight , depth+1)
        weight += self.all_fruits[depth]
        self.solve(weight , depth+1)

if __name__ == '__main__':
    n = int(input())
    all_fruits = list(map(int,input().split()))

    print(Solver(n,all_fruits).total)