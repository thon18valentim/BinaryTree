from tree import Escola

# Inicializando árvore & setando nó raiz
escola = Escola("100", [10, 10, 10, 10])
root = escola.getRootAluno()

#escola.setRecursionLimit(3500)

while True:
    print("\n--- Bem vindo ao sistema da Escola ---")
    print("\n(1) Cadastrar Novo Aluno\n(2) Pesquisar Aluno por matrícula\n(3) Remover Aluno\n(4) Exibir todos\n(0) Fechar sistema\n")
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
    elif(r == 3):
        matricula = input("\nRemover Aluno (Matricula): ")
        #escola.removeAluno(matricula, root)
        escola.remover(matricula)
    elif(r == 4):
        escola.showTree(root)
