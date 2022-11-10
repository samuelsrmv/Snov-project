import json
import csv
from locale import currency

from numpy import Inf
from money import Money

def facturasResult(factura_cliente):
    info_facturas = {}
    text = '''
        <p>&nbsp;</p>
        <table style="color: #222222; font-family: Arial, Helvetica, sans-serif; font-size: small; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: #ffffff; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border-collapse: collapse; width: 100%;" border="0" width="100%" cellspacing="0" cellpadding="0">
        <colgroup>
        <col style="width: 65pt;" width="87" />
        <col style="width: 95pt;" width="127" />
        <col style="width: 55pt;" width="73" />
        <col style="width: 65pt;" width="87" />
        <col style="width: 105pt;" width="140" />
        <col style="width: 70pt;" width="93" />
        </colgroup>
        <tbody>
        <tr style="height: 20pt;">
            <td class="gmail-xl65" style="font-family: Calibri, sans-serif; margin: 0px; height: 20pt; width: 65pt; font-size: 12pt; color: white; font-weight: bold; border-width: 0.5pt 0.5pt 1pt; border-style: solid; border-color: #70ad47; background: #025a5a; text-align: center; padding-top: 1px; padding-right: 1px; padding-left: 1px; vertical-align: bottom; border-image: initial; white-space: nowrap;" width="87" height="27">NIT</td>
            <td class="gmail-xl65" style="font-family: Calibri, sans-serif; margin: 0px; width: 95pt; font-size: 12pt; color: white; font-weight: bold; border-width: 0.5pt 0.5pt 1pt; border-style: solid; border-color: #70ad47; background: #025a5a; text-align: center; padding-top: 1px; padding-right: 1px; padding-left: 1px; vertical-align: bottom; border-image: initial; white-space: nowrap;" width="127">Nombre Cliente</td>
            <td class="gmail-xl65" style="font-family: Calibri, sans-serif; margin: 0px; width: 55pt; font-size: 12pt; color: white; font-weight: bold; border-width: 0.5pt 0.5pt 1pt; border-style: solid; border-color: #70ad47; background: #025a5a; text-align: center; padding-top: 1px; padding-right: 1px; padding-left: 1px; vertical-align: bottom; border-image: initial; white-space: nowrap;" width="73">Factura</td>
            <td class="gmail-xl65" style="font-family: Calibri, sans-serif; margin: 0px; width: 65pt; font-size: 12pt; color: white; font-weight: bold; border-width: 0.5pt 0.5pt 1pt; border-style: solid; border-color: #70ad47; background: #025a5a; text-align: center; padding-top: 1px; padding-right: 1px; padding-left: 1px; vertical-align: bottom; border-image: initial; white-space: nowrap;" width="87">Fecha</td>
            <td class="gmail-xl65" style="font-family: Calibri, sans-serif; margin: 0px; width: 105pt; font-size: 12pt; color: white; font-weight: bold; border-width: 0.5pt 0.5pt 1pt; border-style: solid; border-color: #70ad47; background: #025a5a; text-align: center; padding-top: 1px; padding-right: 1px; padding-left: 1px; vertical-align: bottom; border-image: initial; white-space: nowrap;" width="140">Fecha Vencimiento</td>
            <td class="gmail-xl65" style="font-family: Calibri, sans-serif; margin: 0px; width: 70pt; font-size: 12pt; color: white; font-weight: bold; border-width: 0.5pt 0.5pt 1pt; border-style: solid; border-color: #70ad47; background: #025a5a; text-align: center; padding-top: 1px; padding-right: 1px; padding-left: 1px; vertical-align: bottom; border-image: initial; white-space: nowrap;" width="93">&nbsp;Edad Cartera&nbsp;</td>
            <td class="gmail-xl65" style="font-family: Calibri, sans-serif; margin: 0px; width: 70pt; font-size: 12pt; color: white; font-weight: bold; border-width: 0.5pt 0.5pt 1pt; border-style: solid; border-color: #70ad47; background: #025a5a; text-align: center; padding-top: 1px; padding-right: 1px; padding-left: 1px; vertical-align: bottom; border-image: initial; white-space: nowrap;" width="93">&nbsp;Total Cartera&nbsp;</td>
        </tr>
        '''
    file = open("template.html","w")
    file.write(text)
    file.close()
    value_amount = 0
    invoice_amount = 0
    number_invoices = 0
    current_inovices = 0
    expired_inovices = 0
    for index, factura in enumerate(factura_cliente):
        key_id = "f_id_{}".format(index + 1)
        info_facturas[key_id] = factura['Documento Afectado']
        key_fecha = "f_fecha_{}".format(index + 1)
        info_facturas[key_fecha] = factura['Fecha emision']
        key_identificacion_cliente = "f_identificacion_cliente_{}".format(index + 1)
        info_facturas[key_identificacion_cliente] = factura['Identificacion Cliente']
        key_nombre_cliente = "f_nombre_cliente_{}".format(index + 1)
        info_facturas[key_nombre_cliente] = factura['Nombre Cliente']
        key_fecha_vencimiento = "f_fecha_vencimiento_{}".format(index + 1)
        info_facturas[key_fecha_vencimiento] = factura['Fecha Vencimiento']
        key_saldo_total_cartera = "f_saldo_total_cartera_{}".format(index + 1)
        info_facturas[key_saldo_total_cartera] = factura['Suma de Saldo Total Cartera']
        key_edad_cartera = "f_edad_cartera_{}".format(index + 1)
        info_facturas[key_edad_cartera] = factura['Suma de Edad Cartera']
        invoice_amount = factura['Suma de Saldo Total Cartera'].replace('$', '').replace('.', '').replace(',', '.')
        value_amount += float(invoice_amount)
        number_invoices = number_invoices+1
        if int(info_facturas[key_edad_cartera]) <= 0:
            color = "#e2efda"
            current_inovices = current_inovices+1
        elif int(info_facturas[key_edad_cartera]) >= 1:
            color = "#f4cccc"
            expired_inovices = expired_inovices+1
        tex_facutra = f"""
                    <tr style="height: 16pt;">
                    <td class="gmail-xl69" style="font-family: Calibri, sans-serif; margin: 0px; font-size: 11pt; color: black; border: 0.5pt solid #70ad47; background: {color}; text-align: center; padding-top: 1px; padding-right: 1px; padding-left: 1px; vertical-align: bottom; white-space: nowrap;"><span style="caret-color: #000000; text-size-adjust: auto;">{factura['Identificacion Cliente']}</span></td>
                    <td class="gmail-xl69" style="font-family: Calibri, sans-serif; margin: 0px; font-size: 11pt; color: black; border: 0.5pt solid #70ad47; background: {color}; text-align: center; padding-top: 1px; padding-right: 1px; padding-left: 1px; vertical-align: bottom; white-space: nowrap;"><span style="caret-color: #000000; text-size-adjust: auto;">{factura['Nombre Cliente']}</span></td>
                    <td class="gmail-xl69" style="font-family: Calibri, sans-serif; margin: 0px; font-size: 11pt; color: black; border: 0.5pt solid #70ad47; background: {color}; text-align: center; padding-top: 1px; padding-right: 1px; padding-left: 1px; vertical-align: bottom; white-space: nowrap;"><span style="caret-color: #000000; text-size-adjust: auto;">{factura['Documento Afectado']}</span></td>
                    <td class="gmail-xl69" style="font-family: Calibri, sans-serif; margin: 0px; font-size: 11pt; color: black; border: 0.5pt solid #70ad47; background: {color}; text-align: center; padding-top: 1px; padding-right: 1px; padding-left: 1px; vertical-align: bottom; white-space: nowrap;"><span style="caret-color: #000000; text-size-adjust: auto;">{factura['Fecha emision']}</span></td>
                    <td class="gmail-xl69" style="font-family: Calibri, sans-serif; margin: 0px; font-size: 11pt; color: black; border: 0.5pt solid #70ad47; background: {color}; text-align: center; padding-top: 1px; padding-right: 1px; padding-left: 1px; vertical-align: bottom; white-space: nowrap;"><span style="caret-color: #000000; text-size-adjust: auto;">{factura['Fecha Vencimiento']}</span></td>
                    <td class="gmail-xl69" style="font-family: Calibri, sans-serif; margin: 0px; font-size: 11pt; color: black; border: 0.5pt solid #70ad47; background: {color}; text-align: center; padding-top: 1px; padding-right: 1px; padding-left: 1px; vertical-align: bottom; white-space: nowrap;"><span style="caret-color: #000000; text-size-adjust: auto;">{factura['Suma de Edad Cartera']}</span></td>
                    <td class="gmail-xl69" style="font-family: Calibri, sans-serif; margin: 0px; font-size: 11pt; color: black; border: 0.5pt solid #70ad47; background: {color}; text-align: center; padding-top: 1px; padding-right: 1px; padding-left: 1px; vertical-align: bottom; white-space: nowrap;"><span style="caret-color: #000000; text-size-adjust: auto;">{factura['Suma de Saldo Total Cartera']}</span></td>
                    </tr>
                    </colgroup>
                    <tbody>
                    """
        with open('template.html', 'a') as outfile:
            outfile.write(tex_facutra)
    total_amount = Money(amount=value_amount, currency='COP')
    info_facturas['total amount'] = total_amount
    tex_botton = f"""
                <td style="font-family: Calibri, sans-serif; margin: 0px; border: 0.5pt solid #70ad47; height: 15pt; color: white; font-weight: bold; text-align: center; background: #025a5a; padding-top: 1px; padding-right: 1px; padding-left: 1px; font-size: 12pt; vertical-align: bottom; white-space: nowrap;" colspan="6" height="20">CARTERA PENDIENTE</td>
                <td style="font-family: Calibri, sans-serif; margin: 0px; border-top: none; border-left: none; color: white; font-weight: bold; text-align: center; border-right: 0.5pt solid #70ad47; border-bottom: 0.5pt solid #70ad47; background: #025a5a; padding-top: 1px; padding-right: 1px; padding-left: 1px; font-size: 11pt; vertical-align: bottom; white-space: nowrap;">{total_amount}</td>
                """
    with open('template.html', 'a') as outfile:
        outfile.write(tex_botton)
    info_facturas['Numero total de facturas'] = number_invoices
    info_facturas['Numero de facturas corrientes'] = current_inovices
    info_facturas['Numero de facturas vencidas'] = expired_inovices
    
    return info_facturas
    

if __name__ == '__main__':
    facturasResult()



    