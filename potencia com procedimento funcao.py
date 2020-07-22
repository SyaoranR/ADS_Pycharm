def potencia(base,exp): # função com parâmetro opcional
  if exp==0: # todo número elevado a zero = 1
    return 1
  pot=base; i=1; # ele = ele mesmo; inicialização
  while i < exp:
     pot=pot*base
     i=i+1
  return pot

print("Começa aqui!")
exec = 's'
while exec == 's':
    b = int(input("Informe uma base: "))
    e = int(input("Informe um expoente: "))
    print (b, ' elevado a ', e, ' = ', potencia(b, e))
    exec = str(input("Continuar?, DIGITE 's' para continuar ou 'n' para não "))