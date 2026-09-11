# Entrada de dados
nome = input("Digite o seu nome: ")
idade = input("Digite a sua idade: ")
peso_texto = input("Digite o seu peso em kg: ")
altura_texto = input("Digite a sua altura em metros: ")

# Conversão de string para float
peso_float = float(peso_texto)
altura_float = float(altura_texto)

# Cálculo do IMC
altura_ao_quadrado = altura_float * altura_float
imc = peso_float / altura_ao_quadrado

# Saída de dados
print(f"Olá, {nome}! O resultado é {imc:.2f}.")