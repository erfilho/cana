"""

IFCE - Instituto Federal do Ceará - Campus Tianguá
Aluno: Francisco Erineldo Xavier Filho
Curso: Ciências da Computação - 5o Semestre
Professor: Adonias Caetano de Oliveira
Disciplina: Construção e Análise de Algoritmos

Trabalho Computacional 02 - Árvores e Heapsort

Questão 04 - 

Implemente em Python todos os dez algoritmos de ordenação ensinados em sala de aula, realizando experimentos que avaliem o tempo de execução para ordenar de acordo com as seguintes regras:

I.Serão nove vetores com os seguintes tamanhos para cada um: 1000, 3000, 6000, 9000, 12000, 15000, 18000, 21000, 24000.
II.Os métodos de ordenação são:Bubble sort, Insertion sort, Selection sort, Merge sort, Quick sort, Counting sort, Radix sort, Shell sort, Bucket sort e Heapsort. 
III.Os valores armazenados nos nove vetores serão números inteiros gerados aleatoriamente. 
IV.Usar a biblioteca “matplotlib.pyplot”
V.Plotar um gráfico comparando o tempo de execução dos algoritmos de acordo com o tamanho do vetor.
"""

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

arr = [12, 45, 6, 1, 6, 23]
heapsort(arr)
n = len(arr)
print('O array ordenado é: ')
for i in range(n):
    print(f"{arr[i]}, ")