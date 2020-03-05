import sys, os
import pandas as pd
import helpers

remu_path = 'data/clean/remu_clean.csv'
remu_categories = ['ligne_rectification', 'benef_categorie_code', 'benef_qualite_code', 'benef_pays_code', 
    'benef_titre_code', 'benef_specialite_code', 'benef_identifiant_type_code']

conv_path = 'data/clean/conv_clean.csv'
conv_categories = ['ligne_rectification', 'benef_categorie_code', 'benef_qualite_code', 'benef_pays_code', 
    'benef_titre_code', 'benef_specialite_code', 'benef_identifiant_type_code', 'conv_objet']

benef_path = 'data/clean/benef_clean.csv'
benef_categories = ['ligne_rectification', 'benef_categorie_code', 'benef_qualite_code', 'benef_pays_code', 
    'benef_titre_code', 'benef_specialite_code', 'benef_identifiant_type_code', 'semestre']

entr_path = 'data/clean/entreprise_clean.csv'
entr_categories = [
    'pays_code', 'secteur_activite_code'
]
# ['benef_categorie_code', 'benef_pays_code', 'benef_identifiant_type_code', 'benef_titre_code', 'benef_specialite_code']

def load_short_entr():
    cols = ['pays_code', 'secteur_activite_code']
    df = pd.read_csv(
        'data/entr_short.csv', sep=',', 
        encoding='utf-8', low_memory=False)

    for col in cols:
        df[col] = df[col].astype('category')

    df['remu_date'] = pd.to_datetime(df['remu_date'], format='%Y-%m-%d')

    return df

def load_short_remu():
    cols = ['benef_categorie_code', 'benef_pays_code', 'benef_identifiant_type_code', 'benef_titre_code', 'benef_specialite_code']
    df = pd.read_csv(
        'data/remu_short.csv', sep=';', 
        encoding='utf-8', low_memory=False)

    for col in cols:
        df[col] = df[col].astype('category')
        
    df['remu_date'] = pd.to_datetime(df['remu_date'], format='%Y-%m-%d')
    return df
    
def load_all():
    return (load_benef(), load_conv(), load_remu(), load_entr())

def load_benef():
    return load(benef_path, benef_categories)

def load_conv():
    return load(conv_path, conv_categories)

def load_remu():
    return load(remu_path, remu_categories)

def load_entr():
    return load(entr_path, entr_categories, sep=',')

def load(path, cats, sep=';'):
    df = pd.read_csv(path, sep=sep, encoding='utf-8', low_memory=False)
    for cat in cats:
        df[cat] = df[cat].astype('category')
    return df
