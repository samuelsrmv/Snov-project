import requests
import json
from find_prospect_by_email import getProspectsByEmail
from token_snov import get_access_token
from change_status_recipents import change_recipient_status
import csv

def resultLead():
    token = get_access_token()
    results = []
    with open('bd.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:        
            results.append(row)
    d = {} 
    for item in results:
        d.setdefault(item['Identificacion Cliente'], []).append(item)

    clientes = {}
    for cliente in d.keys():
        corriente = 0
        for item_ in d[cliente]:
            if int(item_['Suma de Edad Cartera']) <= 0:
                corriente = corriente+1

        if corriente == len(d[cliente]):
            estado = 1 #corriente
        elif corriente > 0 and corriente < len(d[cliente]):
            estado = 2 #corriente vencido
        elif corriente == 0 and len(d[cliente]) > 0:
            estado = 3 #vencido

        clientes[cliente] = {}
        clientes[cliente]['estado'] = estado
        clientes[cliente]['facturas'] = d[cliente]
        
        email = d[cliente][0]['email']
        status = getProspectsByEmail(email)
        #campaign_id = status['data'][0]['campaigns'][0]['id']
        
        print(clientes)

        #estado_csv = clientes[cliente]['estado']
        #estado_snov = status['data'][0]['locality']
        

        # if int(estado_csv) == int(estado_snov):
        #     print('El estado es igual')
        # elif estado_csv != estado_snov:
        #     #change_recipient_status(email, campaign_id)
        #     print('Es diferente')



if __name__ == '__main__':
    resultLead()