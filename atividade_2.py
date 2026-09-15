lista = [
    (3, "Ana"), (10, "Bruno"), (15, "Carlos"), (18, "Daniela"),
    (19, "Eduardo"), (28, "Fernanda"), (33, "Gustavo"), (35, "Helena"),
    (43, "Igor"), (48, "Juliana"), (58, "Kleber"), (83, "Larissa"),
    (84, "Marcos"), (86, "Natália"), (97, "Otávio"), (104, "Patrícia"),
    (106, "Rafael"), (115, "Sabrina"), (120, "Tiago"), (122, "Vanessa"),
    (127, "Amanda"), (143, "Breno"), (147, "Camila"), (149, "Diego"),
    (151, "Eliane"), (175, "Fabiano"), (179, "Gabriela"),
    (184, "Henrique"), (187, "Isabela"), (194, "João"), (199, "Karen"),
    (201, "Leonardo"), (211, "Mirela"), (213, "Nicolas"),
    (232, "Olivia"), (241, "Pedro"), (244, "Queila"), (246, "Rodrigo"),
    (256, "Simone"), (258, "Túlio"), (259, "Ursula"), (261, "Victor"),
    (269, "Wesley"), (273, "Xênia"), (278, "Yasmin"), (280, "Zeca"),
    (288, "Alana"), (291, "Caio"), (292, "Diana"), (294, "Fábio")
]

procurado = 256
inicio = 0
fim = len(lista) - 1
tentativas_binaria = 0
nome = ""

# Busca binária
while inicio <= fim:
    meio = (inicio + fim) // 2
    tentativas_binaria += 1

    if lista[meio][0] == procurado:
        nome = lista[meio][1]
        break
    elif lista[meio][0] < procurado:
        inicio = meio + 1
    else:
        fim = meio - 1

# Busca sequencial
tentativas_sequencial = 0

for numero, pessoa in lista:
    tentativas_sequencial += 1

    if numero == procurado:
        break

print("Nome associado ao número 256:", nome)
print("Tentativas na busca binária:", tentativas_binaria)
print("Tentativas na busca sequencial:", tentativas_sequencial)