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
    def busca(self,raiz, item):
        
        if raiz is None:
            return None

        if raiz.item == item:
            return raiz
        
        if raiz.item < item:
            return self.busca(raiz.dir, item)
        elif raiz.item < item:
            return self.busca(raiz.esq, item)
        else:
            return None
        
    def altura(self, atual):
        if atual == None:
            return -1
        elif atual.esq == None and atual.dir == None:
            return 0
        else:
            if self.altura(atual.esq) > self.altura(atual.dir):
                return  1 + self.altura(atual.esq) 
            else:
                return  1 + self.altura(atual.dir) 
    
    def profundidade(self, atual):
        if atual == None:
            return -1
        elif atual.esq == None and atual.dir == None:
            return 0
        else:
            if self.altura(atual.esq) > self.altura(atual.dir):
                return  1 + self.altura(atual.esq) 
            else:
                return  1 + self.altura(atual.dir) 

    def getGrau(self, no):
        grau = 0
        no = self.busca(self.root, no)
        
        if no != None:
            if(no.esq != None):
                grau += 1
            if(no.dir != None):
                grau += 1
            return grau
        else:
            return "Nó não encontrado"
    
    def Folhas(self, atual):
        if atual != None:     
            if atual.esq == None and atual.dir == None:
                return atual.item
            return (self.Folhas(atual.esq), self.Folhas(atual.dir))
           
    def getNosFolhas(self, atual):
        nos = arvore.Folhas(atual)
        nos = str(nos)
        characters = "(Nnoe,)"
        for x in range(len(characters)):
            nos = nos.replace(characters[x],"")
        return [int(temp)for temp in nos.split() if temp.isdigit()]
   
      
arvore = Arvore()

valores = [1, 2, 3, 4, 5, 6, 8, 12, 10, 11, 13, 14, 15]

for i in valores:
    arvore.inserir(i)
    
nos_folha = arvore.getNosFolhas(arvore.root)
grau_No = arvore.getGrau(8)
altura = arvore.altura(arvore.root)
profundidade = arvore.profundidade(arvore.root)

print("Nós folha:", nos_folha)
print("Grau do nó 8:", grau_No)
print("altura da arvore:", altura)
print("profundidade da arvore:", profundidade)