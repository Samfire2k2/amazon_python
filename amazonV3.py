import csv
import pandas as pd
 
df = pd.read_csv('bestsellers with categories.csv') 
df = pd.DataFrame(df)
colonne_annee = 'Year'
annees_uniques = df[colonne_annee].unique()

year = '2015'

#boucler pour avoir les donnees de 2015
for year in annees_uniques:
    df_year = df[df[colonne_annee] == 2015]
    df_year.to_csv(f'bestsellers_2015.csv', sep=',' ,index=False, encoding='utf-8')

print("Le traitement est fini.")
#print(annees_uniques)