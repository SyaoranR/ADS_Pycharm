import random
num_pensado = None
num_escolhido = None

num_pensado = int(input('Advinhe o n�mero que escolhi'))
print("Pensarei em um n�mero entre 1 e 10 e voc� tentar� advinh�-lo")
num_escolhido = random.randint(1,10)
while num_pensado != num_escolhido:
    print('')
    num_pensado = int(input('Advinhe o n�mero que escolhi'))
print('Parab�ns, acertou')
