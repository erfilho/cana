"""

IFCE - Instituto Federal do Ceará - Campus Tianguá
Aluno: Francisco Erineldo Xavier Filho
Curso: Ciências da Computação - 5o Semestre
Professor: Adonias Caetano de Oliveira
Disciplina: Construção e Análise de Algoritmos

Trabalho Computacional 01 - Ordenação e Busca

Problema 6

Faça um programa que leia N nomes e ordene-os pelo tamanho

Método utilizado: Shell Sort
"""

def shellSort(array, n):
    intervalo = n // 2
    while intervalo > 0:
        for i in range(intervalo, n):
            temp = array[i]
            j = i

            verifica = str(array[j - intervalo])
            # Caso o objeto do array seja um número ele vai executar o while normalmente, mas caso não seja ele vai verificar os tamanhos das strings para classificar pelo tamanho
            if(verifica.isnumeric()):
                while j >= intervalo and array[j - intervalo] > temp:
                    array[j] = array[j - intervalo]
                    j -= intervalo
            else:
                while j >= intervalo and len(str(array[j - intervalo])) > len(str(temp)):                    
                    array[j] = array[j - intervalo]
                    j -= intervalo
            array[j] = temp
        intervalo //= 2

teste_numeros = [0, 6, 3, 4, 5, 6, 7, 2, 1, 6, 7, 2]
teste_nomes = ['João', 'Paulo', 'Sartre', 'Tom', 'Pedro', 'Antônio', 'Francisco', 'Jean', 'André', 'Paulino', 'Marco']

tam_num = len(teste_numeros)
tam_nomes = len(teste_nomes)

shellSort(teste_numeros, tam_num)
shellSort(teste_nomes, tam_nomes)

print("Execução de testes do algoritmo: ")
print(teste_numeros)
print(teste_nomes)

print(" ")
nomes = []
tam = input("Digite a quantidade de nomes: ")
for i in range(0, int(tam)):
    var = str(input())
    nomes.append(var)
tam_nomes_f = len(nomes)
shellSort(nomes, tam_nomes_f)
print(nomes)