from heapq import merge
from operator import index
from sqlite3 import paramstyle
import requests
import json
import csv
from token_snov import get_access_token
from find_prospect_by_email import getProspectsByEmail
from change_status_recipents import change_recipient_status
from facturas import facturasResult
from create_pdf import create_pdf
from googledrive import googledriveAPI


def add_prospect_to_list():
    path_template = '/Users/samuelmartinez/Documents/ayenda/mail_project/snov/template.html'
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
        list_ids = {1:'11925770',  2: '11925775', 3: '11925773'}
        email = d[cliente][0]['email']
        status = getProspectsByEmail(email)


        factura_cliente = clientes[cliente]['facturas']
        factura_cliente.sort(key=lambda item:item['Suma de Edad Cartera'], reverse=False)
        info_facturas = facturasResult(factura_cliente)
        result_facturas = create_pdf(path_template, info_facturas)
        result_drive = googledriveAPI(result_facturas)
        link_drive = result_drive['webViewLink']

        try:
            if status['success'] == True:
                campaigns = status['data'][0]['campaigns']
                estado_csv = clientes[cliente]['estado']
                #estado_snov = status['data'][0]['locality']

                campaigns_ids = {851520: 1, 851549: 2, 851540: 3}

                for campaign in campaigns:
                    campaign_id = campaign['id']
                    try:
                        if estado_csv == campaigns_ids[campaign['id']]:
                            status_campaing = "Active"
                        else:
                            status_campaing = "Paused"
                        
                        change_recipient_status(email, campaign_id, status_campaing)
                    except: 
                        print('Id de campañana no encontrado')

                invoice_ = info_facturas['Numero total de facturas']
                current_invoice = info_facturas['Numero de facturas corrientes']
                expired_inovices = info_facturas['Numero de facturas vencidas']
                if info_facturas['Numero total de facturas'] == 1:
                    invoice_ = str(info_facturas['Numero total de facturas']) + " factura"
                    current_invoice = str(info_facturas['Numero de facturas corrientes']) + " factura"
                    expired_inovices = str(info_facturas['Numero de facturas vencidas']) + " factura" 
                elif info_facturas['Numero total de facturas'] > 1:
                    invoice_ = str(info_facturas['Numero total de facturas']) + " facturas"
                    if info_facturas['Numero de facturas corrientes'] > 1:
                        current_invoice = str(info_facturas['Numero de facturas corrientes']) + " facturas"
                        if info_facturas['Numero de facturas vencidas'] > 1:
                            expired_inovices = str(info_facturas['Numero de facturas vencidas']) + " facturas"
                        else:
                            expired_inovices = str(info_facturas['Numero de facturas vencidas']) + " factura"
                        
                    elif info_facturas['Numero de facturas vencidas'] > 1:
                        expired_inovices = str(info_facturas['Numero de facturas vencidas']) + " facturas"
                        if info_facturas['Numero de facturas corrientes'] > 1:
                            current_invoice = str(info_facturas['Numero de facturas corrientes']) + " facturas"
                        else:
                            current_invoice = str(info_facturas['Numero de facturas corrientes']) + " factura"
                    
                                
                params = {'access_token':token,
                        'email': d[cliente][0]['email'],
                        'fullName': d[cliente][0]['Nombre Cliente'].title(),
                        #'firstName':row['first name'],
                        #'lastName':row['last name'],
                        'country':'United States',
                        'locality': clientes[cliente]['estado'],
                        'position':'Civil Engineer',
                        'companyName':d[cliente][0]['Nombre Cliente'],
                        'companySite':'https://goldenrule.com',
                        'updateContact':1,
                        'customFields[number_invoices]': invoice_,
                        'customFields[current_inovices]': current_invoice,
                        'customFields[expired_inovices]': expired_inovices,
                        'customFields[total_amount]': info_facturas['total amount'],
                        'customFields[link_factura]': link_drive,
                        'listId':list_ids[clientes[cliente]['estado']], 
                    }

                res = requests.post('https://api.snov.io/v1/add-prospect-to-list', data=params)
                print(res)
                print(f"Cliente {cliente} agregado")

            else:
                invoice_ = info_facturas['Numero total de facturas']
                current_invoice = info_facturas['Numero de facturas corrientes']
                expired_inovices = info_facturas['Numero de facturas vencidas']
                
                if info_facturas['Numero total de facturas'] == 1:
                    invoice_ = str(info_facturas['Numero total de facturas']) + " factura"
                    current_invoice = str(info_facturas['Numero de facturas corrientes']) + " factura"
                    expired_inovices = str(info_facturas['Numero de facturas vencidas']) + " factura" 
                elif info_facturas['Numero total de facturas'] > 1:
                    invoice_ = str(info_facturas['Numero total de facturas']) + " facturas"
                    if info_facturas['Numero de facturas corrientes'] > 1:
                        current_invoice = str(info_facturas['Numero de facturas corrientes']) + " facturas"
                        if info_facturas['Numero de facturas vencidas'] > 1:
                            expired_inovices = str(info_facturas['Numero de facturas vencidas']) + " facturas"
                        else:
                            expired_inovices = str(info_facturas['Numero de facturas vencidas']) + " factura"
                        
                    elif info_facturas['Numero de facturas vencidas'] > 1:
                        expired_inovices = str(info_facturas['Numero de facturas vencidas']) + " facturas"
                        if info_facturas['Numero de facturas corrientes'] > 1:
                            current_invoice = str(info_facturas['Numero de facturas corrientes']) + " facturas"
                        else:
                            current_invoice = str(info_facturas['Numero de facturas corrientes']) + " factura"

                params = {'access_token':token,
                        'email': d[cliente][0]['email'],
                        'fullName': d[cliente][0]['Nombre Cliente'].title(),
                        # 'firstName':row['first name'],
                        # 'lastName':row['last name'],
                        'country':'United States',
                        'locality': clientes[cliente]['estado'],
                        'position':'Corporate',
                        'companyName':d[cliente][0]['Nombre Cliente'],
                        'companySite':'https://goldenrule.com',
                        'updateContact':1,
                        'customFields[number_invoices]': invoice_,
                        'customFields[current_inovices]': current_invoice,
                        'customFields[expired_inovices]': expired_inovices,
                        'customFields[total_amount]': info_facturas['total amount'],
                        'customFields[link_factura]': link_drive, 
                        'listId':list_ids[clientes[cliente]['estado']], 
                    }

                res = requests.post('https://api.snov.io/v1/add-prospect-to-list', data=params)
                print(res)
                print(f"Cliente {cliente} agregado")
        except:
            continue

if __name__ == '__main__':
    add_prospect_to_list()