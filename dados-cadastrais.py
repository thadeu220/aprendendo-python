# script de aprendisagem com python
# ele pergunta informações para o usuário e depois imprime

print("olá! seja b bem-vindo a central de cadastros")
print("para começar, informe o seu nome")
nome = input("digite o nome")
print("insira seu CPF")
cpf = input("insira o número do CPF com 11 digitos sem pontos ou traços")
if(len(cpf)<11):
    print("o CPF tem menos de 11 dígitos")

if(len(cpf)>11):
    print("o CPF tem mais de 11 dígitos")

# caso o CPF tenha formato adequado, então continua o programa

rua = input("insira o nome de sua rua")
numero_casa = input("insira o número de sua casa")
bairro = input("insira o nome do bairro")
cidade = input("insira o nome de sua cidade")
UF = input("insira o nome do estado")

# imprime os dados

print("seu nome é ", nome)
print("seu CPF é ", cpf)
print("o nome de sua rua é ", rua)
print("o número da casa é ", numero_casa)
print("o nome do seu bairro é ", bairro)
print("nome da cidade ", cidade)
print("estado é ", UF)

# finaliza
print("até logo")