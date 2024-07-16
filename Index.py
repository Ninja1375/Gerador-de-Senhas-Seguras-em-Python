import random
import string

def gerar_senha(comprimento=12, incluir_maiusculas=True, incluir_minusculas=True, incluir_numeros=True, incluir_especiais=True):
    caracteres = ''
    if incluir_maiusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_especiais:
        caracteres += string.punctuation
    
    if not caracteres:
        raise ValueError("Pelo menos um tipo de caractere deve ser selecionado")
    
    senha = ''.join(random.choice(caracteres) for i in range(comprimento))
    return senha

def main():
    print("Gerador de Senhas Seguras")
    comprimento = int(input("Digite o comprimento da senha (padrão 12): ") or 12)
    incluir_maiusculas = input("Incluir letras maiúsculas? (s/n, padrão 's'): ").lower() in ['s', 'sim', '']
    incluir_minusculas = input("Incluir letras minúsculas? (s/n, padrão 's'): ").lower() in ['s', 'sim', '']
    incluir_numeros = input("Incluir números? (s/n, padrão 's'): ").lower() in ['s', 'sim', '']
    incluir_especiais = input("Incluir caracteres especiais? (s/n, padrão 's'): ").lower() in ['s', 'sim', '']

    senha = gerar_senha(comprimento, incluir_maiusculas, incluir_minusculas, incluir_numeros, incluir_especiais)
    print(f"Sua senha gerada é: {senha}")

if __name__ == "__main__":
    main()
