class No:
    def __init__(self, key, dir, esq):
        self.item = key
        self.dir = dir
        self.esq = esq

class Arvore:
    def __init__(self):
        self.root = No(None, None, None)
        self.root = None

    def inserir(self, v):
          novo = No(v,None,None) # cria um novo Nó
          if self.root == None:
               self.root = novo
          else: # se nao for a raiz
               atual = self.root
               while True:
                    anterior = atual
                    if v <= atual.item: # ir para esquerda
                         atual = atual.esq
                         if atual == None:
                                anterior.esq = novo
                                return
                    # fim da condição ir a esquerda
                    else: # ir para direita
                         atual = atual.dir
                         if atual == None:
                                 anterior.dir = novo
                                 return
                    # fim da condição ir a direita

    def altura(self, atual):
        if atual == None or atual.esq == None and atual.dir == None:
            return 0
        else:
            if self.altura(atual.esq) > self.altura(atual.dir):
                return  1 + self.altura(atual.esq) 
            else:
                return  1 + self.altura(atual.dir) 
    
    def profundidade(self):
        return 0

    def getGrau(self, no):
        return 0

    def getNosFolhas(self, atual):
         if atual.esq == None and atual.dir == None:
              return atual.key
        
arvore = Arvore()

valores = [1, 2, 3, 4, 5, 6, 8, 12, 10, 11, 13, 14, 15]

for i in valores:
    arvore.inserir(i)

print(arvore.getNosFolhas(arvore.root))