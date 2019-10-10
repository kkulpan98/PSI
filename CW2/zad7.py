tablica = []
tablica_2 = []
for i in range(10):
    tablica.append(i+1)
for i in range(5):
    tablica_2.append(tablica.pop())
tablica_2.sort()
tablica += tablica_2
tablica.insert(0, 0)
tablica = sorted(tablica, reverse=True)
print(tablica)
