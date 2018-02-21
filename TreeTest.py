from trees import BinaryTree

arvore = BinaryTree()

arvore.insert(60)
arvore.insert(17)
arvore.insert(35)
arvore.insert(73)

print(arvore.minValue())
print(arvore.maxValue(arvore.root))

arvore.inOrderTransversal()