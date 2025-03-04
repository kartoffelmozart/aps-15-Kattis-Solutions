def getInput():
    l,w,n,r = map(int,input().split())
    cranes = [tuple(map(int,input().split())) for _ in range(n)]
    return l,w,n,r,cranes

def dist(p1,p2):
    x1,y1 = p1
    x2,y2 = p2
    return ((x2-x1)**2 + (y2-y1)**2)**.5
   
class SolverPrunedCranesWithReaches: 
    def __init__(self , l , w , n , r , cranes):
        self.walls = ((-l/2,0) , (l/2,0) , (0,-w/2) , (0,w/2))
        self.r = r
        reaches = set()

        for crane in cranes:
            reach = []
            for wall in self.walls:
                if dist(crane,wall) <= r:
                    reach.append(wall)
            reaches.add(tuple(reach))
        reaches = sorted([set(reach) for reach in reaches],key=len)

        self.cranes = []
        for i in range(len(reaches)-1,-1,-1):
            include = True
            for reach in reaches[:i]:
                if reaches[i].issubset(reach):
                    include = False
                    break
            if include: self.cranes.append(reaches[i])
            
        self.n = len(self.cranes)             
        self.shortest_solution = list(range(self.n+1))
        self.calls = 0
        self.solve([],0)
        self.result = len(self.shortest_solution) if len(self.shortest_solution) <= self.n else 'Impossible'

    def solve(self , solution , index):
        if self.isValid(solution):
            if len(solution) < len(self.shortest_solution):
                self.shortest_solution = solution.copy()
            return
        elif index >= self.n:
            return
        self.solve(solution,index+1)
        solution.append(self.cranes[index])
        self.solve(solution,index+1)
        solution.pop()

    def isValid(self , solution):
        for wall in self.walls:
            wall_reached = False
            for reach in solution:
                if wall in reach:
                    wall_reached = True
                    break
            if not wall_reached: return False
        return True

if __name__ == '__main__':
    w,l,n,r,cranes = getInput()
    print(SolverPrunedCranesWithReaches(w,l,n,r,cranes).result)