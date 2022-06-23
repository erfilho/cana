# Definição da função heapify
def heapify(array, n, i):
    # Inicializa o maior com a raiz
    maior = i
    d = 2 * i + 1
    e = 2 * i + 2

    if e < n and array[maior] < array[e]:
        maior = e
    if d < n and array[maior] < array[d]:
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