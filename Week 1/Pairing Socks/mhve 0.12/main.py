# I could not tell you why I went for the whole void concept when just using two stacks would probably have been faster.

_,N = input(),list(map(int,input().split()))

class SockPairer:
    def __init__(self , N):
        self.N = N
        self.void_pointers = [None] * len(N)
        self.voids = []
        self.moves = 0
        self.solve()
        self.displayResult()

    def displayResult(self):
        if self.impossible(): print('impossible')
        else:                 print(self.moves)
    def solve(self):
        self.i = len(self.N) - 1
        self.j = self.i + 1
        while 1:
            if self.i < 0: break
            self.mainToAux()
            while N[self.i] == N[self.j]:
                self.removePair()
                if self.j >= len(self.N): break

    def mainToAux(self):
        self.i -= 1
        self.setJ()
        self.moves += 1

    def removePair(self):
        if self.j < len(self.N) - 1 \
        and self.void_pointers[self.j + 1] is not None:
            self.void_pointers[self.i] = self.void_pointers[self.j] = self.void_pointers[self.j + 1]
            self.voids[self.void_pointers[self.i]][0] = self.i
        elif self.void_pointers[self.i + 1] is not None:
            self.void_pointers[self.i] = self.void_pointers[self.j] = self.void_pointers[self.i + 1]
            self.voids[self.void_pointers[self.i]] = [self.i , self.j]
        else:
            self.void_pointers[self.i] = self.void_pointers[self.j] = len(self.voids)
            self.voids.append([self.i,self.j])
        self.moves += 1
        self.i -= 1
        self.setJ()

    def setJ(self):
        self.j = self.i + 1
        if self.void_pointers[self.j] is not None:
            self.j = self.voids[self.void_pointers[self.j]][1] + 1

    def impossible(self): return None in self.void_pointers

SockPairer(N)