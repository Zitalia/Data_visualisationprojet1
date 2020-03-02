import pandas as pd

df_benef = pd.read_csv("C:/Users/Utilisateur/Desktop/data_viz/data/benef.csv", sep=';')

to_dels = ['ligne_type', 'categorie', 'qualite', 'pays', 'benef_titre_libelle',
    'benef_speicalite_libelle', 'identifiant_type']

for to_del in to_dels:
    del df_benef[to_del]

print(df_benef.head())

df_benef.to_csv('benef_clean.csv', sep=';', encoding='utf-8')
