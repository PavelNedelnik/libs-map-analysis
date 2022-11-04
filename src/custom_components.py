import dash
import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
import dash_daq

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
            ),
        ],
        className="card-title"
    )


# TODO labelPosition
def make_toggle(label_false, label_true, idx):
    return place_in_container(
        dbc.Row([
            dbc.Col([comp]) for comp in [label_false, dash_daq.BooleanSwitch(id=idx, className='dbc'), label_true] if not isinstance(comp, str) or len(comp)
        ])
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


# TODO table body
def make_table(title, idx):
    # table header
    row1 = html.Tr([html.Td("Arthur"), html.Td("Dent")])
    row2 = html.Tr([html.Td("Ford"), html.Td("Prefect")])
    row3 = html.Tr([html.Td("Zaphod"), html.Td("Beeblebrox")])
    row4 = html.Tr([html.Td("Trillian"), html.Td("Astra")])

    table_body = [html.Tbody([row1, row2, row3, row4])]

    table = dbc.Table(table_body, bordered=True)

    return place_in_container([
            make_tooltip_title(title, 'table_title', 'TBD'),
            table,
        ])