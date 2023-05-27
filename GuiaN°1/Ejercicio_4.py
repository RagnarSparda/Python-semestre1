def cubos_nicomaco(n):
    cubos = []
    for i in range(n):
        suma_impares = sum(range(2*i+1))
        cubo = suma_impares**3
        cubos.append(cubo)
    return cubos

n = int(input("Ingrese el valor de n: "))
cubos = cubos_nicomaco(n)
for i in range(n):
    print(f"{i+1}³ = {cubos[i]}")