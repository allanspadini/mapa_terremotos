import marimo

__generated_with = "0.11.10"
app = marimo.App(width="medium", auto_download=["html"])


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md("""# Mapa terremotos""")
    return


@app.cell
def _():
    import pandas as pd
    import plotly.express as px
    import plotly.graph_objects as go
    return go, pd, px


@app.cell
def _(pd):
    df = pd.read_csv('https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_day.csv')
    return (df,)


@app.cell
def _(df, go, mo):
    # Definir o layout da figura
    fig = go.Figure()

    fig.update_layout(
        title=dict(
            text="Total de eventos",
            font=dict(
                family="Arial, sans-serif",
                size=16,
                color="black"
            ),
            x=0.5,  # Centralizar o título
            y=0.9   # Posicionar o título um pouco abaixo do topo
        ),
        # Tamanho do card (em pixels)
        width=200,
        height=200,
    
        # Cor de fundo
        paper_bgcolor='#A7C7E7',
    
        # Remover margens para maximizar o espaço
        margin=dict(l=10, r=10, t=10, b=10),
    
        # Remover eixos e grid
        xaxis=dict(
            showgrid=False,
            zeroline=False,
            showticklabels=False,
            visible=False
        ),
        yaxis=dict(
            showgrid=False,
            zeroline=False,
            showticklabels=False,
            visible=False
        )
    )

    # Adicionar o texto centralizado
    fig.add_annotation(
        text=str(len(df)),
        xref="paper", yref="paper",
        x=0.5, y=0.5,
        showarrow=False,
        font=dict(
            family="Arial, sans-serif",
            size=24,
            color="black"
        )
    )

    # Criar o plot usando mo.ui.plotly
    plot2 = mo.ui.plotly(fig)

    # Exibir o plot
    plot2

    return fig, plot2


@app.cell
def _(df, mo, px):
    plot = mo.ui.plotly(px.scatter_mapbox(
        df, 
        lat="latitude", 
        lon="longitude", 
        size="mag",  # Tamanho dos círculos baseado na magnitude
        color="mag",  # Cor baseada na magnitude
        hover_name="place",  # Nome ao passar o mouse
        hover_data=["time", "mag", "depth"],  # Dados adicionais no hover
        color_continuous_scale="Reds",  # Escala de cores vermelhas
        size_max=15,  # Tamanho máximo dos círculos
        zoom=1,  # Nível de zoom inicial
        center={"lat": -15.77, "lon": -47.94},  # Centro do mapa (mesmo do seu código)
        mapbox_style="carto-darkmatter"  # Estilo do mapa similar ao 'cartodbdark_matter'
    ))

    plot
    return (plot,)


@app.cell
def _(mo):
    mo.md("""Fonte de dados: USGS: https://www.usgs.gov/programs/earthquake-hazards""")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
