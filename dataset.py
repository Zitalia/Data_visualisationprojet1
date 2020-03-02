import pandas as pd


benef_categories = ['ligne_rectification', 'benef_categorie_code', 'benef_qualite_code', 'benef_pays_code', 
    'benef_titre_code', 'benef_specialite_code', 'benef_identifiant_type_code', 'semestre']

def load_benef():
    df = pd.read_csv('benef_clean.csv', sep=';', encoding='utf-8')
    for cat in benef_categories:
        df[cat].astype('category')
    return df

