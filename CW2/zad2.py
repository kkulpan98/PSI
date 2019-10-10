imie = "Jakub"
nazwisko = "Kulpan"

litera_1 = imie[2]
litera_2 = nazwisko[3]

tekst = "W tekście jest %d liter %s oraz %d liter %s"

liczba_liter1=tekst.__contains__(litera_1)
liczba_liter2=tekst.__contains__(litera_2)
print(tekst % (liczba_liter1,litera_1,liczba_liter2,litera_2))
