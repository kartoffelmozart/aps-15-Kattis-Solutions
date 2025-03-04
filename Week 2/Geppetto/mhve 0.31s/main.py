# I believe this is simply our professor Martin's solution that I copied.

n,m = map(int,input().split())
M = [map(int,input().split()) for _ in range(m)]
class Solver:
    def __init__(self , n , M):
        self.forbidden_pairs = set()
        for a,b in M:
            self.forbidden_pairs.add((a, b) if a < b else (b, a))
        self.n_solutions = self.search1([], 1, n + 1)

    def search1(self, subset, k, n):
        if k == n:
            # is the given pizza valid?
            #print(subset, forbidden_pairs)
            for a, b in self.forbidden_pairs:
                if a in subset and b in subset:
                    return 0
            return 1
        else:
            solutions_without = self.search1(subset, k + 1, n) # do not take element k in the subset
            subset.append(k)
            solutions_with = self.search1(subset, k + 1, n) # take element k in the subset
            subset.pop()
            return solutions_without + solutions_with
print(Solver(n,M).n_solutions)