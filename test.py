print ("1")
print ("")
tax = 12.5 / 100
preco = 100.50
preco * tax
print("imposto = ", preco * tax)
# _ reaproveita o valor(resultado) usado uma linha acima
# mas parece só funcionar no prompt >>>
# preco + _
# print("preco com imposto = ", preco + _)
# round(_,2)
# print("arrendodar pr com imp = ", round(_,2))


imp = preco * tax
print("imposto = ", imp)
n_preco = preco + imp
print("preco com imposto = ", n_preco)
round(n_preco,2)
print("arrendodar pr com imp = ", round(n_preco,2))

print ("2")
print ("")
nasc = 1988
atual = 2019
print("Idade bruta em anos = ", atual - nasc)

print ("3")
print ("")

print('sonic the hedgehog')
print("Para aspa simples aparecer, usar 'barra invertida' ou")
print('child\'s play')
print("Para aspa simples aparecer, usar aspas duplas")
print("child\'s play")

print ("4")
print ("")

def adicionar():
    a = 44
    b = 34
    return a + b
print('adicionar = ', adicionar())
