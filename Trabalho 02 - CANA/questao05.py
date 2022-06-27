"""

IFCE - Instituto Federal do Ceará - Campus Tianguá
Aluno: Francisco Erineldo Xavier Filho
Curso: Ciências da Computação - 5o Semestre
Professor: Adonias Caetano de Oliveira
Disciplina: Construção e Análise de Algoritmos

Trabalho Computacional 02 - Árvores e Heapsort

Questão 05 - 
"""
import random

# Definição da função heapify
def heapify(array, n, i):
    # Inicializa o maior com a raiz
    maior = i
    d = 2 * i + 1
    e = 2 * i + 2

    if e < n and array[maior] > array[e]:
        maior = e
    if d < n and array[maior] > array[d]:
        maior = d

    if maior != i:
        array[i], array[maior] = array[maior], array[i]

        heapify(array, n, maior)

def heapsort(array):
    n = len(array)

    for i in range(n//2 - 1, -1, -1):
        heapify(array, n, i)

    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)

# gera uma lista de inteiros de modo aleatorio
def geraLista(tam):
  random.seed()
  i = 0
  lista = []
  while i < tam:
    lista.append(random.randint(1, tam))
    i += 1
  return lista

arr = geraLista(10)
heapsort(arr)
print('O array ordenado decrescente é: ')
print(arr)