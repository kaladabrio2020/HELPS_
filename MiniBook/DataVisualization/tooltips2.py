from dash import Dash, dcc, html, Input, Output, no_update
import plotly.express as px

df = px.data.tips()
fig = px.histogram(df, x="sex", y="total_bill")

# Configurando o hovertemplate para todos os pontos
fig.update_traces(
    hovertemplate="<b>%{x}</b><br>Total: $%{y:.2f}<extra></extra>",
)

app = Dash(__name__)

app.layout = html.Div(
    children=[
        dcc.Graph(id="graph-3", figure=fig, clear_on_unhover=True),
        dcc.Tooltip(id="graph-tooltip-3", direction="bottom"),
    ],
    style={"height": 800, "padding": 50},
)

# Defina aqui o ponto específico para o qual você quer mostrar o tooltip personalizado
SPECIFIC_POINT = "Male"  # Por exemplo, apenas mostrar tooltip para "Male"

@app.callback(
    Output("graph-tooltip-3", "show"),
    Output("graph-tooltip-3", "bbox"),
    Output("graph-tooltip-3", "children"),
    Input("graph-3", "hoverData"),
)
def update_tooltip_content(hoverData):
    if hoverData is None:
        return False, no_update, no_update

    pt = hoverData["points"][0]	
    
    # Verificar se o ponto atual é o específico que queremos mostrar o tooltip personalizado
    if pt["x"] != SPECIFIC_POINT:
        return False, no_update, no_update
    
    bbox = pt["bbox"]
    dff = df[df.sex == pt["x"]]
    fig = px.bar(dff, x="day", y="total_bill", title=f"Total Bill by Day - {pt['x']}")
    children = [dcc.Graph(figure=fig, style={"height": 300})]

    return True, bbox, children


if __name__ == "__main__":
    app.run_server(debug=True)