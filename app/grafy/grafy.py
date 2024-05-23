#Zde by měly být funkce a pomocné funkce na vizualizaci grafů
import plotly.graph_objects as go

def test():
    fig = go.Figure(data=[go.Bar(x=['Category 1', 'Category 2', 'Category 3'], y=[10, 20, 30])])
    fig.update_layout(title='Example Graph with Data')
    return fig
