import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

# The data
avocado = pd.read_csv("data/avocado.csv")
avocado["Date"] = pd.to_datetime(avocado["Date"])
avocado.set_index("Date", inplace=True)

avocado_grpby_region = avocado.groupby(["region"])["Total Volume"].sum()
avocado_grpby_month = avocado.groupby(pd.Grouper(freq="M")).mean()



# Start of the Dash App
external_stylesheets = [
    dbc.themes.BOOTSTRAP
]

app = dash.Dash(
    __name__,
    external_stylesheets=external_stylesheets
)

app.title = "Avocado Price Research"

header = dbc.Navbar(
    dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        html.A(
                            html.Img(src=app.get_asset_url("logo.png")),
                            href="https://www.github.com/zjohn77/dataviz"
                        )
                    ),
                    dbc.Col(
                        dbc.NavbarBrand("The Avocado App")
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
                    "x": avocado_grpby_region.index,
                    "y": avocado_grpby_region,
                    "type": "bar",
                    "hovertemplete": "%{y:.2f}" "<extra></extra>"
                }
            ],
            "layout": {
                "title": {
                    "text": "Total Volume by Region",
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

plot2 = html.Div(
    children=dcc.Graph(
        id="date-chart",
        config={"displayModeBar": False},
        figure={
            "data": [
                {
                    "x": avocado_grpby_month.index,
                    "y": avocado_grpby_month["AveragePrice"],
                    "type": "line",
                    "hovertemplete": "%{y:.2f}" "<extra></extra>"
                }
            ],
            "layout": {
                "title": {
                    "text": "Average Price by Year",
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
# 
app.layout = html.Div(
    children=[
        header,
        dashboard
    ]
)

# Expose flask instance
server = app.server


if __name__ == "__main__":
    # print(avocado_grpby_region.head())
    app.run_server(
        debug=True,
        host="0.0.0.0",
        port=8080
    )
