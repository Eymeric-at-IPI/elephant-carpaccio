# Globals
state_taxe = {
    "UT": 0.0685,
    "NV": 0.08,
    "TX": 0.0400,
    "AL": 0.0400,
    "CA": 0.0825
}


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

    return float(user_input)


def ask_qte():
    while True:
        user_input = input("Quelle quantité d’article souhaitez vous acheter ? (Valeur en nombre uniquement) : ")
        # if user_input.isnumeric():
        break

    return int(user_input)


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


def compute_bill(_user_state, _user_price, _user_qte):
    bill = _user_qte * _user_price
    bill_reduc = 0
    bill_taxe = 0

    if bill <= 1000:
        bill_reduc = bill * 0.03
    elif bill <= 5000:
        bill_reduc = bill * 0.05
    elif bill <= 7000:
        bill_reduc = bill * 0.07
    elif bill <= 10000:
        bill_reduc = bill * 0.10
    elif bill <= 50000:
        bill_reduc = bill * 0.15

        print("UT - 6.85 %")
        print("NV - 8.00 %")
        print("TX - 6.25 %")
        print("AL - 4.00 %")
        print("CA - 8.25 %")

    if _user_state == "UT":
        bill_taxe = bill_reduc * 0.0685
    elif _user_state == "NV":
        bill_taxe = bill_reduc * 0.08
    elif _user_state == "TX":
        bill_taxe = bill_reduc * 0.0625
    elif _user_state == "AL":
        bill_taxe = bill_reduc * 0.0400
    elif _user_state == "CA":
        bill_taxe = bill_reduc * 0.0825

    return {
        "bill": bill,
        "bill_reduc": bill_reduc,
        "bill_taxe": bill_taxe
    }


def print_bill(_bill_computen _user_state):
    print("Votre commande est d’un total de :", _bill_compute["bill"] - _bill_compute["bill_reduc"] + _bill_compute["bill_taxe"], "$ TTC soit", _bill_compute["bill"] - _bill_compute["bill_reduc"], "$ HT, puisque votre état est :", _user_state, "la taxe à appliquer est : XX % le montant de la taxe est : XX $ ...")


def main():
    print("Hello world")
    start_text()
    start_text2()
    user_state = ask_state()
    user_price = ask_price()
    user_qte = ask_qte()
    print(compute_bill(user_state, user_price, user_qte))


if __name__ == '__main__':
    main()
