from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd


app = Dash(__name__)

df = pd.read_csv("data/daily_sales_data_2.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.groupby(["date", "price", "product", pd.Grouper(key = "date", freq = "M")], as_index = False)["quantity"].sum()
df = df.set_index("product")
df.rename(columns = {"date":"Date", "price":"Price", "product":"Product", "quantity":"Sales Volume"}, inplace = True )
df = df.loc["pink morsel"]

fig = px.line(df, x = "Date", y = "Sales Volume", color = "Price")

app.layout = html.Div(children=[
    html.H1(children='Soul Foods'),

    html.Div(children='''
        Sales before and after Pink Morsel price increase on the 15th January 2021.
    '''),

    dcc.Graph(
        id='pink-morsels',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
