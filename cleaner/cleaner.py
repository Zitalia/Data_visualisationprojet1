import pandas as pd

def clean(from_path, to_path, sep, to_dels):
    df = pd.read_csv(from_path, sep=sep)
    for to_del in to_dels:
        del df[to_del]
    df.to_csv(to_path, sep=sep, encoding='utf-8', index=False)

''' BENEF '''

# clean(
#     "data/benef.csv",
#     "data/clean/benef_clean.csv",
#     ';',
#     ['ligne_type', 'categorie', 'qualite', 'pays', 'benef_titre_libelle', 'benef_speicalite_libelle', 'identifiant_type'],
# )

''' CONV '''

# clean(
#   "data/conv.csv",
#   "data/clean/conv_clean.csv",
#   ';',
#   ['ligne_type', 'categorie', 'qualite', 'pays', 'benef_titre_libelle', 'benef_speicalite_libelle', 'identifiant_type']   
# )

''' REMU '''

# clean(
#   "data/remu.csv",
#   "data/clean/remu_clean.csv",
#   ';',
#   ['ligne_type', 'categorie', 'qualite', 'pays', 'benef_titre_libelle', 'benef_speicalite_libelle', 'identifiant_type']   
# )

''' ENTR '''

clean(
  "data/entreprise.csv",
  "data/clean/entreprise_clean.csv",
  ',',
  ['pays', 'secteur']   
)