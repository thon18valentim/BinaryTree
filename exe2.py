import sys

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


# Inicializando árvore & setando nó raiz
escola = Escola("100", [10, 10, 10, 10])
root = escola.getRootAluno()

#escola.setRecursionLimit(3500)

while True:
    print("\n--- Bem vindo ao sistema da Escola ---")
    print("\n(1) Cadastrar Novo Aluno\n(2) Pesquisar Aluno por matrícula\n(0) Fechar sistema\n")
    r = int(input("R.: "))

    if(r == 0):
        break
    elif(r == 1):
        notas = []
        matricula = input("\nMatricula: ")
        for i in range(1, 5):
            notas.append(int(input("\nNota %d: " % i)))
        escola.addAluno(matricula, notas)
    elif(r == 2):
        s = input("\nMatricula: ")
        aluno = escola.findAluno(s, root)
        if aluno is None:
            print("\n-> Aluno não encontrado")
        else:
            print("\n-> Aluno encontrado")
            print("\n-> Matrícula: %s" % aluno.matricula)
            print("-> Média: %.2f" % aluno.getMedia())
