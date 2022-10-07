import dash
import dash_bootstrap_components as dbc
from dash import html
from dash import dcc

def make_map(name, title):
    return  html.Div([
        dbc.Card(
            dbc.CardBody([
                html.H4(title, className="card-title"),
                dcc.Graph(
                    id=name,
                    config={
                        'displayModeBar': False
                    }
                ) 
            ])
        ),  
    ])


def make_dropdown(name, options):
    return dbc.Card(
        dbc.CardBody([
            dbc.Row([
                dbc.Col([
                    dcc.Dropdown(
                        options=options,
                        value=options[0],
                        id=name,
                        className="dbc", # to be compatible with dbc themes (it's a dcc component)
                    )
                ])
            ])
        ])
    )


def make_table():
    table_header = [
        html.Thead(html.Tr([html.Th("First Name"), html.Th("Last Name")]))
    ]

    row1 = html.Tr([html.Td("Arthur"), html.Td("Dent")])
    row2 = html.Tr([html.Td("Ford"), html.Td("Prefect")])
    row3 = html.Tr([html.Td("Zaphod"), html.Td("Beeblebrox")])
    row4 = html.Tr([html.Td("Trillian"), html.Td("Astra")])

    table_body = [html.Tbody([row1, row2, row3, row4])]

    table = dbc.Table(table_header + table_body, bordered=True)
    return table


def make_tooltip():
    return html.Div(
        [
            html.P(
                [
                    "I wonder what ",
                    html.Span(
                        "floccinaucinihilipilification",
                        id="tooltip-target",
                        style={"textDecoration": "underline", "cursor": "pointer"},
                    ),
                    " means?",
                ]
            ),
            dbc.Tooltip(
                "Noun: rare, "
                "the action or habit of estimating something as worthless.",
                target="tooltip-target",
            ),
        ]
    )


def make_slider(calibration):
    return  html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.RangeSlider(
                    min=calibration[0],
                    max=calibration[-1],
                    value=[calibration[0], calibration[-1]],
                    id='wavelength_slider',
                    tooltip={"placement": "bottom", "always_visible": True},
                    step=.2,
                    marks=None,
                )
            ])
        ),  
    ])


def make_spectra(name, title):
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    id=name,
                ) 
            ])
        ),  
    ])