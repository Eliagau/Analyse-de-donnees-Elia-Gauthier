#coding:utf8

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

def listedesterritoires(territoiretest, exportationUSD, importationUSD):
    listedesterritoires = [[territoiretest[0], 0]]
    pos = 0
    for element in range(0,len(territoiretest)):
        if territoiretest[element] != listedesterritoires[pos][0]:
            listedesterritoires.append([territoiretest[element], element])
            pos += 1
    lignes = []
    for element in range(1,len(listedesterritoires)):
        lignes.append(listedesterritoires[element][1] - 1)
    lignes.append(len(territoiretest))
    liste = []
    for element in range(0,len(listedesterritoires)):
        liste.append([listedesterritoires[element][0], listedesterritoires[element][1], lignes[element]])
    totalparterritoire = []
    for element in range(0,len(liste)):
        totalparterritoire.append([liste[element][0], exportationUSD[liste[element][1]:liste[element][2]].sum(), importationUSD[liste[element][1]:liste[element][2]].sum()])
    return totalparterritoire

def nettoyage(colonne):
    colonne2 = []
    for element in colonne:
        if element == 'Sans objet' or element =='-':
            colonne2.append(float(0))
        else:
            colonne2.append(float(element))
    return colonne2

def getliste(territoiretest):
    listedesterritoires = [[territoiretest[0], 0]]
    pos = 0
    for element in range(0,len(territoiretest)):
        if territoiretest[element] != listedesterritoires[pos][0]:
            listedesterritoires.append([territoiretest[element], element])
            pos += 1
    lignes = []
    for element in range(1,len(listedesterritoires)):
        lignes.append(listedesterritoires[element][1] - 1)
    lignes.append(len(territoiretest))
    liste = []
    for element in range(0,len(listedesterritoires)):
        liste.append([listedesterritoires[element][0], listedesterritoires[element][1], lignes[element]])
    return liste


# Question 4
print("Question 4")
# Source des données : https://www.cepii.fr/CEPII/en/bdd_modele/bdd_modele_item.asp?id=37
with open("./data/Afrique-2024.csv", "r", encoding="utf-8") as fichier:
    contenu = pd.read_csv(fichier)

# Question 5
print("Question 5")
print(pd.DataFrame(contenu))

# Question 6
print("Question 6")
print("Nombre de lignes :", len(contenu))
print("Nombre de colonnes :", len(contenu.columns))

# Question 7
print("Question 7")
print(contenu.head())

# Question 8
print("Question 8")
print(contenu.dtypes)
types_colonnes = [
    int,  # year
    str,  # origin_id
    str,  # dest_id
    str,  # dist_VO (km)
    int,  # hs92_Section_id
    int,  # hs92_HS02_id
    int,  # hs92_HS04_id
    int,  # hs92_HS06_id
    int,  # export_val
    int,  # import_val
    str,  # export_ton
    str   # import_ton
]
print(types_colonnes)

# Contenu des colonnes
# "year" : année
# "origin_id" : territoire de référence
# "dest_id" : territoire partenaire
# "Dist_VO (km)" : distance intercentroïde entre les deux territoires
# "hs92_Section_id" : code Section du produit
# "hs92_HS02_id" : code 2-digit du produit
# "hs92_HS04_id" : code 4-digit du produit
# "hs92_HS06_id" : code 6-digit du produit
# "export_val" : valeur des exportations du territoire de référence vers le territoire partenaire en dollars courants
# "import_val" : valeur des importations du territoire partenaire vers le territoire de référence en dollars courants
# "export_ton" : valeur des exportations du territoire de référence vers le territoire partenaire en tonnes
# "import_ton" : valeur des importations du territoire partenaire vers le territoire de référence en tonnes

# Question 9
print("Question 9")
export_ton = contenu["export_ton"]
import_ton = contenu["import_ton"]

# Question 10
print("Question 10")

totaux = []

for colonne in [export_ton, import_ton]:
    total = 0
    for valeur in colonne:
        if str(valeur).strip() != "-":
            total += float(valeur)
    totaux.append(total)

