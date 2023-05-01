meta = 200 #meta definida, não precisa está dentro do bloco

#aqui cria as classes e funções, e o uso do self = classe
class Vendedor:
  def __init__(self,nome): #método construtor, será tudo que terá dentro da classe
    self.nome = nome #nome não foi definido, logo está no parâmetro construtor
    self.vendas = 0 #self que já terá um valor e não receberá o prório self.vendas = vendas, não precisa está no parâmetro construtor

  def vendeu(self,vendas):
    self.vendas = vendas
    print(self.nome,'vendeu o total de',self.vendas)

  def bateu_metas(self,meta):
    if self.vendas >= meta:
      print(self.nome,'bateu a meta','com o total de',self.vendas)
    else:
      print(self.nome,'Não bateu a meta','vendeu apenas',self.vendas)
