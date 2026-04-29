import pandas as pd
import plotly.express as px

df = pd.DataFrame({
    "produit": ["A", "B", "C"],
    "total_ventes": [17500, 15825, 11500]
})

fig = px.bar(df, x="produit", y="total_ventes", title="Ventes par produit")
fig.show()
