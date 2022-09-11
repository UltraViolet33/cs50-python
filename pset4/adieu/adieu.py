import inflect

p = inflect.engine()
names = []


while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        print(names)
        sentence = "Adieu, adieu, to "
        sentence += p.join(names)
        print(sentence)

        break
