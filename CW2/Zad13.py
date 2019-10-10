def wypisz_slownik_z_list(lista_slownikow):
    output = ""
    for slownik in lista_slownikow:
        for element in slownik.values():
            output += element + ' '
    print(output)


lista_slownikow = [{"aaa": "bbb", "ccc": "ddd"}, {"eee": "fff", "ggg": "hhh"}]
wypisz_slownik_z_list(lista_slownikow)
