import pandas as pd

benef_categorie_code = ['[PRS]', '[ETU]', '[FON]', '[VET]', '[PMO]', '[VPM]', '[APS]',
       '[AUS]', '[ETA]', '[PRE]', '[ADU]', '[LOG]', '[AGR]', '[SAN]']
categorie = ['Professionnel de santé', 'Etudiant',
       'Académies, Fondation, sociétés savantes, organismes de conseils',
       'Vétérinaire',
       'Personnes morales assurant la formation initiale ou continue des professionnels de santé',
       'Vétérinaire Personne Morale',
       'Association professionnel de santé',
       'Association usager de santé', 'Etablissement de santé',
       'Presse et média', "Association d'étudiants",
       'Editeur de logiciel', 'Groupement professionels agricoles',
       'Groupement sanitaire']

benef_qualite_code = ['[60]', '[10]', '[ADE]', '[21]', '[70]', '[50]', '[40]',
       '[01]', '[99]', '[82]', '[98]', '[94]', '[02]', '[86]', '[92]',
       '[96]', '[28]', '[95]', '[03]', '[04]', '[05]', '[91]', '[80]',
       '[EDP]']
qualite = ['Infirmier', 'Médecin', 'Assistant dentaire', 'Pharmacien',
       'Masseur-kinésithérapeute', 'Sage-femme', 'Chirurgien-dentiste',
       'Préparateur en pharmacie et préparateur en pharmacie hospitalière',
       'Physicien médical',
       'Prothésiste et orthésiste pour l’appareillage des personnes handicapées',
       'Manipulateur d’électroradiologie médicale', 'Ergothérapeute',
       'Aide soignant', 'Technicien de laboratoire médical',
       'Orthoptiste', 'Psychomotricien', 'Opticien-lunetier',
       'Diététicien', 'Auxiliaire de puériculture', 'Ambulancier',
       'Audioprothésiste', 'Orthophoniste', 'Pédicure-podologue',
       'Editeur de presse']

benef_pays_code = ['[FR]', '[PF]', '[RE]', '[NC]', '[MQ]', '[GP]', '[GF]',
       '[BE]', '[DZ]', '[MC]', '[TN]', '[CH]', '[GY]', '[YT]', '[CA]',
       '[NZ]', '[IT]', '[US]', '[LU]', '[TH]', '[AF]', '[SL]', '[SN]',
       '[MA]', '[IL]', '[TR]', '[MF]', '[GB]', '[ES]', '[DE]', '[GD]',
       '[BL]', '[CI]', '[BJ]', '[MG]', '[SY]', '[MR]', '[GR]', '[EG]',
       '[FI]', '[RU]', '[BG]', '[BF]', '[GN]', '[NL]', '[NA]', '[PM]',
       '[JP]', '[FJ]', '[BD]', '[ZA]', '[LB]', '[PT]', '[PR]', '[SV]',
       '[GU]', '[MU]', '[AD]', '[GE]', '[DJ]', '[MY]', '[MZ]', '[KW]',
       '[SM]', '[CG]', '[OM]', '[BR]', '[RO]', '[ML]', '[AR]', '[CM]',
       '[IN]', '[GA]', '[VN]', '[RS]', '[VE]', '[CN]', '[TG]', '[CD]',
       '[TD]', '[KH]', '[MO]', '[CZ]', '[PY]', '[ST]', '[CF]', '[AE]',
       '[GM]', '[NR]', '[CL]', '[EC]', '[TF]', '[PG]', '[AL]', '[DK]',
       '[MD]', '[SA]', '[DM]', '[HU]', '[IE]', '[SK]']