print("Total des exportations en tonnes :", totaux[0])
print("Total des importations en tonnes :", totaux[1])

# Question 11
print("Question 11")

origin_id = contenu["origin_id"]
export_val = contenu["export_val"]
import_val = contenu["import_val"]

totalparterritoire = listedesterritoires(
    origin_id, export_val, import_val
)

print("Nombre de territoires :", len(totalparterritoire))
print("Exemple de totaux par territoire :")
print(totalparterritoire[:5])

# Création des diagrammes pour chaque territoire
for territoire in totalparterritoire:
    codeiso = territoire[0]
    exportations = territoire[1]
    importations = territoire[2]

    plt.figure()
    plt.bar(
        ["Exportations", "Importations"],
        [exportations, importations]
    )
    plt.title(codeiso)
    plt.ylabel("Valeur en dollars courants (USD)")
    plt.tight_layout()
    plt.savefig("./img/" + str(codeiso) + ".png")
    plt.close()

print("Les graphiques ont été enregistrés dans le dossier img.")

# Questions 12 et 14
print("Questions 12 et 14")

distance_2 = nettoyage(contenu["Dist_VO (km)"])
export_val_2 = nettoyage(contenu["export_val"])
import_val_2 = nettoyage(contenu["import_val"])
export_ton_2 = nettoyage(contenu["export_ton"])
import_ton_2 = nettoyage(contenu["import_ton"])

liste = getliste(contenu["origin_id"])

# Mettre le code nouveau DataFrame ici et appeler la liste donnees2

donnees2titre = [
    "distance",
    "export_val_2",
    "import_val_2",
    "export_ton_2",
    "import_ton_2"
]

donnees2 = pd.DataFrame({
    donnees2titre[0]: distance_2,
    donnees2titre[1]: export_val_2,
    donnees2titre[2]: import_val_2,
    donnees2titre[3]: export_ton_2,
    donnees2titre[4]: import_ton_2
})

print("Tableau donnees2 :")
print(donnees2.head())

# Compléter la boucle à partir des différents éléments précédents. Le nom des listes est celle proposée dans les commentaires.
# parametres = []
# quartiles = []
# deciles = []
# for element in range(0,len(donnees2.columns)):
#     parametres2 = []
#     distanceinterquartile = []
#     distanceinterdecile = []
#     for element2 in range(0,len(liste)):
#         codeiso = liste[element2][0]
#         data2 = donnees2.iloc[liste[element2][1]:liste[element2][2],element]

#         moyenne = 
#         mediane = 
#         mode = 
#         ecarttype = 
#         ecartabsolumoyen = 
#         etendue = 
#         parametres2.append([codeiso, moyenne, mediane, mode, ecarttype, ecartabsolumoyen, etendue])

#         quartile = 
#         distanceinterquartile.append([codeiso, (quartile[0.75] - quartile[0.25]).round(decimals=2)])
#         decile = 
#         distanceinterdecile.append([codeiso, (decile[0.9] - decile[0.1]).round(decimals=2)])
#     parametres.append(parametres2)
#     quartiles.append(distanceinterquartile)
#     deciles.append(distanceinterdecile)

parametres = []

for colonne in donnees2.columns:
    serie = donnees2[colonne]

    moyenne = serie.mean()
    mediane = serie.median()
    mode = serie.mode().iloc[0]
    ecart_type = serie.std()
    ecart_absolu = np.abs(serie - moyenne).mean()
    etendue = serie.max() - serie.min()

    moyenne = round(moyenne, 2)
    mediane = round(mediane, 2)
    mode = round(mode, 2)
    ecart_type = round(ecart_type, 2)
    ecart_absolu = round(ecart_absolu, 2)
    etendue = round(etendue, 2)

    parametres.append([
        colonne,
        moyenne,
        mediane,
        mode,
        ecart_type,
        ecart_absolu,
        etendue
    ])

print("Paramètres statistiques :")
for parametre in parametres:
    print(parametre)

# Question 13
print("Question 13")

# Question 14
print("Question 14")

distances_interquantiles = []

