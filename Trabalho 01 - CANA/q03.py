import random
import timeit
import math
import matplotlib.pyplot as plt

#Ordenador Quick Sort
def quickSort(lista, e, d):
    r = 0
    if (d > e):
        r = particao(lista, e, d)
        quickSort(lista, e, r - 1)
        quickSort(lista, r + 1, d)
    return lista
def particao(lista, e, d):
    i = e
    aux1 = 0
    aux2 = 0
    for j in range(e + 1, d + 1):
        if (lista[j] < lista[e]):
            i = i + 1
            aux1 = lista[i]
            lista[i] = lista[j]
            lista[j] = aux1
    aux2 = lista[e]
    lista[e] = lista[i]
    lista[i] = aux2
    return i

#Busca sequencial comum
def busca_sequencial(valor, tamanho, lista):
    i = 0
	
    while (i < tamanho and lista[i] != valor):
        i += 1
    if (i == tamanho):
        return -1
    else:
        return i

#Busca sequencial com sentinela
def busca_sentinela(valor, tamanho, lista):
    i = 0
    lista[tamanho] = valor

    while (lista[i] != valor):
        i += 1
    if(i == tamanho):
        return -1
    else:
        return i

#Busca Binária comum
def busca_binaria (valor, tamanho, lista):
   L = -1
   R = tamanho
   while (L < R-1): 
      m = math.floor((L + R)/2)
      if (lista[m] < valor):
          L = m
      else:
          R = m
   return R

#Busca binária rápida
def busca_binaria_rapida(valor, tamanho, lista):
    L = 0
    R = tamanho - 1
    while (L < R):
        m = math.floor((L + R) / 2)
        if(lista[m] < valor):
            L = m + 1
        else:
            R = m
    if (lista[R] == valor):
        return R
    else:
        return -1
 
#guarda os tempos de execução
temposBusca = []
temposBuscaSentinela = []
temposBuscaBinaria = []
temposBuscaBinariaRapida = []

#Função pricipal
def main():
    #Tamanhos dos vetores
    tamanhos = [1000, 3000, 6000, 9000, 12000, 15000, 18000, 21000, 24000]
    
    #Gera uma lista de inteiros de modo aleatorio
    def gera_lista(tam):
        random.seed()
        i = 0
        lista = []
        while i < tam:
            lista.append(random.randint(1, tam))
            i += 1
        return lista
    
    #Gera um valor aleatório entre 1 e o valor do tamanho da lista em questão
    def gera_valor(tam):
        return random.randint(1, tam)
    
    #Executa busca sequencial comum
    print("\nBusca sequencial comum")
    for tamanho in tamanhos :
        lista_busca = gera_lista(tamanho)
        valor_busca = gera_valor(tamanho)
        temposBusca.append(timeit.timeit("busca_sequencial({},{},{})".format(valor_busca, tamanho, lista_busca),setup="from __main__ import busca_sequencial", number=1))
        print("Busca de %d" % valor_busca, "na lista de tamanho %d concluída" % tamanho)
     
    #Executa busca sequencial com sentinela
    print("\nBusca sequencial com sentinela")
    for tamanho in tamanhos :
        lista_busca_sentinela = gera_lista(tamanho)
        valor_busca_sentinela = gera_valor(tamanho)
        lista_busca_sentinela.append(0)
        temposBuscaSentinela.append(timeit.timeit("busca_sentinela({},{},{})".format(valor_busca_sentinela, tamanho, lista_busca_sentinela),setup="from __main__ import busca_sentinela", number=2))
        print("Busca de %d" % valor_busca_sentinela, "na lista de tamanho %d concluída" % tamanho)

    #Executa busca binária comum
    print("\nBusca binária comum")
    for tamanho in tamanhos :
        lista_busca_binaria = gera_lista(tamanho)
        valor_busca_binaria = gera_valor(tamanho)
        lista_busca_binaria =  quickSort(lista_busca_binaria, 0, len(lista_busca_binaria)-1)
        temposBuscaBinaria.append(timeit.timeit("busca_binaria({},{},{})".format(valor_busca_binaria, tamanho, lista_busca_binaria),setup="from __main__ import busca_binaria", number=3))
        print("Busca de %d" % valor_busca_binaria, "na lista de tamanho %d concluída" % tamanho)

    #Executa busca binária rápida
    print("\nBusca binária rápida")
    for tamanho in tamanhos :
        lista_busca_binaria_rapida = gera_lista(tamanho)
        valor_busca_binaria_rapida = gera_valor(tamanho)
        lista_busca_binaria_rapida =  quickSort(lista_busca_binaria_rapida, 0, len(lista_busca_binaria_rapida)-1)
        temposBuscaBinariaRapida.append(timeit.timeit("busca_binaria_rapida({},{},{})".format(valor_busca_binaria_rapida, tamanho, lista_busca_binaria_rapida),setup="from __main__ import busca_binaria_rapida", number=4))
        print("Busca de %d" % valor_busca_binaria_rapida, "na lista de tamanho %d concluída" % tamanho)

    #Configuracoes do grafico
    fig, tela = plt.subplots()

    tela.plot(tamanhos, temposBusca, label="Busca Sequencial")
    tela.plot(tamanhos, temposBuscaSentinela, label="Busca Sequencial com sentinela")
    tela.plot(tamanhos, temposBuscaBinaria, label="Busca Binária")
    tela.plot(tamanhos, temposBuscaBinariaRapida, label="Busca Binária Rápida")
   
    plt.ylabel("TEMPO")
    plt.xlabel("TAMANHO")

    legend = tela.legend(loc='upper left', shadow=True)

    frame = legend.get_frame()
    frame.set_facecolor('0.90')

    for label in legend.get_texts():
        label.set_fontsize('large')

    for label in legend.get_lines():
        label.set_linewidth(1.5)
    plt.show()
    
if __name__== "__main__":
    main()