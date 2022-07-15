from plotly.offline import plot
import plotly.graph_objects as go


def integral_intensity(zscale, sum_p):
    trace = go.Scatter(x=zscale, y=sum_p)
    layout = dict(
        title='Интегральная интенсивность',
        xaxis=dict(range=[min(zscale), max(zscale)], title_text='x'),
        yaxis=dict(range=[min(sum_p), max(sum_p)], title_text='\u2211 <sub>\u03c4</sub> |U|<sup>2</sup>')
    )
    fig = go.Figure(data=[trace], layout=layout)
    plot_div = plot(fig, output_type='div', include_plotlyjs=False)
    return plot_div


def impulse_shape(tscale, res):
    trace1 = go.Scatter(x=tscale, y=res[0], name='Вход', line=dict(color='blue'))
    trace2 = go.Scatter(x=tscale, y=res[-1], name='Выход', line=dict(color='red'))
    layout = dict(
        title='Импульс на входе(синий) и на выходе(красный)',
        xaxis=dict(range=[min(tscale), max(tscale)], title_text='\u03c4'),
        yaxis=dict(title_text='|U|<sup>2</sup>')
    )
    fig = go.Figure(data=[trace1, trace2], layout=layout)
    plot_div = plot(fig, output_type='div', include_plotlyjs=False)
    return plot_div


def spectrum_shape(tscale, spres):
    N = len(tscale)
    trace1 = go.Scatter(
        x=tscale[int(N/2-80):int(N/2+80)],
        y=spres[0][int(N/2-80):int(N/2+80)],
        name='Вход',
        line=dict(color='blue')
    )
    trace2 = go.Scatter(
        x=tscale[int(N/2-80):int(N/2+80)],
        y=spres[-1][int(N/2-80):int(N/2+80)],
        name='Выход',
        line=dict(color='red')
    )
    layout = dict(
        title='Спектр на входе(синий) и на выходе(красный)',
        xaxis=dict(range=[min(tscale), max(tscale)], title_text='\u03c9'),
        yaxis = dict(title_text='|U|<sup>2</sup>')
    )
    fig = go.Figure(data=[trace1, trace2], layout=layout)
    plot_div = plot(fig, output_type='div', include_plotlyjs=False)
    return plot_div


def impulse(zscale, tscale, res):
    surface = go.Surface(
        x=tscale,
        y=zscale,
        z=res
    )
    layout = dict(
        title='Импульс',
    )
    fig = go.Figure(data=[surface], layout=layout)
    fig.update_layout(scene=dict(
        xaxis=dict(title_text='\u03c4'),
        yaxis=dict(title_text='x'),
        zaxis=dict(title_text='|U|<sup>2</sup>')
    ))
    plot_div = plot(fig, output_type='div', include_plotlyjs=False)
    return plot_div


def spectrum(omscale, zscale, spres):
    N = len(omscale)
    surface = go.Surface(
        x=omscale[int(N/2-80):int(N/2+80)],
        y=zscale,
        z=spres[:, int(N/2-80):int(N/2+80)]
    )
    layout = dict(
        title='Форма спектра импульса',
    )
    fig = go.Figure(data=[surface], layout=layout)
    fig.update_layout(scene=dict(
        xaxis=dict(title_text='\u03c9'),
        yaxis=dict(title_text='x'),
        zaxis=dict(title_text='|U|<sup>2</sup>')
    ))
    plot_div = plot(fig, output_type='div', include_plotlyjs=False)
    return plot_div