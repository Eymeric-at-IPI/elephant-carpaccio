

def ask_state():
    while True:
        user_state = input("Choisissez l’état dans lequel vous êtes(Veuillez renseigner les deux lettres de votre état, parmi la liste suivante ? (UT - NV - TX - AL - CA)): ")
        # if user_state in ["UT", "NV", "TX", "AL", "CA"]:
        break

    return user_state


def start_text():
    print("Vous venez de lancer le logiciel Elephant Carpaccio, celui-ci permet de calculer le montant d’une commande, en fonction du nombre de produit, du prix de ce même produit et enfin avoir une taxe différente en fonction de votre état.")
    print("les états supporté par le logiciel sont les suivants : ")
    print("UT - 6.85 %")
    print("NV - 8.00 %")
    print("TX - 6.25 %")
    print("AL - 4.00 %")
    print("CA - 8.25 %")


def main():
    print("Hello world")
    start_text()
    user_state = ask_state()


if __name__ == '__main__':
    main()
