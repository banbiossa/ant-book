import numpy as np
class UnionFindTree():
    def __init__(self, n:int):
        ''' UnionFindTree implementation
        
        Parameters
        ----------
        n: max number of nodes
        '''
        self.n = n
        self.par = np.array(range(n))
        self.rank = np.zeros((n,), dtype = np.int8)
    
    def find(self, x: int):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]
    
    def unite(self, x: int, y:int):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
    
    def same(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)