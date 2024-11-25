from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import dash
import pandas as pd
import os

from src.dash1 import generate_visualizations as generate_visualizations1
#from src.dash2 import generate_visualizations as generate_visualizations2
from src.dash3 import generate_visualizations as generate_visualizations3
from src.dash4 import generate_visualizations as generate_visualizations4

# Estilo de la tarjeta
tab_style = {
    'idle':{
        'borderRadius': '10px',
        'padding': '0px',
        'marginInline': '5px',
        'display':'flex',
        'alignItems':'center',
        'justifyContent':'center',
        'fontWeight': 'white',
        'backgroundColor': '#E52421',
        'border':'none'
    },
    'active':{
        'borderRadius': '12px',
        'padding': '0px',
        'marginInline': '5px',
        'display':'flex',
        'alignItems':'center',
        'justifyContent':'center',
        'fontWeight': 'bold',
        'border':'none',
        'textDecoration': 'underline',
        'backgroundColor': '#E52421'
    }
}
# Ruta para la carpeta de imágenes
static_folder = os.path.join(os.path.dirname(__file__), "assets")

# Configurar la aplicación Dash con la carpeta de assets personalizada
app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True,
    title='Fundacion2050',
    assets_folder=static_folder  # Configurar carpeta de assets
)

server = app.server

app.layout = html.Div([
    dbc.Container([
        # Fila para el logo y las Tabs
        dbc.Row([
            # Logo centrado en una fila
            dbc.Col(html.Img(src="/assets/Logo_mtp.png", width=850, height=100), width=12, style={'display': 'flex', 'justifyContent': 'center', 'marginBottom': '30px'}),

            # Tabs centrados en una fila
            dbc.Col(
                dcc.Tabs(id='graph-tabs', value='Main', children=[
                    dcc.Tab(label='Encuestas', value='Encuestas', style={**tab_style['idle'], 'color': 'white'}, selected_style={**tab_style['active'], 'color': 'white'}),
                    dcc.Tab(label='Relatorias', value='Relatorias', style={**tab_style['idle'], 'color': 'white'}, selected_style={**tab_style['active'], 'color': 'white'}),
                    dcc.Tab(label='Analisis de Sentimientos', value='Sentimientos', style={**tab_style['idle'], 'color': 'white'}, selected_style={**tab_style['active'], 'color': 'white'}),
                    dcc.Tab(label='Centralidad del Debate', value='Debate', style={**tab_style['idle'], 'color': 'white'}, selected_style={**tab_style['active'], 'color': 'white'})
                ], style={'marginTop': '15px', 'height': '50px', 'width': '100%'})
            , width=12, style={'display': 'flex', 'justifyContent': 'center'}),  # Centrado de los tabs
        ]),

        # Título y texto entre las Tabs y los gráficos
        dbc.Row([
            dbc.Col(html.H1("META ASAMBLEA CIUDADANA DELIBERATIVA", style={'textAlign': 'center', 'fontSize': '40px', 'fontWeight': 'bold'}), width=12),
        ], justify='center', style={'marginTop': '30px'}),

        dbc.Row([
            dbc.Col(html.H3("Bogotá 2024", style={'textAlign': 'center', 'fontSize': '30px'}), width=12),
        ], justify='center', style={'marginTop': '10px'}),

        dbc.Row([
            dbc.Col(html.P("""
                Se trata de una primera Asamblea Ciudadana para definir el funcionamiento de los 3 ciclos deliberativos propuestos
                y cómo dialogan con el actual sistema de participación distrital de la ciudad de Bogotá. A este proceso de diseño participativo
                centrado en las personas, en el que en el marco de una Asamblea Ciudadana se delibera sobre el funcionamiento de futuras Asambleas Ciudadanas,
                le hemos llamado Meta-Deliberación. De manera general, la Meta Asamblea se desarrolla en 4 fases: convocatoria, formación, deliberación
                y seguimiento de acuerdos. El propósito de la Meta Asamblea es lograr un ejercicio deliberativo que tenga como resultado la definición
                de las bases para la expedición de un marco regulatorio y reglamentario de la participación y deliberación ciudadana de cara a los ciclos
                deliberativos a realizarse entre el 2025 y 2027.
            """, style={'textAlign': 'center', 'fontSize': '18px', 'maxWidth': '800px', 'marginLeft': 'auto', 'marginRight': 'auto'}), width=12),
        ], justify='center', style={'marginTop': '20px'}),

        # Fila para el contenido de los gráficos
        dbc.Row([
            dcc.Loading([
                html.Div(id='tabs-content')
            ], type='default', color='#2956A4', style={'width': '100%'})  # El ancho ahora es 100%
        ], justify='center')  # Asegura que los gráficos se centren en la fila
    ], style={'padding': '0px', 'maxWidth': '100%'})  # Asegura que el contenedor ocupe el 100% del ancho
], style={'backgroundColor': 'white', 'minHeight': '100vh'})



