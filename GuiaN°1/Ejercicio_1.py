paragraph = "La Universidad de los Lagos es una institucion estatal fundada en 1993. Esta Universidad regional entrega una contribucion significativa al desarrollo sostenible del territorio. Como Universidad sus pilares fundamentales se basan en la inclusion, pluralismo, conciencia ambiental y participacion democratica."

words = paragraph.split()

count = words.count("Universidad")

print(count)

words_tuple = tuple(word for word in words if word == "Universidad")
print(words_tuple)