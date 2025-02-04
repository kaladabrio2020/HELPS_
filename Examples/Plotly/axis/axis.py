import plotly.graph_objects as go

# Dados de exemplo
x = [1, 2, 3, 4]
y = [10, 15, 7, 12]

# Criando o gráfico de dispersão
fig = go.Figure(data=go.Scatter(x=x, y=y, mode='markers'))

# Personalizando os eixos x e y
fig.update_layout(
    xaxis=dict(
        title=dict(
            text = 'nome',
            font = dict(
                size  = 16,
                color = 'red'
            )
            
        ),
        type     = 'linear',  
        tickvals = [1, 2, 3, 4],  
        ticktext = ['A', 'B', 'C', 'D'],
        tickfont = dict(
            size = 15, 
            color='green'),  
        showgrid =True,  
        gridwidth=1,          
        gridcolor='lightgrey' 
    ),
    yaxis=dict(
        type  ='linear',  
        range =[0, 20],  
        tickfont = dict(
            size  = 10, 
            color ='purple'),  
        showgrid  = True, 
        gridwidth = 1,  
        gridcolor ='lightgrey'  
    )
)

# Exibindo o gráfico
fig.show()
