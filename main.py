

def ask_state():
    while True:
        user_input = input("Choisissez l’état dans lequel vous êtes(Veuillez renseigner les deux lettres de votre état, parmi la liste suivante ? (UT - NV - TX - AL - CA)): ")
        # if user_input in ["UT", "NV", "TX", "AL", "CA"]:
        break

    return user_input


def ask_price():
    while True:
        user_input = input("Quel est le prix de l’article que vous souhaitez acheter ? (Valeur en nombre uniquement) : ")
        # if user_input.isnumeric():
        break

    return user_input


def ask_qte():
    while True:
        user_input = input("Quelle quantité d’article souhaitez vous acheter ? (Valeur en nombre uniquement) : ")
        # if user_input.isnumeric():
        break

    return user_input


def start_text():
    print("Vous venez de lancer le logiciel Elephant Carpaccio, celui-ci permet de calculer le montant d’une commande, en fonction du nombre de produit, du prix de ce même produit et enfin avoir une taxe différente en fonction de votre état.")
    print("les états supporté par le logiciel sont les suivants : ")
    print("UT - 6.85 %")
    print("NV - 8.00 %")
    print("TX - 6.25 %")
    print("AL - 4.00 %")
    print("CA - 8.25 %")
    print("")


def start_text2():
    print("Pour information voici les différentes réduction dont vous pouvez bénéficier :")
    print("Valeur commande    Réduction")
    print("1 000 $        3 %")
    print("5 000 $        5 %")
    print("7 000 $        7 %")
    print("10 000 $        10 %")
    print("50 000 $        15 %")
    print("")


def main():
    print("Hello world")
    start_text()
    start_text2()
    user_state = ask_state()
    user_price = ask_price()
    user_qte = ask_qte()


if __name__ == '__main__':
    main()
