def cadastrar_equipamentos():
  """
  Função para cadastrar equipamentos na lista.

  Retorna:
    Lista de equipamentos cadastrados.
  """
  equipamentos = []
  for i in range(3):
    equipamento = input("Digite o nome do equipamento: ")
    equipamentos.append(equipamento)
  return equipamentos

def exibir_equipamentos(equipamentos):
  """
  Função para exibir a lista de equipamentos cadastrados.

  Argumentos:
    equipamentos: Lista de equipamentos.
  """
  print("\nLista de Equipamentos:")
  for equipamento in equipamentos:
    print(f"- {equipamento}")

# Cadastro dos equipamentos
equipamentos_cadastrados = cadastrar_equipamentos()

# Exibição da lista de equipamentos
exibir_equipamentos(equipamentos_cadastrados)