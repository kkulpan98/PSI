from datetime import datetime

person = {'first': 'Jean-Luc', 'last': 'Picard'}
print('{p[first]} {p[last]}'.format(p=person))

data = [4, 8, 15, 16, 23, 42]
print('{d[4]} {d[5]}'.format(d=data))

print('{:.{prec}} = {:.{prec}f}'.format('Gibberish', 2.7182, prec=3))

dt = datetime(2001, 2, 3, 4, 5)
print('{:{dfmt} {tfmt}}'.format(dt, dfmt='%Y-%m-%d', tfmt='%H:%M'))

print('{:{}{}{}.{}}'.format(2.7182818284, '>', '+', 10, 3))
