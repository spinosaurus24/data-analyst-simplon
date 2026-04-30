import plotly.express as px
import pandas as pd

# Charger les données
df = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

# Graphique existant (corrigé)
figure = px.pie(df, values='qte', names='region', title='quantité vendue par région')
figure.write_html('ventes-par-region.html')

print('ventes-par-région.html généré avec succès !')

# 1. VENTES PAR PRODUIT
ventes_produit = df.groupby("produit")["qte"].sum().reset_index()

fig = px.bar(
    ventes_produit,
    x="produit",
    y="qte",
    title="Ventes par produit"
)

fig.write_html("ventes-par-produit.html")

# 2. CHIFFRE D'AFFAIRES
df["chiffre_affaires"] = df["qte"] * df["prix"]

ca_produit = df.groupby("produit")["chiffre_affaires"].sum().reset_index()

fig = px.bar(
    ca_produit,
    x="produit",
    y="chiffre_affaires",
    title="Chiffre d'affaires par produit"
)

fig.write_html("ca-par-produit.html")