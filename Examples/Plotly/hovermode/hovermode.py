import plotly.graph_objects as go

# Dados de exemplo
x = [1, 2, 3, 4]
y = [10, 15, 7, 12]
labels = ['Ponto 1', 'Ponto 2', 'Ponto 3', 'Ponto 4']

# Criando o gráfico de dispersão
fig = go.Figure(data=go.Scatter(x=x, y=y, mode='markers', text=labels))

# Personalizando os rótulos flutuantes
fig.update_layout(
    hoverlabel=dict(
        bgcolor    = 'lightblue',
        bordercolor= 'black',
        font=dict(
            family= 'Arial', 
            size  = 20, 
            color = 'black'),
        align = 'left',
        namelength = 10,
    ),

)

# Exibindo o gráfico
fig.show()