pays = ['FRANCE', 'POLYNÉSIE FRANÇAISE', 'RÉUNION',
       'NOUVELLE-CALÉDONIE', 'MARTINIQUE', 'GUADELOUPE',
       'GUYANE FRANÇAISE', 'BELGIQUE', 'ALGÉRIE', 'MONACO', 'TUNISIE',
       'SUISSE', 'GUYANA', 'MAYOTTE', 'CANADA', 'NOUVELLE-ZÉLANDE',
       'ITALIE', 'ÉTATS-UNIS', 'LUXEMBOURG', 'THAÏLANDE', 'AFGHANISTAN',
       'SIERRA LEONE', 'SÉNÉGAL', 'MAROC', 'ISRAËL', 'TURQUIE',
       'SAINT-MARTIN(PARTIE FRANÇAISE)', 'ROYAUME-UNI', 'ESPAGNE',
       'ALLEMAGNE', 'GRENADE', 'SAINT-BARTHÉLEMY', "CÔTE D'IVOIRE",
       'BÉNIN', 'MADAGASCAR', 'SYRIENNE, RÉPUBLIQUE ARABE', 'MAURITANIE',
       'GRÈCE', 'ÉGYPTE', 'FINLANDE', 'RUSSIE, FÉDÉRATION DE', 'BULGARIE',
       'BURKINA FASO', 'GUINÉE', 'PAYS-BAS', 'NAMIBIE',
       'SAINT-PIERRE-ET-MIQUELON', 'JAPON', 'FIDJI', 'BANGLADESH',
       'AFRIQUE DU SUD', 'LIBAN', 'PORTUGAL', 'PORTO RICO', 'EL SALVADOR',
       'GUAM', 'MAURICE', 'ANDORRE', 'GÉORGIE', 'DJIBOUTI', 'MALAISIE',
       'MOZAMBIQUE', 'KOWEÏT', 'SAINT-MARIN', 'CONGO', 'OMAN', 'BRÉSIL',
       'ROUMANIE', 'MALI', 'ARGENTINE', 'CAMEROUN', 'INDE', 'GABON',
       'VIET NAM', 'SERBIE', 'VENEZUELA, RÉPUBLIQUE BOLIVARIENNE DU',
       'CHINE', 'TOGO', 'CONGO, LA RÉPUBLIQUE DÉMOCRATIQUE DU', 'TCHAD',
       'CAMBODGE', 'MACAO', 'TCHÈQUE, RÉPUBLIQUE', 'PARAGUAY',
       'SAO TOMÉ-ET-PRINCIPE', 'CENTRAFRICAINE, RÉPUBLIQUE',
       'ÉMIRATS ARABES UNIS', 'GAMBIE', 'NAURU', 'CHILI', 'ÉQUATEUR',
       'TERRES AUSTRALES FRANÇAISES', 'PAPOUASIE-NOUVELLE-GUINÉE',
       'ALBANIE', 'DANEMARK', 'MOLDOVA, RÉPUBLIQUE DE', 'ARABIE SAOUDITE',
       'DOMINIQUE', 'HONGRIE', 'IRLANDE', 'SLOVAQUIE']

benef_titre_code = ['[DR]', '[PG]', '[PR]', '[MG]', '[AUTRE]', '[PC]', '[MC]']
benef_titre_libelle = ['Docteur', 'Pharmacien Général', 'Professeur',
       'Médecin Général', 'Autre', 'Pharmacien Chef', 'Médecin chef']

benef_specialite_code = ['[SM54]', '[SM40]', '[SM03]', '[SM26]', '[SM39]', '[SM44]',
       '[SM02]', '[SM08]', '[SM53]', '[AUTRE]', '[SM04]', '[SM31]',
       '[SM11]', '[SM12]', '[SM05]', '[SM16]', '[SM13]', '[SM14]',
       '[SM25]', '[SM32]', '[SM41]', '[SM20]', '[SM15]', '[SM35]',
       '[SM24]', '[SM38]', '[SM36]', '[SM48]', '[SM45]', '[SM21]',
       '[SM27]', '[SM30]', '[SM99]', '[SM01]', '[SM19]', '[SM23]',
       '[SM43]', '[SCD01]', '[SM18]', '[SM42]', '[SM28]', '[SM17]',
       '[SM37]', '[SM55]', '[SM06]', '[SCD02]', '[SM34]', '[SM22]',
       '[SM29]', '[SM10]', '[SCD03]', '[SP02]', '[SM46]', '[SM09]',
       '[SM49]', '[SM51]', '[SP03]', '[SM50]', '[SM07]', '[SM52]',
       '[SM47]', '[SP01]', '[SM33]', '[SP04]']
