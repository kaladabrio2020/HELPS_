import plotly.graph_objects as go


fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x = [1,2,3,4],
        y = [1,2,4,9]
    )
)
fig.update_layout(
    title = {
        'text':'nome',
        'font':{
            'size':15,
            'family':'arial',
            'color':'red'
        },
        'x':0.5,
        'y':0.5,
        'xanchor':'center',
        'yanchor':'bottom',
        'automargin':True,
        'yref':'paper',
        'xref':'paper'
    }
    
)
fig.show()
