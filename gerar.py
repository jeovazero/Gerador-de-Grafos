# -*- coding: utf8 -*-
#---------------------------------------------------------
# O que isso faz:
#   Gera um Grafo aleatorio (random)
#   que por azar ou sorte pode ser desconexo.
#
# E nao eh soh isso:
#   Voce pode garantir que eh conexo,
#   respondendo a pergunta no inicio da execucao.
#
#   Programador: jeovazero
#
#--------------------------------------------------------
from random import randint
from kruskal import mst
from libGerar import geradorGrafos
#--=--=--=-=-=--=-=-=--=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-
print("Antes de começar: \"Não seja um usuário burro, digite o que lhe eh pedido\"\n")
print("A saida no arquivo \'ginput.txt\':\nNa primeira linha terá o número de VÉRTICES(V) e o número de ARESTAS(A)\nDepois terá (A) linhas na forma <vertice1> <vertice2> <peso>\n")

print("Quantos vértices terá TODOS os grafos gerados?: ")
V = int(input())

print("O Grafo eh completo? [s/n]: ")
complete = raw_input()

if complete != "s":
    print("Você quer que gere quantos Grafos de %d vértices?: " % V)
    quantGrafos = int(input())

    querconexo = False
    print("Quer todos os Grafos conexos? [s/n]: ")
    resp = raw_input()
    while resp != 's' and resp != 'n':
        print("Digita a entrada correta usuário BURRO!: ")
        resp = raw_input()
        if resp == 's':
            querconexo = True
            print("Viu como é fácil. :P")

print("O nome dos arquivos de saídas são:\n \'ginput.txt\' e \'gresult.txt\'.")
print("\'ginput.txt\' contem os dados do grafo de entrada.")
print("\'gresult.txt\' contem os dados da arvore minima.")

#--=--=--=-=-=--=-=-=--=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-

m = geradorGrafos()
m.cleanFile()
if complete == 's':
    m.setCompleto(True)
    m.gerar(V)
else:
    if querconexo: m.setCnx(True)
    for i in range(0, quantGrafos):
        m.gerar(V)
    print("Grafos Conexos gerados: %d" % m.countCnx)
    print("Grafos DesConexos gerados: %d" % m.countDnx)

