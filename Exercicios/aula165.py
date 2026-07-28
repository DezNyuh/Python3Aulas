from datetime import datetime
from dateutil.relativedelta import relativedelta

data = datetime.strptime('2020-12-20', '%Y-%m-%d')
valor_emprestimo = 1_000_000
valor_parcelado = valor_emprestimo / 60

for i in range(60):
    data += relativedelta(months=1)
    pagamento = data.strftime('%d/%m/%Y')
    valor = f'{valor_parcelado:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
    print(f'{pagamento} R$ {valor}')