benef_specialite_libelle = ['Médecine Générale', 'Pédiatrie', 'Biologie médicale',
       'Qualifié en Médecine Générale', 'Oto-rhino-laryngologie',
       'Radio-diagnostic', 'Anesthesie-réanimation',
       'Chirurgie orthopédique et traumatologie',
       'Spécialiste en Médecine Générale', 'Autre',
       'Cardiologie et maladies vasculaires', 'Neuro-chirurgie',
       'Chirurgie thoracique et cardio-vasculaire',
       'Chirurgie urologique', 'Chirurgie générale',
       'Endocrinologie et métabolisme', 'Chirurgie vasculaire',
       'Chirurgie viscérale et digestive', 'Médecine du travail',
       'Neurologie', 'Pneumologie', 'Gynécologie-obstétrique',
       'Dermatologie et vénéréologie',
       'Oncologie (option onco-hématologie)',
       'Gastro-entérologie et hépatologie', 'Ophtalmologie',
       'Oncologie option médicale', 'Rhumatologie', 'Radio-thérapie ',
       'Hématologie', 'Médecine interne', 'Néphrologie',
       'ORL et ophtalmologie', 'Anatomie et cytologie pathologiques',
       'Gynécologie médicale', 'Hématologie (option Onco-hématologie)',
       'Psychiatrie option enfant & adolescent',
       'Orthopédie dento-faciale', 'Gériatrie', 'Psychiatrie',
       'Médecine nucléaire', 'Génétique médicale',
       'Oncologie option radiothérapie',
       'Radio-diagnostic et Radio-Thérapie', 'Chirurgie maxillo-faciale',
       'Chirurgie Orale', 'O.R.L et chirurgie cervico faciale',
       'Hématologie (option Maladie du sang)',
       'Médecine physique et réadaptation',
       'Chirurgie plastique reconstructrice et esthétique',
       'Médecine Bucco-Dentaire', 'Hygiène', 'Réanimation médicale',
       'Chirurgie infantile', 'Santé publique et médecine sociale',
       'Gynéco-obstétrique et gynécologie médicale option 1',
       'Pharmacovigilance', 'Stomatologie',
       'Chirurgie maxillo-faciale et stomatologie',
       'Gynéco-obstétrique et gynécologie médicale option 2',
       'Recherche médicale', 'Radio-pharmacie', 'Neuro-psychiatrie',
       'Hémovigilance']

benef_identifiant_type_code = ['[AUTRE]', '[RPPS]', '[ORDRE]', '[SIREN]', '[FINESS]']
identifiant_type = ['AUTRE', 'RPPS', 'ORDRE', 'SIREN', 'FINESS']

def lists_to_dict(list1, list2):
    res = {}
    if len(list1) != len(list2):
        print('ERROR : len of list1 and list2 is not equal : %s, %s'% (len(list1), len(list2)))
        return res
    for i in range(0, len(list1)):
        res.update({list1[i]:list2[i]})    
    return res    

codes = {}
codes.update({'categorie': lists_to_dict(benef_categorie_code, categorie)})
codes.update({'qualite': lists_to_dict(benef_qualite_code, qualite)})
codes.update({'pays': lists_to_dict(benef_pays_code, pays)})
codes.update({'titre': lists_to_dict(benef_titre_code, benef_titre_libelle)})
codes.update({'specialite': lists_to_dict(benef_specialite_code, benef_specialite_libelle)})
codes.update({'identifiant': lists_to_dict(benef_identifiant_type_code, identifiant_type)})

import json
with open('codes.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(codes))