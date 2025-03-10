from dash import Dash, dcc, html, Input, Output, no_update
import plotly.express as px

df = px.data.tips()
fig = px.histogram(df, x="sex", y="total_bill")
fig.update_traces(
    hoverinfo="none",
    hovertemplate=None,
)

app = Dash(__name__)

app.layout = html.Div(
    children=[
        dcc.Graph(id="graph-3", figure=fig, clear_on_unhover=True),
        dcc.Tooltip(id="graph-tooltip-3", direction="bottom"),
    ],
    style={"height": 800, "padding": 50},
)


@app.callback(
    Output("graph-tooltip-3", "show"),
    Output("graph-tooltip-3", "bbox"),
    Output("graph-tooltip-3", "children"),
    Input("graph-3", "hoverData"),
)
def update_tooltip_content(hoverData):
    if hoverData is None:
        return no_update

    pt = hoverData["points"][0]
    bbox = pt["bbox"]
    dff = df[df.sex == pt["x"]]
    fig = px.bar(dff, x="day", y="total_bill", title=f"Total Bill by Day - {pt['x']}")
    children = [dcc.Graph(figure=fig, style={"height": 300})]

    return True, bbox, children


if __name__ == "__main__":
    app.run_server(debug=True)