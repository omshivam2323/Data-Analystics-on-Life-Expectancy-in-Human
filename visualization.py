import plotly.graph_objects as go

def plotBar(datapoints, title, xlabel, ylabel):
    
    layout = go.Layout(title= title,
                    xaxis=dict(title=xlabel),
                    yaxis=dict(title=ylabel))
    fig = go.Figure(layout = layout)
    
    fig.add_trace( go.Bar(x = datapoints.index,y= datapoints.values.flatten()))
    return fig

def plotPie(datapoints, title, xlabel, ylabel):
    
    layout = go.Layout(title= title,
                    xaxis=dict(title=xlabel),
                    yaxis=dict(title=ylabel))
    fig = go.Figure(layout = layout)
    
    fig.add_trace( go.Line(x = datapoints.index, y= datapoints.values.flatten()))
    return fig

def plotPie(labels, nums):
    fig = go.Figure()

    fig.add_trace( go.Pie( labels = labels , values = nums ) )

    return fig