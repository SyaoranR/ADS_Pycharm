# lista de exerc�cios 1
print("4 Tabuada de n para m")
for n in range(1, 11, 1):
    print('')
    print("Tabuada de ", n)
    print('')
    for m in range(1, 11, 1):
        print(n, ' * ', m, ' = ', n * m)

print("")
print("5 Unidade, Dezena, Centena")
print("")

x = int(input("Entre com o valor inteiro x: "))
cent = x / 100
print('Centena = %4.2f' % cent)
dez = (x / 10) % 10
print('Dezena = %4.2f' % dez)
unid = x % 10
print('Unidade = %4.2f' % unid)


print("")
print("6 Consumo Veículo")
print("")

# l => combust�vel abastecido no tanque, S = dist�ncia percorrida
# s => dist�ncia inicial, c=> autonomia do carro
l = int(input("Informe quanto combustível abasteceu o veículo: "))
S = int(input("Informe a distância final do veículo: "))
s = int(input("Informe a distância inicial do veículo: "))
c = (S - s) / l
print('Autonomia do veículo: %4.2f' % c)
g = c/l
print('Gasto por litro: %4.2f' % g)
