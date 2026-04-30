import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

figure = px.pie(données, values='qte', names='region', title='quantité vendue par région')

figure.write_html('ventes-par-region.html')

print('ventes-par-région.html généré avec succès !')


ventes_produit = df.groupby("produit")["quantite"].sum().reset_index()

fig = px.bar(
    ventes_produit,
    x="produit",
    y="quantite",
    title="Ventes par produit"
)

fig.write_html("ventes-par-produit.html")


df["chiffre_affaires"] = df["quantite"] * df["prix"]

fig = px.bar(
    ca_produit,
    x="produit",
    y="chiffre_affaires",
    title="Chiffre d'affaires par produit"
)

fig.write_html("ca-par-produit.html")
