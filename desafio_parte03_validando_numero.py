import re

def validate_numero_telefone(phone_number):
    """
    Valida se o número de telefone está no formato correto.

    Args:
        phone_number (str): O número de telefone a ser validado.

    Returns:
        str: Mensagem indicando se o número é válido ou inválido.
    """
    pattern = pattern = r"\(\d{2}\) 9\d{4}-\d{4}" # Padrão regex para o formato (XX) 9XXXX-XXXX
    if re.match(pattern, phone_number):
        return "Número de telefone válido."
    else:
        return "Número de telefone inválido."

phone_number = input("Digite o número de telefone: ")
result = validate_numero_telefone(phone_number)
print(result)