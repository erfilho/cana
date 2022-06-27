import math
import timeit
import matplotlib.pyplot as plt
import random

#Metodo Bubble Sort
def bubbleSort(lista):
    i = 0
    while i < len(lista) :
        j = 0
        while j < len(lista) - 1:
            if lista[j] > lista[j + 1]:
                temp = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temp
            j += 1
        i += 1
    return list

#Método Insertion Sort
def insertionSort(lista):
    x = 0
    n = len(lista) 
    for i in range(1, n):
        x = lista[i]
        j = i - 1
        
        while(j >= 0 and lista[j] > x):
            lista[j + 1] = lista[j]
            j = j-1
        
        lista[j+1] = x
    i = i +1
    return lista

#Método Selection Sort
def selectionSort(lista):
    i = 0
    j = i + 1
    n = len(lista)

    for i in range(0, n-1):
        min = i
        for j in range(i+1, n): 
            if(lista[j] < lista[min]):
                min = j
        aux = lista[i]
        lista[i] = lista[min]
        lista[min] = aux
        j = j + 1
    i = i + 1
    return lista

def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1

#Método Quick Sort
def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

# Counting sort in Python programming
def countingSort(A):
    size = len(A)
    B = [0] * size

    # Initialize count array
    k = max(A)
    C = [0 for w in range(k+1)]
    #C = [0] * 10

    # Store the count of each elements in count array
    for i in range(0, size):
        C[A[i]] += 1

    # Store the cummulative count
    for i in range(1, k):
        C[i] += C[i - 1]

    # Find the index of each element of the original array in count array
    # place the elements in output array
    i = size - 1
    while i >= 0:
        B[C[A[i]] - 1] = A[i]
        C[A[i]] -= 1
        i -= 1

    # remove last element
    B.pop()

    return B

# Python program for implementation of Radix Sort

# A function to do counting sort of arr[] according to
# the digit represented by exp.
def countingSortForRadixSort(arr, exp1):

	n = len(arr)

	# The output array elements that will have sorted arr
	output = [0] * (n)

	# initialize count array as 0
	count = [0] * (10)

	# Store count of occurrences in count[]
	for i in range(0, n):
		index = (arr[i]/exp1)
		count[int((index)%10)] += 1

	# Change count[i] so that count[i] now contains actual
	# position of this digit in output array
	for i in range(1,10):
		count[i] += count[i-1]

	# Build the output array
	i = n-1
	while i>=0:
		index = (arr[i]/exp1)
		output[ count[ int((index)%10) ] - 1] = arr[i]
		count[int((index)%10)] -= 1
		i -= 1

	# Copying the output array to arr[],
	# so that arr now contains sorted numbers
	i = 0
	for i in range(0,len(arr)):
		arr[i] = output[i]

# Method to do Radix Sort
def radixSort(arr):

	# Find the maximum number to know number of digits
	max1 = max(arr)

	# Do counting sort for every digit. Note that instead
	# of passing digit number, exp is passed. exp is 10^i
	# where i is current digit number
	exp = 1
	while max1/exp > 0:
		countingSortForRadixSort(arr,exp)
		exp *= 10

#Método Shell Sort 
def shellSort(nums):
    h = 1
    n = len(nums)
    while h > 0:
            for i in range(h, n):
                c = nums[i]
                j = i
                while j >= h and c < nums[j - h]:
                    nums[j] = nums[j - h]
                    j = j - h
                    nums[j] = c
            h = int(h / 2.2)
    return nums

n = len(arr) 
print ("Array antes sorting:") 
for i in range(n): 
	print(arr[i]), 

arr = shellSort(arr) 

print ("\nArray depois sorting:") 
for i in range(n): 
	print(arr[i]),

#Método Bucket Sort
def bucketSort(lista):
    largest = max(lista)
    tam = len(lista)
    size = largest/tam
 
    # Create Buckets
    buckets = [[] for i in range(tam)]
 
    # Bucket Sorting   
    for i in range(tam):
        index = int(lista[i]/size)
        if index != tam:
            buckets[index].append(lista[i])
        else:
            buckets[tam - 1].append(lista[i])
 
    # Sorting Individual Buckets  
    for i in range(len(lista)):
        buckets[i] = sorted(buckets[i])
 
 
    # Flattening the Array
    result = []
    for i in range(tam):
        result = result + buckets[i]
             
    return result

