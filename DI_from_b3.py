import json
from datetime import datetime
import requests

# -- setup

URL = 'https://www2.cetip.com.br/' + 'ConsultarTaxaDi/ConsultarTaxaDICetip.aspx'

# -- extract
try:
    response = requests.get(URL)
    response.raise_for_status()
except Exception as exc:
    raise exc
else:
    data = json.loads(response.text)
    print(f'1 - {data}')

# -- transform
data['taxa'] = data['taxa'].replace(',', '.')
data['indice'] = data['indice'].replace('.', '').replace(',', '.')

data['dataTaxa'] = datetime.strptime(data['dataTaxa'], '%d/%m/%Y').strftime('%Y-%m-%d')
data['dataIndice'] = datetime.strptime(data['dataIndice'], '%d/%m/%Y').strftime('%Y-%m-%d')
data['dataReferencia'] = datetime.now().strftime('%Y-%m-%d')

data_csv = ','.join([v for v in data.values()])

print(f'2 - {data}')
print(f'3 - {data_csv}')