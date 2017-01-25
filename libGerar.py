# -*- coding: utf8 -*-
#---------------------------------------------------------
# O que isso faz:
#   Gera um Grafo aleatorio (random)
#   que por azar ou sorte pode ser desconexo.
#
# E nao eh soh isso:
#   Voce pode garantir que eh conexo,
#
#   Programador: jeovazero
#
#--------------------------------------------------------
from random import randint
from kruskal import mst
import functools

#--=--=--=-=-=--=-=-=--=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-
def p(J):
    for i in J:
        print(i)
    print("------------------")
class geradorGrafos(object):
    def __init__(self):
        self.querconexo = False
        self.idGrafos = 1
        self.countCnx = 0
        self.countDnx = 0
        self.completo = False
    def setCnx(self, T):
        self.querconexo = T
    def setCompleto(self, T):
        self.completo = T
    def cleanFile(self):
        open("ginput.txt", "w").write("")
        open("gresults.txt", "w").write("")
    def salvarEntradas(self, V, A, G):
        f = open("ginput.txt", "a")
        buff = "%d %d\n" % (V, A)
        f.write(buff)
        for i in G:
            buff = "%d %d %d\n" % (i[0], i[1], i[2])
            f.write(buff)
        f.write('\n')
        f.close()
        print("InputOK.")
    def salvarResultados(self, arv, dataG, id):
        f = open("gresults.txt", "a")
        buff = "[GRAFO %3d] Peso: %d\n%d arestas na arvore mínima:\n" % (id, dataG[1], len(arv))
        if dataG[0] > 1: buff += "GRAFO DESCONEXO! :(\n"
        f.write(buff)
        for i in arv:
            buff = "%d %d %d\n" % (i[0], i[1], i[2])
            f.write(buff)
        f.write('\n')
        f.close()
        print("ResultOK.")
#Atencao muita POG a seguir, estou avisando
#Elementos de Tuplas sao imutaveis
    def arestasRepetidas(self, G):
        h = []
        repetidos = []
        j = 0
        for i in G:
            a = min(i[0], i[1])
            b = max(i[0], i[1])
            h.append((a,b,i[2],j))
            j+=1
        def comp(x,y):
            for i in range(2):
                k = x[i]-y[i]
                if k != 0: return k
            return 0

        h = sorted(h, key=functools.cmp_to_key(comp))
        for i in range(0, len(h)-1):
            if h[i][0] == h[i+1][0] and h[i][1] == h[i+1][1]:
                repetidos.append(h[i][3])
        print("RepeatedAnalized.")
        return sorted(repetidos, reverse=True)
    def gerar(self, V):
        print("Init Generation.")
        A = (V*(V-1))/2
        G = []                    #G de Grafo
        if self.completo == True:
            print("%d_Arestas.."%A)
            for i in range(1, V+1):
                for j in range(i, V+1):
                    G.append((i, j, randint(1, V)))
            print("Grafo_Completo Gerado." )
            g = mst(G, V)
            self.salvarEntradas(V, A, G)
            G = [] #tirando a referencia, o coletor vai agir
            print("Passou pelo mst.")
            arvore = g.arv
            dataG = (g.qcomps, g.peso)
            g = [] #o coletor vai trabalhar
        else:
            A = randint(V-2, A-1)  #A de Arestas
            print("%d_Arestas.."%A)
            for i in range(0, A):
                v1 = v2 = randint(1, V)
                while v1 == v2: v2 = randint(1, V)
                c = randint(1, A)
                G.append((v1, v2, c))

            print("Grafo sem validade gerado.")
            rep = self.arestasRepetidas(G)
            for i in rep:
                G.pop(i)
                A -= 1
            print("Removed.Edges.Repeated.")
            g = mst(G, V)
            self.salvarEntradas(V, A, G)
            arvore = g.arv
            dataG = (g.qcomps, g.peso)
            print("MST neles.")
            if g.qcomps > 1:
                self.countDnx += 1
                if self.querconexo == True: #isso nunca foi testado verdadeiramente
                    sets = [x for x in g.sets if len(x) != 0]
                    for i in range(1,len(sets)):
                        first = sets[0][randint(0, len(sets[0])-1)]
                        second = sets[i][randint(0, len(sets[i])-1)]
                        c = randint(1, A)
                        G.append((first, second, c))
                        A += 1
                        sets[0] += sets[i]
                        sets[i] = []
                    g = mst(G, V)
                    if g.qcomps == 1:
                        self.countCnx += 1
                        self.countDnx -= 1
            else: self.countCnx += 1
        self.salvarResultados(arvore, dataG, self.idGrafos)
        self.idGrafos += 1
        print("......FINISH......")

