import threading

i = 1
tempo_de_espera = 5

while i < 10:
    for i in range(1, 11):
        i += 1
        print(i, end=" ")
