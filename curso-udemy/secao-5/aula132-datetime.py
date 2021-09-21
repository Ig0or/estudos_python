from datetime import datetime
from locale import setlocale, LC_ALL
from calendar import mdays, monthrange

setlocale(LC_ALL, 'pt_br')

dt = datetime.now()

formatacao1 = dt.strftime('%A, %d de %B de %Y')
formatacao2 = dt.strftime('%d/%m/%Y %H:%M:%S')

print(formatacao1)
print(formatacao2)

mes_atual = int(dt.strftime('%m'))
print(mdays[mes_atual])

print(monthrange(2021, 9))