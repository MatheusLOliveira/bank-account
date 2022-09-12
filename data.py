from datetime import datetime
from locale import setlocale, LC_ALL

setlocale(LC_ALL, 'pt_BR.utf-8')

dt = datetime.now()
FORMATACAO = dt.strftime('%d/%m/%Y %H:%M:%S')
