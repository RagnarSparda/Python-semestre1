import random

numbers = [random.randint(40, 350) for _ in range(20)]

search_num = int(input("Ingrese el número a buscar: "))

occurrences = numbers.count(search_num)

print(f"La lista generada es: {numbers}")
print(f"El número {search_num} aparece {occurrences} veces en la lista.")