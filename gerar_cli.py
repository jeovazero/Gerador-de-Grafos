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

# parse command line
import argparse

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument(
		"NUMERO_DE_VERTICES",
		help=u"Número de vertices",
		type=int,
		)
	parser.add_argument(
		"-cmp",
		"--completo",
		help=u"Grafo copleto?",
		action="store_true",
		dest="cmp")
	parser.add_argument(
		"-cnx",
		"--conexo",
		help=u"Grafo conexo?",
		action="store_true",
		dest="cnx")
	parser.add_argument(
		"-q",
		"--quantidade-de-grafos",
		help=u"Quantidade de grafos",
		type=int,
		default=1,
		dest='q')
	parser.add_argument(
		"-v", "--verbose",
		help="increase output verbosity",
		action="store_true")
	args = parser.parse_args()
	
	if args.verbose:
		print(args)
	
	V = args.NUMERO_DE_VERTICES

	complete = args.cmp

	quantGrafos = args.q
	querconexo = args.cnx
	if args.verbose:
		print("O nome dos arquivos de saídas são:\n \'ginput.txt\' e \'gresult.txt\'.")
		print("\'ginput.txt\' contem os dados do grafo de entrada.")
		print("\'gresult.txt\' contem os dados da arvore minima.")

	#--=--=--=-=-=--=-=-=--=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-

	m = geradorGrafos()
	m.cleanFile()
	if complete:
		m.setCompleto(True)
		m.gerar(V)
	else:
		if querconexo:
			m.setCnx(True)
		for i in range(quantGrafos):
			m.gerar(V)
		if args.verbose:
			print("Grafos Conexos gerados: %d" % m.countCnx)
			print("Grafos DesConexos gerados: %d" % m.countDnx)


if __name__ == "__main__":
	main()
