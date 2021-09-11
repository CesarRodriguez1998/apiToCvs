import requests
import pandas as pd
import cerberus
import cerberus.validator
import json

print("Solicitando informacion")
print("espere....") 
URL = 'https://www.datos.gov.co/resource/t9rj-u779.json' 

Covid19 = requests.get(URL)
Covid19 = Covid19.json()

data = pd.read_json('https://www.datos.gov.co/resource/t9rj-u779.json')
df = pd.DataFrame(data)
df.to_csv(r'/home/KratosGOD/datosCovid19.csv', index = None)