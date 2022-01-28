import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

# The data
avocado = pd.read_csv("data/avocado.csv")


# Start of the Dash App
external_stylesheets = [
    dbc.themes.BOOTSTRAP
]

app = dash.Dash(
    __name__,
    external_stylesheets=external_stylesheets
)

app.title = "Registered Investment Advisors"

header = dbc.Navbar(
    dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        html.A(
                            html.Img(src=app.get_asset_url("logo.png")),
                            href="https://www.google.com"
                        )
                    ),
                    dbc.Col(
                        dbc.NavbarBrand("Advisor Roll App")
                    )
                ],
                align="center"
            )
        ],
        fluid=True
    ),
    color="dark",
    dark=True
)

plot1 = html.Div(
    children=dcc.Graph(
        id="price-chart",
        config={"displayModeBar": False},
        figure={
            "data": [
                {
                    "x": avocado["type"],
                    "y": avocado["AveragePrice"],
                    "type": "bar",
                    "hovertemplete": "%{y:.2f}" "<extra></extra>"
                }
            ],
            "layout": {
                "title": {
                    "text": "Average Price by Organic vs Conventional",
                    "x": 0.05,
                    "xanchor": "left"
                },
                "xaxis": {"fixedrange": True},
                "yaxis": {
                    "tickprefix": "",
                    "fixedrange": True
                },
                "colorway": ["#17B897"]
            }
        }
    ),
    className="card"
)

fig = px.line(avocado, x='Date', y="AveragePrice")

plot2 = html.Div(
    children=dcc.Graph(
        id="status-time-chart",
        config={"displayModeBar": False},
        figure=fig
    ),
    className="card"
)


# The bootstrap grid
dashboard = dbc.Container(
    [
        dbc.Row([
            dbc.Col(plot1),
            dbc.Col(plot2)
        ])
    ],
    fluid=False
)

app.layout = html.Div(
    children=[
        header,
        dashboard
    ]
)

# Expose flask instance
server = app.server


if __name__ == "__main__":

    app.run_server(
        debug=True,
        host="0.0.0.0",
        port=8080
    )
