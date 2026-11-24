print("Digite 0 para quebrar a sequência.\n")
mylist = []

while True:
    num = int(input("Digite um valor: "))

    mylist.append(num)

    maior_numero = max(mylist)

    if num <= 0:
        print("\nO número é menor que ou é 0")
        break

    elif num < maior_numero:
        print("\nSequência quebrada pois o número inserido é menor que o anterior")
        mylist.pop()
        print(f"Lista dos números: {mylist}")
        break

total=0

for num in mylist:
    total += num
print(f"\nO soma de todos os números é: {total}")