# gera uma lista de inteiros de modo aleatorio
def geraLista(tam):
  random.seed()
  i = 0
  lista = []
  while i < tam:
    lista.append(random.randint(1, tam))
    i += 1
  return lista

  #tamanhos = [100, 300] # teste
tamanhos = [1000, 3000, 6000, 9000, 12000, 15000, 18000, 21000, 24000]

temposBurbbleSort = []
temposInsertionSort = []
temposSelectionSort = []
temposMergeSort = []
temposQuickSort = []
temposCountingSort = []
temposShellSort = []
temposBucketSort = []
temposRadixSort = []

# Executa a ordenação de todos os métodos
for tamanho in tamanhos :
    lista = geraLista(tamanho)
    
    lista_teste = lista.copy() #copia a lista
    temposBurbbleSort.append(timeit.timeit("bubbleSort({})".format(lista_teste),setup="from __main__ import bubbleSort", number=1))

    lista_teste = lista.copy() #copia a lista
    temposInsertionSort.append(timeit.timeit("insertionSort({})".format(lista_teste),setup="from __main__ import insertionSort", number=1))
    
    lista_teste = lista.copy() #copia a lista
    temposSelectionSort.append(timeit.timeit("selectionSort({})".format(lista_teste),setup="from __main__ import selectionSort", number=1))
    
    lista_teste = lista.copy() #copia a lista
    temposMergeSort.append(timeit.timeit("mergeSort({})".format(lista_teste),setup="from __main__ import mergeSort", number=1))
    
    lista_teste = lista.copy() #copia a lista
    temposQuickSort.append(timeit.timeit("quickSort({})".format(lista_teste),setup="from __main__ import quickSort", number=1))
    
    lista_teste = lista.copy() #copia a lista
    temposCountingSort.append(timeit.timeit("countingSort({})".format(lista_teste),setup="from __main__ import countingSort", number=1))
    
    lista_teste = lista.copy() #copia a lista
    temposShellSort.append(timeit.timeit("shellSort({})".format(lista_teste),setup="from __main__ import shellSort", number=1))
    
    lista_teste = lista.copy() #copia a lista
    temposBucketSort.append(timeit.timeit("bucketSort({})".format(lista_teste),setup="from __main__ import bucketSort", number=1))
    
    lista_teste = lista.copy() #copia a lista
    temposRadixSort.append(timeit.timeit("radixSort({})".format(lista_teste),setup="from __main__ import radixSort", number=1))

    print( "Lista de tamanho {}".format(tamanho), " ordenada")

fig, ax = plt.subplots()
#ax.semilogx(tamanhos, temposBurbbleSort, label="Bubble Sort")
#ax.loglog(tamanhos, temposBurbbleSort, label="Bubble Sort")
ax.plot(tamanhos, temposBurbbleSort, label="Bubble Sort")
ax.plot(tamanhos, temposInsertionSort, label="Insertion Sort")
ax.plot(tamanhos, temposSelectionSort, label="Selection Sort")
ax.plot(tamanhos, temposMergeSort, label="Merge Sort")
ax.plot(tamanhos, temposQuickSort, label="Quick Sort")
ax.plot(tamanhos, temposCountingSort, label="Counting Sort")
ax.plot(tamanhos, temposRadixSort, label="Radix Sort")
ax.plot(tamanhos, temposBucketSort, label="Bucket Sort")
ax.plot(tamanhos, temposShellSort, label="Shell Sort")

#Configuracoes do grafico
plt.ylabel("TEMPO")
plt.xlabel("TAMANHO")


legend = ax.legend(loc='upper center', shadow=True)

frame = legend.get_frame()
frame.set_facecolor('0.90')

for label in legend.get_texts():
    label.set_fontsize('large')

for label in legend.get_lines():
    label.set_linewidth(1.5)
plt.show()