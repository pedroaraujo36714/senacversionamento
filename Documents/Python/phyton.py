# Faça um programa em python que solicite para o usuario
# Informar 3 valores e mostrar no final

## o maior valor
## o menor valor
## o valor do meio

a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))

maior = max(a, b, c)
menor = min(a, b, c)
meio = (a + b + c) - maior - menor

print("O maior número é:", maior)
print("O menor número é:", menor)
print("O número do meio é:", meio)