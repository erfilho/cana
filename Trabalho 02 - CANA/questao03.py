from errno import EILSEQ
from setuptools import PEP420PackageFinder


class Node:
    def __init__(self, chave= None, esquerda= None, direita= None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

    def __repr__(self) -> str:
        return "%s <- %s -> %s" % (self.esquerda and self.esquerda.chave,
                                    self.chave,
                                    self.direita and self.direita.chave)


def altura(raiz):
    if raiz is None:
        return 0
    return max(altura(raiz.esquerda), altura(raiz.direita)) + 1
def profundidade(raiz, no):
    if raiz is None:
        return 0
    
    dist = 0

    if raiz == no:
        return dist + 1
    elif profundidade(raiz.esquerda, no) >= 0:
        dist = profundidade(raiz.esquerda, no)
        return dist + 1
    elif profundidade(raiz.direita, no) >= 0:
        dist = profundidade(raiz.direita, no)
        return dist + 1
    return dist




raiz = Node(8)
raiz.esquerda = Node(4)
raiz.direita = Node(12)

raiz.esquerda.esquerda = Node(2)
raiz.esquerda.direita = Node(6)
raiz.esquerda.esquerda.esquerda = Node(1)
raiz.esquerda.esquerda.direita = Node(3)
raiz.esquerda.direita.esquerda = Node(5)

raiz.direita.esquerda = Node(10)
raiz.direita.direita = Node(14)
raiz.direita.esquerda.direita = Node(11)
raiz.direita.direita.esquerda = Node(13)
raiz.direita.direita.direita = Node(15)



print(profundidade(raiz, 6))