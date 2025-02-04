import plotly.graph_objects as go

fig = go.Figure()

for i in ['oi','oi2']:
    fig.add_traces(
        go.Scatter(
            x = [1,2,3,4],
            y = [e*len(i) for e in [1,2,4,9]],
            name=i
        )
    )
    
fig.update_layout(
    legend={
        'bgcolor'    :'purple',
        'bordercolor':'black',
        'borderwidth':20,
        'orientation':'h',
        'entrywidth':500,
        'entrywidthmode':'pixels',
        'visible':True,
        'traceorder':'grouped',
        'title':{
            'text':'rara',
            'font':{
                'size':16,
                'family':'arial',
                'color':'white'
            }
        },
        'font':{
            'size':16,
            'family':'arial',
            'color':'white'
        },
        'x':0.5,
        'y':0.5,
        'xanchor':'center',
        'yanchor':'bottom',
    },
    paper_bgcolor='red'

)
fig.show()
