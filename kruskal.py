import functools

class mst(object):
    def __init__(self, G, V):
        self.G = G
        self.V = V
        self.A = len(G)
        self.root = [x for x in range(0, self.V+1)]
        self.size = [1 for x in range(0, self.V+1)]
        self.arv = self.Kruskal()
        self.qcomps = self.quantComponentes() #quantidade de componentes
        self.peso = sum([x[2] for x in self.arv])
    def U(self, x, y):
        if self.size[x] < self.size[y]:
            self.root[x] = y
            self.size[y] += self.size[x]
        else:
            self.root[y] = x
            self.size[x] += self.size[y]
    def F(self, x):
        while x != self.root[x]:
            x = self.root[x]
        return x
    def Kruskal(self):
        def comp(x, y):
            return x[2] - y[2]
        g = sorted(self.G, key=functools.cmp_to_key(comp))
        arvore = []
        for e in g:
            r1, r2 = self.F(e[0]), self.F(e[1])
            if r2 == r1: continue
            self.U(r1, r2)
            arvore.append(e)
        return arvore
    def quantComponentes(self):
        self.verif = [0 for x in range(0, self.V+1)]
        self.sets = [[] for x in range(0, self.V+1)]
        count = 0
        for i in range(1, self.V+1):
            r = self.F(self.root[i])
            if self.verif[r] == 0:
                self.sets[r].append(i)
                self.verif[r] = self.size[r]
                count+=1
            else: self.sets[r].append(i)
        return count
