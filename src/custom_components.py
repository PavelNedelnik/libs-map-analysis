import dash
import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
import dash_daq
from dash import dash_table

# TODO transform into objects

def place_in_container(component_body:list):
    return html.Div([
        dbc.Card(
            dbc.CardBody(
                component_body
            ),
            color = 'dark',
        )
    ])

def make_plot(map_header, idx, figure={}):
    return  place_in_container([
        map_header,
        dcc.Graph(
            id=idx,
            config={
                'displayModeBar': False
            },
            figure=figure,
        ),
    ])


def make_tooltip_title(title, idx, tooltip_text):
    return html.Div(
        [
            html.H4(
                [
                    html.Span(
                        title,
                        id=idx,
                        style={"textDecoration": "underline", "cursor": "pointer"},
                    ),
                ]
            ),
            dbc.Tooltip(
                tooltip_text,
                target=idx,
                id=idx + '_tooltip',
            ),
        ],
        className="card-title"
    )


# TODO labelPosition
def make_toggle(label_text, idx):
    return place_in_container(
        dash_daq.BooleanSwitch(id=idx, className='dbc', label=label_text, labelPosition="left")
    )


# TODO try adding a tooltip
def make_dropdown(idx, options):
    return place_in_container([
        dcc.Dropdown(
            options=options,
            value=options[0],
            id=idx,
            className="dbc", # to be compatible with dbc themes (it's dcc)
        )
    ])


def make_error_table(title, title_tooltip, idx):
    table = dbc.Table([], bordered=True, id=idx)

    return place_in_container([
            make_tooltip_title(title, 'table_title', title_tooltip),
            table,
        ])


def make_button(text, idx, color='secondary'):
    return place_in_container([ dbc.Button(text, id=idx, color=color, outline=True),])