data = pd.read_excel("ANEXO_A_Filter.xlsx")
data_pos = pd.read_excel("ANEXO_C_Filter.xlsx")
data_tree = pd.read_excel("archivo_con_resumenes.xlsx")


# Define function to load data based on tab selection
def load_data(tab):
    if tab == 'Encuestas':
        return data, data_pos
    elif tab == 'Sentimientos':
        return data_tree, 0
    elif tab == 'Debate':
        return 0, 0

@app.callback(
    Output('tabs-content', 'children'),
    [Input('graph-tabs', 'value')]
)

def update_tab(tab):

    data, data_pos = load_data(tab)

    if tab == 'Encuestas':
        fig1 = generate_visualizations1(data, data_pos)
        return html.Div([
        dbc.Row([
            dbc.Col(html.H3("Encuestas", style={'textAlign': 'center', 'fontSize': '30px'}), width=12),
        ], justify='center', style={'width': '100%', 'display': 'flex', 'justifyContent': 'center'}),

        dbc.Row([
            dbc.Col(html.P("""
                Durante los cuatro días de ejecución de la Meta-Asamblea, se aplicaron un total de tres encuestas a los asambleístas. Estas herramientas permitieron recoger sus percepciones sobre el desarrollo del proceso, evaluar la calidad de la deliberación y medir el impacto de las metodologías empleadas.
            """, style={'textAlign': 'center', 'fontSize': '18px', 'maxWidth': '800px', 'marginLeft': 'auto', 'marginRight': 'auto'}), width=12),
        ], justify='center', style={'width': '100%', 'display': 'flex', 'justifyContent': 'center'}),
        html.Div([
            dcc.Graph(id='graph1', figure=fig1[0]),
        ], style={'width': '100%', 'display': 'flex', 'justifyContent': 'center'}),
        html.Div([
            dcc.Graph(id='graph2', figure=fig1[1]),
        ], style={'width': '100%', 'display': 'flex', 'justifyContent': 'center'}),
        html.Div([
            dcc.Graph(id='graph3', figure=fig1[2]),
        ], style={'width': '100%', 'display': 'flex', 'justifyContent': 'center'}),
        html.Div([
            dcc.Graph(id='graph4', figure=fig1[3]),
        ], style={'width': '100%', 'display': 'flex', 'justifyContent': 'center'}),
        html.Div([
            dcc.Graph(id='graph5', figure=fig1[4]),
        ], style={'width': '100%', 'display': 'flex', 'justifyContent': 'center'}),
        html.Div([
            dcc.Graph(id='graph6', figure=fig1[5]),
        ], style={'width': '100%', 'display': 'flex', 'justifyContent': 'center'}),
        html.Div([
            dcc.Graph(id='graph7', figure=fig1[6]),
        ], style={'width': '100%', 'display': 'flex', 'justifyContent': 'center'})
    ])
    elif tab == 'Relatorias':
        fig1, fig2, fig3, fig4 = generate_visualizations2(data, splits)
        return html.Div([
        html.Div([
            dcc.Graph(id='graph1', figure=fig1),
        ], style={'width': '50%', 'display': 'inline-block'}),
        html.Div([
            dcc.Graph(id='graph2', figure=fig2),
        ], style={'width': '50%', 'display': 'inline-block'}),
        html.Div([
            dcc.Graph(id='graph3', figure=fig3),
        ], style={'width': '50%', 'display': 'inline-block'}),
        html.Div([
            dcc.Graph(id='graph4', figure=fig4),
        ], style={'width': '50%', 'display': 'inline-block'})
    ])
    elif tab == 'Sentimientos':
        fig1 = generate_visualizations3(data)
        return html.Div([
        html.Div([
            dcc.Graph(id='graph1', figure=fig1),
        ], style={'width': '100%', 'display': 'flex', 'justifyContent': 'center'})
        ])
    elif tab == 'Debate':
        fig1, fig2 = generate_visualizations4()
        return html.Div([
        html.Div([
            dcc.Graph(id='graph1', figure=fig1),
        ], style={'width': '100%', 'display': 'flex', 'justifyContent': 'center'}),
        html.Div([
            dcc.Graph(id='graph2', figure=fig2),
        ], style={'width': '100%', 'display': 'flex', 'justifyContent': 'center'}),
        ])

if __name__ == '__main__':
    app.run_server(debug=False)
