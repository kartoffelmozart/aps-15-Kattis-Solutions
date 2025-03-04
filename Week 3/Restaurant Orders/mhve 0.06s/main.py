def getInput():
    n = int(input())
    C = list(map(int,input().split()))
    m = int(input())
    S = list(map(int,input().split()))
    return C,S

class Solver:
    def __init__(self,C,S):
        self.C = C
        self.S = S
        self.findDP()
        for s in self.S:
            print(self.findSolution(s))

    def findSolution(self,s):
        solution = []
        if self.dp[s] in ('Impossible','Ambiguous'):
            return self.dp[s]
        while s:
            k = self.dp[s]
            solution.append(k+1)
            s -= self.C[k]
        return ' '.join(map(str,solution))    
                
    def findDP(self):
        self.dp = [len(self.C)]*(max(self.S)+1)
        for s in range(1,max(self.S)+1):
            valid_c_found = False
            for k,c in enumerate(self.C):
                new_s = s - c
                if new_s >= 0:
                    if self.dp[new_s] == 'Ambiguous':
                        self.dp[s] = 'Ambiguous'
                        break
                    elif valid_c_found:
                        if isinstance(self.dp[new_s] , int) and k <= self.dp[new_s]:
                            self.dp[s] = 'Ambiguous'
                            break
                    else:
                        if self.dp[new_s] == 'Impossible':
                            self.dp[s] = 'Impossible'
                        else:
                            valid_c_found = True
                            self.dp[s] = k
                else:
                    if not valid_c_found:
                        self.dp[s] = 'Impossible'



if __name__ == '__main__':
    Solver(*getInput())