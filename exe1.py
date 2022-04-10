from tree import BinaryTree

# Inicializando árvore & setando nó raiz
tree = BinaryTree(10)
root = tree.getRootNode()

# Inicializando produtos como padrão
for data in [30, 5, 1, 15, 25, 20]:
    tree.addNode(data, root)

while True:
    print("\n--- Bem vindo ao sistema de Loja ---")
    print("Digite o id do produto para busca-lo  ou 0 para fechar o sistema\n")
    item = int(input("R.: "))

    if(item == 0):
        break

    if(tree.findNode(item, root)):
        print("\n-> Produto encontrado no estoque")
    else:
        print("\n-> Produto não encontrado no estoque")