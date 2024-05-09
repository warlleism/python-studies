for i in range(1, 11):
    if i == 5:
        break
    print(i, "", end="")

for i in range(1, 11):
    if i == 5:
        continue
    print(i, "", end="")

count = 0

while True:
    res = input('deseja incrementar? sim/não ')
    condition = res.lower()

    if condition != 'sim' and condition != 'não':
        print('Digite "Sim" ou "Não"')
        continue

    if condition == 'sim':
        count += 1
        print(count)
        continue
    else:
        break