for colonne in donnees2.columns:
    serie = donnees2[colonne]

    q1 = serie.quantile(0.25)
    q3 = serie.quantile(0.75)
    distance_interquartile = q3 - q1

    d1 = serie.quantile(0.10)
    d9 = serie.quantile(0.90)
    distance_interdecile = d9 - d1

    distances_interquantiles.append([
        colonne,
        round(distance_interquartile, 2),
        round(distance_interdecile, 2)
    ])

print("Distances interquartiles et interdeciles :")
for resultat in distances_interquantiles:
    print(resultat)

# Question 15
print("Question 15")

for colonne in donnees2.columns:
    plt.figure()
    plt.boxplot(donnees2[colonne].dropna())
    plt.title("Boîte à moustaches : " + colonne)
    plt.ylabel(colonne)
    plt.tight_layout()
    plt.savefig("./img/boxplot_" + colonne + ".png")
    plt.close()

print("Les boîtes à moustaches ont été enregistrées dans le dossier img.")

# Question 16
print("Question 16")

distances = nettoyage(contenu["Dist_VO (km)"])

intervalles = [
    (0, 2500),
    (2500, 5000),
    (5000, 7500),
    (7500, 10000),
    (10000, 12500),
    (12500, 15000),
    (15000, 17500),
    (17500, 20000)
]

for borne_inf, borne_sup in intervalles:
    effectif = 0

    for distance in distances:
        if borne_inf < distance <= borne_sup:
            effectif += 1

    print(
        "Distances entre", borne_inf, "et", borne_sup,
        "km :", effectif
    )

# Question bonus
print("Question bonus")

noms_pays = pd.read_excel("data/country_names.xls")

print(noms_pays.head())
print(noms_pays.columns)

print(noms_pays[["id_3char", "name"]].head(10))
print(contenu[["origin_id", "dest_id"]].head(10))

noms_pays["id_3char"] = noms_pays["id_3char"].str.lower()

dictionnaire_pays = dict(
    zip(noms_pays["id_3char"], noms_pays["name"])
)

print(dictionnaire_pays.get("ago"))
print(dictionnaire_pays.get("abw"))

# Recréation des diagrammes circulaires avec les vrais noms des territoires
for territoire in totalparterritoire:
    codeiso = territoire[0]
    exportations = territoire[1]
    importations = territoire[2]

    nom_territoire = dictionnaire_pays.get(
        codeiso.lower(), codeiso
    )

    plt.figure()
    plt.pie(
        [exportations, importations],
        labels=["Exportations", "Importations"],
        autopct="%1.1f%%"
    )
    plt.title(nom_territoire)
    plt.tight_layout()
    plt.savefig("./img2/" + str(codeiso) + ".png")
    plt.close()

print("Les nouveaux diagrammes circulaires ont été enregistrés dans le dossier img2.")

# Export des listes au format CSV et Excel

# 1. Totaux par territoire
df_territoires = pd.DataFrame(
    totalparterritoire,
    columns=["Code ISO", "Exportations", "Importations"]
)

df_territoires.to_csv("./csv/totaux_territoires.csv", index=False)
df_territoires.to_excel("./xlsx/totaux_territoires.xlsx", index=False)


# 2. Statistiques descriptives
df_parametres = pd.DataFrame(
    parametres,
    columns=[
        "Variable",
        "Moyenne",
        "Médiane",
        "Mode",
        "Écart-type",
        "Écart absolu moyen",
        "Étendue"
    ]
)

df_parametres.to_csv("./csv/parametres.csv", index=False)
df_parametres.to_excel("./xlsx/parametres.xlsx", index=False)


# 3. Distances interquartiles et interdéciles
df_distances = pd.DataFrame(
    distances_interquantiles,
    columns=["Variable", "Distance interquartile", "Distance interdécile"]
)

df_distances.to_csv("./csv/distances_interquantiles.csv", index=False)
df_distances.to_excel("./xlsx/distances_interquantiles.xlsx", index=False)

print("Les fichiers CSV et Excel ont été enregistrés.")
