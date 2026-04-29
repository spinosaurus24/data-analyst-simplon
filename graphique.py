import pandas as pd
import plotly.express as px

# Création des données
df = pd.DataFrame({
    "produit": ["A", "B", "C"],
    "total_ventes": [17500, 15825, 11500]
})


# Graphique 1 : Barres

fig_bar = px.bar(
    df,
    x="produit",
    y="total_ventes",
    title="Ventes par produit"
)

# Sauvegarde du graphique
fig_bar.write_html("ventes-barres.html")


# Graphique 2 : Camembert

fig_pie = px.pie(
    df,
    names="produit",
    values="total_ventes",
    title="Répartition des ventes"
)

# Sauvegarde du graphique
fig_pie.write_html("ventes-camembert.html")

print("Les graphiques ont été générés avec succès.")
