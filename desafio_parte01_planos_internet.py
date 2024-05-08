# TODO: Crie uma Função: recomendar_plano para receber o consumo médio mensal:
def recomendar_plano(consumo_mensal):
  if consumo_mensal <= 10:
    plano_recomendado = "Essencial Fibra (50Mbps)"
  elif consumo_mensal <= 20:
    plano_recomendado = "Prata Fibra (100Mbps)"
  else:
    plano_recomendado = "Premium Fibra (300Mbps)"

  return plano_recomendado
    
# TODO: Crie uma Estrutura Condicional para verifica o consumo médio mensal 
consumo = float(input("Digite seu consumo médio mensal de dados em GB: "))
# TODO: Retorne o plano de internet adequado:
plano_recomendado = recomendar_plano(consumo)
print(f"O plano ideal para você é o {plano_recomendado}")  

# Solicita ao usuário que insira o consumo médio mensal de dados:
# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
# Chama a função recomendar_plano e imprime o plano recomendado:
