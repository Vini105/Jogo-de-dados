import random
import time

pergun = int(input("Qual soma vc acha q vai dar? "))

numeros = [1,2,3,4,5,6]
chance = 0

#calcular a probabilidade
for x in numeros:
    for y in numeros:
        #print(x,y)
        if x + y == pergun:
            chance += 1

print(f"A chance é {(chance/36)*100:.2f}%")

print("Sorteando...")
time.sleep(1)

#sortear os números
dado1 = random.randint(1,6)
dado2 = random.randint(1,6)


print(f'Os dados foram {dado1} e {dado2}, a soma é {dado1 + dado2}')
if dado1 + dado2 == pergun:
    print("Parabéns!Você acertou!")
else:
    print("Não foi dessa vez :(")