import sys

class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

  def __str__(self):
    return str(self.data)

class BinaryTree:
  def __init__(self, data):
    self.root = Node(data)

  def getRootNode(self):
    return self.root

  def addNode(self, data, root = None):
    if root is None:
      root = self.root
    
    if data > root.data:
      if root.right is None:
        root.right = Node(data)
      else:
        self.addNode(data, root.right)
    else:
      if root.left is None:
        root.left = Node(data)
      else:
        self.addNode(data, root.left)

  def findNode(self, data, root):
    if root is None:
      return False

    if data == root.data:
      return True
      
    if data > root.data:
      return self.findNode(data, root.right)
      
    return self.findNode(data, root.left)

  def showTree(self, root):
    if not root:
      return
    
    self.showTree(root.left)
    print(root)
    self.showTree(root.right)

class Aluno:
    def __init__(self, matricula, notas):
        self.matricula = matricula
        self.notas = notas
        self.left = None
        self.right = None

    def getMedia(self):
        return sum(self.notas)/len(self.notas)

    def __str__(self):
      return str(self.matricula)

class Escola:
    def __init__(self, matricula, notas):
       self.root = Aluno(matricula, notas)

    def setRecursionLimit(self, value):
        sys.setrecursionlimit(value)

    def getRootAluno(self):
        return self.root

    def addAluno(self, matricula, notas, root = None):
        if root is None:
            root = self.root
    
        if matricula > root.matricula:
            if root.right is None:
                root.right = Aluno(matricula, notas)
            else:
                self.addAluno(matricula, notas, root.right)
        else:
            if root.left is None:
                root.left = Aluno(matricula, notas)
            else:
                self.addAluno(matricula, notas, root.left)

    def findAluno(self, matricula, root):
        if root is None:
            return None

        if matricula == root.matricula:
            return root
      
        if matricula > root.matricula:
            return self.findAluno(matricula, root.right)
      
        return self.findAluno(matricula, root.left)

    def removeAtual(self, root):
      while root.left is not None and root is not None:
        root = root.left
      
      return root

    def removeAluno(self, matricula, root):
      aluno = self.findAluno(matricula, root)

      if aluno is None:
        return None

      # Removendo nós sem filhos
      if aluno.right is None and aluno.left is None:
        aluno = None
      elif aluno.left is None: # Removendo nó com filho a direita
        aluno = aluno.right
      elif aluno.right is None: # Removendo nó com filho a esquerda
        aluno = aluno.left
      else: # Removendo nó com ambos os filhos
        temp = self.removeAtual(aluno.right)
        aluno.matricula = temp.matricula
        aluno.notas = temp.notas

        aluno.left = self.removeAluno(temp.matricula, aluno.right)

      return aluno

    def showTree(self, root):
      if not root:
        return
      
      self.showTree(root.left)
      print(root)
      self.showTree(root.right)

    # O sucessor é o Nó mais a esquerda da subarvore a direita do No que foi passado como parametro do metodo
    def nosucessor(self, apaga): # O parametro é a referencia para o No que deseja-se apagar
        paidosucessor = apaga
        sucessor = apaga
        atual = apaga.right # vai para a subarvore a direita

        while atual != None: # enquanto nao chegar no Nó mais a esquerda
              paidosucessor = sucessor
              sucessor = atual
              atual = atual.left # caminha para a esquerda

        # *********************************************************************************
        # quando sair do while "sucessor" será o Nó mais a esquerda da subarvore a direita
        # "paidosucessor" será o o pai de sucessor e "apaga" o Nó que deverá ser eliminado
        # *********************************************************************************
        if sucessor != apaga.right: # se sucessor nao é o filho a direita do Nó que deverá ser eliminado
              paidosucessor.left = sucessor.right # pai herda os filhos do sucessor que sempre serão a direita
              # lembrando que o sucessor nunca poderá ter filhos a esquerda, pois, ele sempre será o
              # Nó mais a esquerda da subarvore a direita do Nó apaga.
              # lembrando também que sucessor sempre será o filho a esquerda do pai
              sucessor.right = apaga.right # guardando a referencia a direita do sucessor para 
                                      # quando ele assumir a posição correta na arvore
        return sucessor

    def remover(self, v):
         if self.root == None:
               return False # se arvore vazia
         atual = self.root
         pai = self.root
         filho_esq = True
         # ****** Buscando o valor **********
         while atual.matricula != v: # enquanto nao encontrou
               pai = atual
               if v < atual.matricula: # caminha para esquerda
                    atual = atual.left
                    filho_esq = True # é filho a esquerda? sim
               else: # caminha para direita
                    atual = atual.right 
                    filho_esq = False # é filho a esquerda? NAO
               if atual == None:
                    return False # encontrou uma folha -> sai
         # fim laço while de busca do valor

         # **************************************************************
         # se chegou aqui quer dizer que encontrou o valor (v)
         # "atual": contem a referencia ao No a ser eliminado
         # "pai": contem a referencia para o pai do No a ser eliminado
         # "filho_esq": é verdadeiro se atual é filho a esquerda do pai
         # **************************************************************

         # Se nao possui nenhum filho (é uma folha), elimine-o
         if atual.left == None and atual.right == None:
               if atual == self.root:
                    self.root = None # se raiz
               else:
                    if filho_esq:
                         pai.left =  None # se for filho a esquerda do pai
                    else:
                         pai.right = None # se for filho a direita do pai

         # Se é pai e nao possui um filho a direita, substitui pela subarvore a direita
         elif atual.right == None:
               if atual == self.root:
                    self.root = atual.left # se raiz
               else:
                    if filho_esq:
                         pai.left = atual.left # se for filho a esquerda do pai
                    else:
                         pai.right = atual.left # se for filho a direita do pai
         
         # Se é pai e nao possui um filho a esquerda, substitui pela subarvore a esquerda
         elif atual.left == None:
               if atual == self.root:
                    self.root = atual.right # se raiz
               else:
                    if filho_esq:
                         pai.left = atual.right # se for filho a esquerda do pai
                    else:
                         pai.right = atual.right # se for  filho a direita do pai

         # Se possui mais de um filho, se for um avô ou outro grau maior de parentesco
         else:
               sucessor = self.nosucessor(atual)
               # Usando sucessor que seria o Nó mais a esquerda da subarvore a direita do No que deseja-se remover
               if atual == self.root:
                    self.root = sucessor # se raiz
               else:
                    if filho_esq:
                         pai.left = sucessor # se for filho a esquerda do pai
                    else:
                         pai.right = sucessor # se for filho a direita do pai
               sucessor.left = atual.left # acertando o ponteiro a esquerda do sucessor agora que ele assumiu 
                                        # a posição correta na arvore   

         return True