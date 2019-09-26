import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

column1 = dbc.Col(
    [
        dcc.Markdown(
            """

            ## How this tool was created

            This predictive model was made using the Python library scikit-learn, and the interactive web app uses Plotly Dash and Heroku.

            The statistical model is a random forest regressor, a machine learning technique that understands data using a "wisdom of the crowd" approach. This means that it combines thousands of random samples from the data to create a generally accurate consensus of the target (in this case, camera prices).
            I chose this algorithm because it has a low risk of overfitting and is straightforward to use.
            There are a couple downsides. A random forest regressor cannot extrapolate to data outside the range of values it has seen, so the interactive tool can't imagine the price of a hypothetical 11MP camera in 1999.
            This model is also very difficult to interpret, in the sense that changes in values don't have a straightforward effect on the price like you might see from a linear regression model.
            So the best we can do to estimate those effects is to play with the sliders!



            """
        ),

    ],
)

layout = dbc.Row([column1])
