import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

from app import app

"""
https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout

Layout in Bootstrap is controlled using the grid system. The Bootstrap grid has
twelve columns.

There are three main layout components in dash-bootstrap-components: Container,
Row, and Col.

The layout of your app should be built as a series of rows of columns.

We set md=4 indicating that on a 'medium' sized or larger screen each column
should take up a third of the width. Since we don't specify behaviour on
smaller size screens Bootstrap will allow the rows to wrap so as not to squash
the content.
"""

column1 = dbc.Col(
    [
        dcc.Markdown(
            """

            ## Understanding the Cost of Digital Camera Features

            This tool is an interactive predictive built using the features of over 1,000 digital cameras released from 1994 to 2007 (the year the iPhone was released).
            With it, you can estimate the cost of a camera from that time period with any features you specify.
            While it won't help you choose a digital camera today, it does illustrate which features were most costly during the heyday of digital cameras.

            """
        ),
        dcc.Link(dbc.Button('Try it out', color='primary'), href='/predictions')
    ],
    md=4,
)

url = "https://raw.githubusercontent.com/strangelycutlemon/camera_prices/master/cameras.csv"
gapminder = pd.read_csv(url)
fig = px.box(df, x='Brand', y='Price',
            #  color='Effective_pixels',
            #  notched=True,
             title ='Price by Digital Camera Brand',
             points='all')

column2 = dbc.Col(
    [
        dcc.Graph(figure=fig),
    ]
)

layout = dbc.Row([column1, column2])
