import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app
import pandas as pd

from joblib import load
pipeline = load('assets/pipeline.joblib')

url = "https://raw.githubusercontent.com/strangelycutlemon/camera_prices/master/modified_camera_prices.csv"
df = pd.read_csv(url)

column1 = dbc.Col(
    [
        dcc.Markdown('## Camera Features', className='mb-5'),
        dcc.Markdown('#### Brand'),
        dcc.Dropdown(
            id='Brand',
            options = [
                {'label': 'Agfa','value': 'Agfa'},
                {'label': 'Canon','value': 'Canon'},
                {'label': 'Casio','value': 'Casio'},
                {'label': 'Contax','value': 'Contax'},
                {'label': 'Epson','value': 'Epson'},
                {'label': 'Fujifilm','value': 'Fujifilm'},
                {'label': 'HP','value': 'HP'},
                {'label': 'JVC','value': 'JVC'},
                {'label': 'Kodak','value': 'Kodak'},
                {'label': 'Kyocera','value': 'Kyocera'},
                {'label': 'Leica','value': 'Leica'},
                {'label': 'Nikon','value': 'Nikon'},
                {'label': 'Olympus','value': 'Olympus'},
                {'label': 'Panasonic','value': 'Panasonic'},
                {'label': 'Pentax','value': 'Pentax'},
                {'label': 'Ricoh','value': 'Ricoh'},
                {'label': 'Samsung','value': 'Samsung'},
                {'label': 'Sanyo','value': 'Sanyo'},
                {'label': 'Sigma','value': 'Sigma'},
                {'label': 'Sony','value': 'Sony'},
                {'label': 'Toshiba','value': 'Toshiba'}
            ],
            value = 'Canon',
            className='mb-5',
        ),
        dcc.Markdown('#### Release Year'),
        dcc.Slider(
            id='Release_date',
            min=1994,
            max=2007,
            step=1,
            value=2003,
            marks={n: str(n) for n in range(1994, 2007,2)},
            className='mb-5',
        ),
        dcc.Markdown('#### Maximum Resolution'),
        dcc.Slider(
            id='Max_resolution',
            min=0,
            max=5616,
            step=16,
            value=2400,
            marks={n: str(n) for n in range(0,5616,1024)},
            className='mb-5',
        ),
        dcc.Markdown('#### Lowest Resolution'),
        dcc.Slider(
            id='Low_resolution',
            min=0,
            max=5616,
            step=16,
            value=1770,
            marks={n: str(n) for n in range(0,5616,1024)},
            className='mb-5',
        ),
        dcc.Markdown('#### Zoom Wide'),
        dcc.Slider(
            id='Zoom_wide',
            min=0,
            max=52,
            step=1,
            value=33,
            marks={n: str(n) for n in range(0,52,4)},
            className='mb-5',
        ),
        dcc.Markdown('#### Zoom Tele'),
        dcc.Slider(
            id='Zoom_tele',
            min=0,
            max=518,
            step=20,
            value=121,
            marks={n: str(n) for n in range(0,518,50)},
            className='mb-5',
        ),

    ],
    md=4,
)



@app.callback(
    Output('out', 'children'),
    [Input('Release_date', 'value'), Input('Max_resolution', 'value'),
    Input('Low_resolution', 'value'), Input('Effective_pixels', 'value'),
    Input('Zoom_wide', 'value'), Input('Zoom_tele', 'value'),
    Input('Normal_focus_range', 'value'), Input('Macro_focus_range', 'value'),
    Input('Storage_included', 'value'), Input('Weight', 'value'),
    Input('Dimensions', 'value'), Input('Brand', 'value'),
    ]
)
def predict(Release_date, Max_resolution, Low_resolution, Effective_pixels, Zoom_wide, Zoom_tele, Normal_focus_range, Macro_focus_range, Storage_included, Weight, Dimensions, Brand):
    df = pd.DataFrame(
        columns=['Release_date',
                 'Max_resolution',
                 'Low_resolution',
                 'Effective_pixels',
                 'Zoom_wide',
                 'Zoom_tele',
                 'Normal_focus_range',
                 'Macro_focus_range',
                 'Storage_included',
                 'Weight',
                 'Dimensions',
                 'Brand'],
        data=[[Release_date,
               Max_resolution,
               Low_resolution,
               Effective_pixels,
               Zoom_wide,
               Zoom_tele,
               Normal_focus_range,
               Macro_focus_range,
               Storage_included,
               Weight,
               Dimensions,
               Brand]]
    )
    y_pred = pipeline.predict(df)[0]
    return("The price is ${}".format(y_pred))

column2 = dbc.Col(
    [
        dcc.Markdown('#### Effective MegaPixels'),
        dcc.Slider(
            id='Effective_pixels',
            min=0,
            max=21,
            step=0.5,
            value=5,
            marks={n: str(n) for n in range(0,21,3)},
            className='mb-5',
        ),
        dcc.Markdown('#### Normal Focus Range'),
        dcc.Slider(
            id='Normal_focus_range',
            min=0,
            max=120,
            step=5,
            value=44,
            marks={n: str(n) for n in range(0,120,10)},
            className='mb-5',
        ),
        dcc.Markdown('#### Macro Focus Range'),
        dcc.Slider(
            id='Macro_focus_range',
            min=0,
            max=85,
            step=5,
            value=7,
            marks={n: str(n) for n in range(0,85,10)},
            className='mb-5',
        ),
        dcc.Markdown('#### Storage Included (Gb)'),
        dcc.Slider(
            id='Storage_included',
            min=0,
            max=450,
            step=10,
            value=17,
            marks={n: str(n) for n in range(0,450,50)},
            className='mb-5',
        ),
        dcc.Markdown('#### Weight (Batteries inc.)'),
        dcc.Slider(
            id='Weight',
            min=0,
            max=1860,
            step=1,
            value=320,
            marks={n: str(n) for n in range(0,1860,200)},
            className='mb-5',
        ),
        dcc.Markdown('#### Dimensions'),
        dcc.Slider(
            id='Dimensions',
            min=0,
            max=240,
            step=1,
            value=105,
            marks={n: str(n) for n in range(0,240,24)},
            className='mb-5',
        ),
    ]
)

column3 = dbc.Col(
    [
        html.H2('Expected Price', className='mb-5'),
        html.Div(id='out', className='lead'),
        # dcc.Input(id='out', value='initial value', type='text')
        # html.Td(test_text)
    ]
)


layout = dbc.Row([column1, column2, column3])
