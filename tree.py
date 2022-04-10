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
                self.addAluno(matricula, root.right)
        else:
            if root.left is None:
                root.left = Aluno(matricula, notas)
            else:
                self.addAluno(matricula, root.left)

    def findAluno(self, matricula, root):
        if root is None:
            return None

        if matricula == root.matricula:
            return root
      
        if matricula > root.matricula:
            return self.findAluno(matricula, root.right)
      
        return self.findAluno(matricula, root.left)