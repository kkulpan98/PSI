tablica = []
tablica_2 = []
for i in range(10):
    tablica.append(i+1)
for i in range(5):
    tablica_2.append(tablica.pop())
print(tablica)
print(tablica_2)
