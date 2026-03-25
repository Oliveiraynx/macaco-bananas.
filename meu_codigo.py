# macaco-bananas.
Meu primeiro programa em Python que divide bananas entre amigos.

bananas = int(input("Quantas bananas você tem? "))
amigos = int(input("Quantos amigos vão dividir? "))

sobras = bananas % amigos

if sobras == 0:
    print("Deu para todos certinho")
else:
    print("Sobrou", sobras, "banana(s)")
