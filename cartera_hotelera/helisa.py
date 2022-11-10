import pandas as pd

df = pd.read_excel("prueba.xlsx")

lista_criterio1 = list(df["Cuenta"])
lista_criterio2 = list(df["Nombre Centro de Costo"])
lista_criterio3 = list(df["Suma de Creditos"])

for i in range(len(df))::
    new = lista_criterio3[i].replace("-", "")
    print(i)


#all_debitos = [df.loc[(df['Cuenta'] == lista_criterio1[i]) & (df['Nombre Centro de Costo'] ==lista_criterio2[i]),"Suma de Debitos"].sum() for i in range(df.shape[0])]
#df["all_debitos"]=all_debitos

#all_creditos = [df.loc[(df['Cuenta'] == lista_criterio1[i]) & (df['Nombre Centro de Costo'] ==lista_criterio2[i]),"Suma de Creditos"].sum() for i in range(df.shape[0])]
#df["all_creditos"]=all_creditos

#df.to_csv('result.csv')

