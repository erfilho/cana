# -*- coding: utf-8 -*-
#e) PROBLEMA 05: Crie um programa que dado uma string, coloque as letras dela em ordem crescente (Dica: Use C ou Python ou Ruby).

def ordenador_tipo_bubbleSort(string , tamanho_string):
    aux1 = ''
    aux2 = []
    for i in range(tamanho_string-1, -1, -1):
        for j in range(0, i):
            if(string[j] > string[j+1]):
                aux2 = list(string)
                aux1 = aux2[j]
                aux2[j] = aux2[j+1]
                aux2[j+1] = aux1
                string = ''.join(aux2)
    return string

def main():
    string = 'CIENCIA DA COMPUTACAO IFCE TIANGUA'
    print("String ordenada de forma crescente: [%s]" % ordenador_tipo_bubbleSort(string, len(string)))
    
if __name__== "__main__":
    main()