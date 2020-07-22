import random
num_pensado = None
num_escolhido = None

num_pensado = int(input('Advinhe o número que escolhi'))
print("Pensarei em um número entre 1 e 10 e você tentará advinhá-lo")
num_escolhido = random.randint(1,10)
while num_pensado != num_escolhido:
    print('')
    num_pensado = int(input('Advinhe o número que escolhi'))
print('Parabéns, acertou')
