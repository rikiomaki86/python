quantidade = int(input("Digite a quantidade de numeros a serem testados: "))
cont_primos = 0

for i in range(0, quantidade):
    numero = int(input(f"Digite o numero{i}: "))
    if numero > 1:
        e_primo = True
        for j in range(2, numero):
            if numero % j == 0:
                e_primo = False
                break
            if e_primo:
                connt_primos = cont_primos + 1

print("Total de numeros: ", quantidade)
print("Total de primos: ", cont_primos)