import jinja2
import pdfkit


def create_pdf(path_template, info_facturas):
    nombre_template = path_template.split('/')[-1]
    path_template = path_template.replace(nombre_template, '')
    factura_name_r = "/Users/samuelmartinez/Documents/ayenda/mail_project/snov/pdf/facutra_{}.pdf".format(info_facturas['f_nombre_cliente_1'])
    factura_name = "facutra_{}.pdf".format(info_facturas['f_nombre_cliente_1'])

    env = jinja2.Environment(loader=jinja2.FileSystemLoader(path_template))
    template = env.get_template(nombre_template)
    info_facturas = template.render(info_facturas)
    config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')
    
    
    
    pdfkit.from_string(info_facturas, factura_name_r, configuration=config)
    return factura_name
    
    
    

if __name__ == "__main__":
    create_pdf()
    #ruta_template = '/Users/samuelmartinez/Documents/ayenda/mail_project/snov/pdf/template.info_facturas'
    #info = {"companyAyenda": "Ayenda SAS", "numeroFacturas": "varias"} 
    

