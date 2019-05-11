import time

print("Olá Mundo")
variavelUsuario = input("Digite alguma coisa: ")

variavelFloat = float(variavelUsuario);

if variavelFloat == 3.14:
    print("Dia do RaspBerry Pi")
elif variavelFloat == 42.0:
    print("Obrigado pelos peixes")
else:
    print("até mais")
    

for x in range(100):
    print("Nunca mais vou aprontar " + str(x+1))
    
tempo = 0
while tempo < 10:
    print("Tempo passando..." + str(tempo))
    #espera um segundo o fluxo do programa
    time.sleep(1)
    tempo = tempo + 1
    
print("O programa acabou")