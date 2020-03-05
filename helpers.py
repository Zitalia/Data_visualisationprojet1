import unidecode, json

import numpy as np
import pandas as pd
import scipy as sp

cols_to_codes = {
    'benef_categorie_code': 'categorie',
    'benef_pays_code': 'pays',
    'benef_identifiant_type_code': 'identifiant',
    'benef_titre_code' : 'titre',
    'benef_specialite_code': 'specialite',
    'pays_code': 'pays',
    'secteur_activite_code': 'secteur'
}

with open('codes/codes.json', 'r', encoding='utf-8') as f:
    CODES = json.loads(f.read())

def normalize_label(s):
    s = s.split(' ')[0]
    s = s.split('/')[0]
    s = s.lower()
    s = unidecode.unidecode(s)
    s = s.replace('[', '')
    s = s.replace(']', '')
    s = s.replace(':', '')
    return s.strip()

def add_to_dict(_dict, key, value, add_if_not_exist=True):
    if key not in _dict.keys() and add_if_not_exist:
        _dict.update({key : 0})
        _dict[key] += value
        return 0
    else:
        _dict[key] += value
        return value

def simplify_column(df, key, title, irrelevant_value, irrelevant_label):
    to_plot = {}
    vcs = df[key].value_counts(normalize=True)
    
    c = 0
    for i in range(0, len(vcs)):
        c += vcs[i]
        
        label = normalize_label(str(vcs.axes[0][i]))
        add_to_dict(to_plot, label, vcs[i])

        if c > irrelevant_value:
            c -= add_to_dict(to_plot, label, vcs[i], False)
            
    add_to_dict(to_plot, irrelevant_label, 1-c)
    return to_plot

def show_at(df, id):
    row = []
    for col in df.columns:
        row.append('%s - %s' % (col, df[col][id]))
    print('\n'.join(row))

def from_remu(remu, conv, id):
    try:
        return conv[conv['ligne_identifiant'] == remu['remu_convention_liee'][id]].index[0]
    except:
        print( '%s - %s - %s' % (
            id, 
            remu['remu_convention_liee'][id],             
            conv[conv['ligne_identifiant'] == remu['remu_convention_liee'][id]].index)
        )

def translate(key, code):
    return CODES[cols_to_codes[key]][code]
    
def translate_list(key, codes):
    translated = []
    for code in codes:
        translated.append(translate(key, code))
    return translated
    
def arrange_to_plot(grouped):
    to_plot = {'labels' : [], 'values' : []}
    for item in grouped.items():
        to_plot['labels'].append(item[0])
        to_plot['values'].append(item[1])
    return to_plot

def chi2(quant, qual, bc):
    to_chi2 = pd.concat([pd.cut(quant, bc), qual],axis=1)
    quantk = to_chi2.columns[0] 
    qualk = to_chi2.columns[1]

    print("=== qual : %s and quant %s divide in %s ==="%(qualk, quantk, bc))
    
    IDS = []
    M = []
    for col in to_chi2[quantk].unique():
        IDS.append(col)
        M.append((list(to_chi2[to_chi2[quantk] == col].groupby([qualk]).count()[quantk])))

    print(pd.DataFrame(
        M, 
        index=list(to_chi2[quantk].unique()), 
        columns=list(to_chi2[qualk].unique())
    ).corr(method='pearson'))

    coeff_pearson = sp.stats.pearsonr(M[0], M[1])
    print('person for : %s - %s'%(IDS[0], IDS[1]))
    print(coeff_pearson)

def parse_date(date):
    if date[6] != '1' and date[7] == '9':
        return '%s0%s'%(date[:7], date[8:])
    if date[6] == '0' or date[6] == '1' and date[7] != '9':
        return '%s2%s'%(date[:6], date[7:])
    else: 
        return date

def parse_dates(df, key):
    df[key] = df[key].apply(parse_date)
    df[key] = pd.to_datetime(df[key], format='%d/%m/%Y')
