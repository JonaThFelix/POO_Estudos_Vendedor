#Estudos de POO
from Vendedor import Vendedor #importa a classe Vendedor da outra janela

vendedor1 = Vendedor('Jonathan')  #vendedor 1 = classe principal (Vendedor)
#print(vendedor1.nome) #print o nome do vendedor1

#execução do vendedor1
vendedor1.vendeu(1000)
vendedor1.bateu_metas(600)
print('\n')


vendedor2 = Vendedor('Ana')
vendedor2.vendeu(400)
vendedor2.bateu_metas(600)

