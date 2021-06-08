import plotly.graph_objects as go


def plotBar(datapoints, title, xlabel, ylabel):

    layout = go.Layout(title=title,
                       xaxis=dict(title=xlabel),
                       yaxis=dict(title=ylabel))
    color = "#6ded71"
    fig = go.Figure(layout=layout)

    fig.add_trace(go.Bar(x=datapoints.index, y=datapoints.values.flatten()))
    return fig


def plotGroupedBar(datapoints, names, title, xlabel, ylabel):

    layout = go.Layout(title=title,
                       xaxis=dict(title=xlabel),
                       yaxis=dict(title=ylabel))
    fig = go.Figure(layout=layout)
    for point, name in zip(datapoints, names):
        fig.add_trace(
            go.Bar(x=point.index, y=point.values.flatten(), name=name))
    return fig


def plotPie(labels, values, title):
    layout = go.Layout(title=title)
    fig = go.Figure(layout=layout)
    fig.add_trace(go.Pie(labels=labels, values=values, title='Genre', textinfo='label+percent', hole=0.2,
                         marker=dict(colors=['#f7d468', '#74cb35'],
                                     line_color='Gray',
                                     line_width=1),
                         textfont={'color': '#000', 'size': 12},
                         textfont_size=12))
    return fig


def plotLine(x, y, title, xlabel, ylabel, template="plotly_dark"):
    layout = go.Layout(title=title,
                       xaxis=dict(title=xlabel),
                       yaxis=dict(title=ylabel), template=template)
    fig = go.Figure(layout=layout)
    fig.add_trace(go.Line(x=x, y=y, line_color='#f63366'))
    return fig


def plotMultiLine(datapoints, title, xlabel, ylabel, template="plotly_dark"):
    layout = go.Layout(title=title,
                       xaxis=dict(title=xlabel),
                       yaxis=dict(title=ylabel), template=template)
    fig = go.Figure(layout=layout)

    for datapoint in datapoints:
        fig.add_trace(go.Line(x=datapoint.get('x'),
                              y=datapoint.get('y'), line_color='#f63366'))
    return fig


def plotHistogram(datapoints, title, xlabel, ylabel):
    layout = go.Layout(title=title,
                       xaxis=dict(title=xlabel),
                       yaxis=dict(title=ylabel))
    fig = go.Figure(layout=layout)

    fig.update_layout(template="ggplot2")
    fig.add_trace(go.Histogram(
        x=datapoints.values,
        # xbins = {'start': 1, 'size': 0.1, 'end' : 5}
    ))

    return fig


def plotScatter(data, x, y, color, title, template="plotly_dark"):
    fig = px.scatter(data_frame=data, x=x, y=y, color=color,
                     title=title, trendline="ols")

    fig.update_traces(marker=dict(symbol="diamond", size=10,
                                  line=dict(width=2,
                                            color='DarkSlateGrey')),
                      selector=dict(mode='markers'))
    fig.update_layout(width=1000, height=500, template=template)

    return fig
