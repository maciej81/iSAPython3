names_list = []
message = """Baza danych
Wybierz opcję:
Wyszukaj imie, naciśnij klawisz 1:
Dodaj imie, naciśnij klawisz 2:
Usuń imie, naciśnij klawisz 3:
Wyświetl liczbę imion, naciśnij klawisz 4:
Wyświetl listę imion, naciśnij klawisz 5:
Zakończ program, naciśnij klawisz 0:"""

def action(note):
    return  input(note)

response = action(message)
while response != "0":
    if response == "1":
        name = action("Podaj wyszukiwane imię: ")
        name = str(name).upper()
        result = name in names_list
        if result:
            print("Imię {} jest już w kontaktach".format(name))
        else:
            print("Imię {} nie zostało odnalezione".format(name))

    elif response == "2":
        name = action("Dodaj imię do listy: ")
        name = str(name).upper()
        result = name in names_list

        if result:
            print("Imię {} jest już w kontaktach".format(name))
        else:
            names_list.append(name)
            print("Imię {} zostało dodane do kontaktów".format(name))

    elif response == "3":
        name = action("Podaj imię, które chcesz usunąć: ")
        name = str(name).upper()
        result = name in names_list

        if result:
            names_list.remove(name)
            print("Imię {} zostało usunięte".format(name))
        else:
            print("Brak imienia na liście")

    elif response == "4":
        print("Liczba imion na liście to {}".format(str(len(names_list))))

    elif response == "5":
        print(names_list)

    else:
        print("Podałeś złę polecenie, spróbuj ponownie.")

    response = action("Podaj nowe polecenie\n")