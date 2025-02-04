import plotly.graph_objects as go
fig = go.Figure()
fig.add_trace(
    go.Scatter3d(
        x = [0,1,2,3],
        y = [0,1,2,3],
        z = [0,1,2,3],
        text = [9,8,7,6]
    )
)
fig.update_traces(
    hovertemplate='<br>x:%{x}\
                   <br>y:%{y}\
                   <br>z:%{z}\
                   <br>m:%{text}'
    )

fig.show()