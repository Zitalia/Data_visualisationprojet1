import pandas as pd 


#df_remu = pd.read_csv('c:/Users/Utilisateur/Videos/python/semaine8projet1/data_viz/data/remu.csv',error_bad_lines= False, sep=',', low_memory=False)
df_benef = pd.read_csv('c:/Users/Utilisateur/Videos/python/semaine8projet1/data_viz/data/conv.csv',error_bad_lines= False, sep=',', low_memory=False)
# x =['[APS]' '[PMO]' '[PRS]' '[PRE]' '[VET]' '[VPM]' '[FON]' '[ETA]' '[ETU]' '[AUS]' '[ADU]' '[SAN]' '[LOG]' '[AGR]']
# y = ['[PRS]' '[ETU]' '[APS]' '[ETA]' '[FON]' '[PRE]' '[AUS]' '[PMO]' '[VET]''[VPM]' '[SAN]' '[AGR]' '[LOG]' '[ADU]']
# ok = 0
# bad = 0
# print(df_remu.head())
# for index, rowremu in df_remu.iterrows():
#     for index, rowbenef in df_benef.iterrows():
#         if rowremu['entreprise_identifiant']== rowbenef['entreprise_identifiant']:
#             if rowremu['categorie']== rowbenef['categorie']:
#                 ok+=1
#             else:
#                 bad +=1

# print(ok, ' / ', bad)

print(df_benef['conv_date_signature'].unique())   