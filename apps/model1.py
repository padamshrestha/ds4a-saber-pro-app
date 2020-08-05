import dash_html_components as html
import dash_bootstrap_components as dbc
import dash
import dash_html_components as html
import pandas as pd
import numpy as np
import os
import glob
#import sklearn.metrics       as Metrics
from sklearn import metrics
from sklearn.ensemble import RandomForestRegressor 
import joblib
#from sklearn.model_selection import train_test_split
import pickle
from sqlalchemy import create_engine
from utils import *
from dash.dependencies import Input, Output
from app import app
from math import radians, cos, sin, asin, sqrt
from sqlalchemy import create_engine



# Create Engine and connect to DB
engine = create_engine('postgresql://admin:ds4a@project.c6mkiiu8v7ky.us-east-2.rds.amazonaws.com/project_ds4a')

#Define variables for reactive components
#Departamento options
departamento_model = get_unique(engine, 'pro_data', "estu_inst_departamento")


ModelQRPrueba = joblib.load('ModelQR.pkl')
QR1=np.round(ModelQRPrueba.predict([[59, 59, 59, 22, 6, 0,1,1,1,1,0,1,0,0,0,0,0,0]]),0)
QR1
X1=int(QR1[0])
X1


#######****Corregir_nombre#############################################################
posenglish_form = dbc.Form(
    [
        dbc.FormGroup(
            [
                dbc.Label("Position Saber 11", className="mr-2"),
                dbc.Input(id="m01", type="number", placeholder="posenglish", min=0, max=1000, step=0.01),
            ],
            className="mr-3",
        )

    ],
)

###################################################################
program_form = dbc.Form(
    [

    dbc.FormGroup(
        [
            dbc.Label("Program", className="mr-2"),
            dbc.Input(id="m02", type="text", placeholder="Ingenieria Industrial"),
        ],
        className="mr-3",
    )
    ],
)

#####****######################################################################
scoreMathHighSchool_form = dbc.Form(
    [
dbc.FormGroup(
    [
        dbc.Label("Score Math Saber 11", className="mr-2"),
        dbc.Input(id="m03", type="number", placeholder="ScoreMathHighSchool", min=0, max=150, step=0.01),
    ],
    className="mr-3",
)
    ],
)

##############################################################################
university_form = dbc.Form(
    [
        dbc.FormGroup(
            [
    dbc.Label("University", className="mr-2"),
    dbc.Input(id="m04", type="text", placeholder="Universidad De Cartagena"),
            ],
            className="mr-3",
        )
    ],
)

############################################################################
ScoreEnglishHighSchool_form = dbc.Form(
    [
        dbc.FormGroup(
            [
                dbc.Label("Score English Saber 11", className="mr-2"),
                dbc.Input(id="m05", type="number", placeholder="ScoreEnglishHighSchool", min=0, max=150, step=0.01),
            ],
            className="mr-3",
        )

    ],
)


##############################################################################

state_form = dbc.Form(
    [
        dbc.FormGroup(
            [
                dbc.Label("State Where you Live", className="mr-2"),
                dbc.Select(
                    id="m06",
                    options=[{'label': i, 'value': i} for i in departamento_model],
                )
        ],
            className="mr-3",
        )

    ],
)


###########****######################################################################

age_form = dbc.Form(
    [
        dbc.FormGroup(
            [
                dbc.Label("Age", className="mr-2"),
                dbc.Input(id="m07", type="number", placeholder="age", min=0, max=60, step=1),
            ],
            className="mr-3",
        )

    ],
)


##################################################################################

state_uni_form = dbc.Form(
    [
        dbc.FormGroup(
            [
                dbc.Label("State Where you Study", className="mr-2"),
                dbc.Select(
                    id="m08",
                    options=[{'label': i, 'value': i} for i in departamento_model]
                )
            ],
            className="mr-3",
        )

    ],
)


#####################################################################################

years11_form = dbc.Form(
    [
        dbc.FormGroup(
            [
                dbc.Label("Year when Saber11 was presented", className="mr-2"),
                dbc.Input(id="m09", type="number", placeholder="Year when Saber11 was presented", min=1990, max=2019, step=1),
            ],
            className="mr-3",
        )

    ],
)


##########################################################################################

gender_form = dbc.Form(
    [
        dbc.FormGroup(
            [
                dbc.Label("Gender", className="mr-2"),
                dbc.Select(
                    id="m010",
                    options=[
                                {"label": "Male", "value": "M"},
                                {"label": "Female", "value": "F"},
                        ],
                )



            ],
            className="mr-3",
        )

    ],
)



##########################################################################################

year_pro_form = dbc.Form(
    [
        dbc.FormGroup(
            [
                dbc.Label("Year when Saber Pro was presented", className="mr-2"),
                dbc.Input(id="m011", type="number", placeholder="Year when Saber pro was presented", min=2016, max=2025, step=1),
            ],
            className="mr-3",
        )

    ],
)


#############################################################################################
mother_level_form = dbc.Form(
    [
        dbc.FormGroup(
            [
                dbc.Label("Mother education", className="mr-2"),
                dbc.Select(
                    id="m012",
                    options=[
                                {"label": "No bachiller", "value": "1"},
                                {"label": "Bachiller", "value": "2"},
                                {"label": "Tecnico", "value": "3"},
                                {"label": "Profesional", "value": "4"},
                                {"label": "Postgrado", "value": "5"},
                                {"label": "NS-NR", "value": "6"},
                    ],
                )



            ],
            className="mr-3",
        )

    ],
)


##########################################################################################################

value_form = dbc.Form(
    [
        dbc.FormGroup(
            [
                dbc.Label("Value payd in the university per semester", className="mr-2"),
                dbc.Select(
                    id="m013", 
                    options=[
                                {"label": "Menos de 500 mil'", "value": "1"},
                                {"label": "0.5M-4M", "value": "2"},
                                {"label": "4M-7M", "value": "3"},
                                {"label": "7+", "value": "4"},
                                {"label": "No pago matricula", "value": "5"},
                    ],
                )



            ],
            className="mr-3",
        )

    ],
)

#############################################################################################################

credit_form = dbc.Form(
    [
        dbc.FormGroup(
            [
                dbc.Label("Did you use a credit to pay university?", className="mr-2"),
                dbc.Select(
                    id="m014", 
                    options=[
                                {"label": "YES", "value": "YES"},
                                {"label": "NO", "value": "NO"},
                    ],
                )



            ],
            className="mr-3",
        )

    ],
)



##################################################################################################################
help_form = dbc.Form(
    [
        dbc.FormGroup(
            [
                dbc.Label("Did your parents help you to pay the university?", className="mr-2"),
                dbc.Select(
                    id="m015", 
                    options=[
                                {"label": "Parents", "value": "Parents"},
                                {"label": "Scholarship", "value": "Scholarship"},
                                {"label": "Myself", "value": "Myself"},
                    ],
                )



            ],
            className="mr-3",
        )

    ],
)
##################################################################

suerte_botton = dbc.Button("Wish me luck!", color="primary", id="m016",)

##################################################################################################################
##################################################################################################################
tarjeta1 = dbc.Card(
    dbc.CardBody(
        [
            posenglish_form,
            scoreMathHighSchool_form,
            ScoreEnglishHighSchool_form,
            age_form,
            years11_form,
            year_pro_form,
            value_form,
            help_form,
        ]
    )
)

tarjeta2 = dbc.Card(
    dbc.CardBody(
        [
            program_form,
            university_form,
            state_form,
            state_uni_form,
            gender_form,
            mother_level_form,
            credit_form,
            suerte_botton,
        ]
    )
)



row_1 = dbc.Row(
    [
        dbc.Col(dbc.Card(tarjeta1, color="secondary", outline=True)),
        dbc.Col(dbc.Card(tarjeta2, color="secondary", outline=True)),
    ],
    className="mb-4",
)


forumulario = html.Div([row_1])



#######################################################################################
#######################################################################################



card_content_1 = [
    dbc.CardBody(
        [
            html.H3("Quantitative Reasoning", className="card-title"),
            html.P(
                "Score expected for you:",
                className="card-text",
            ),
            html.H3(id="mout_01", style={"vertical-align": "middle"}),

        ]
    ),
]

card_content_2 = [
    dbc.CardBody(
        [
            html.H3("Citizen competence", className="card-title"),          
            html.P(
                "Score expected for you:",
                className="card-text",
            ),
            html.H3(id="mout_06", style={"vertical-align": "middle"}),
        ]
    ),
]

card_content_3 = [
    dbc.CardBody(
        [
            html.H3("Critical Lecture", className="card-title"), 
            html.P(
                "Score expected for you:",
                className="card-text",
            ),
            html.H3(id="mout_02", style={"vertical-align": "middle"}),

        ]
    ),
]

card_content_4 = [
    dbc.CardBody(
        [
            html.H3("English", className="card-title"),             
            html.P(
                "Score expected for you:",
                className="card-text",
            ),
            html.H3(id="mout_03", style={"vertical-align": "middle"}),
        ]
    ),
]


card_content_5 = [
    dbc.CardBody(
        [
            html.H3("Written Communication", className="card-title"),                       
            html.P(
                "Score expected for you:",
                className="card-text",
            ),
            html.H3(id="mout_04", style={"vertical-align": "middle"}),
        ]
    ),
]

card_content_6 = [
    dbc.CardBody(
        [
            html.H3("Global Score", className="card-title"),                       
            html.P(
                "Score expected for you:",
                className="card-text",
            ),
            html.H3(id="mout_05", style={"vertical-align": "middle"}),
        ]
    ),
]


row_1 = dbc.Row(
    [
        dbc.Col(dbc.Card(card_content_1, color="secondary", outline=True)),
        dbc.Col(dbc.Card(card_content_2, color="secondary", outline=True)),
    ],
    className="mb-4",
)

row_2 = dbc.Row(
    [
        dbc.Col(dbc.Card(card_content_3, color="secondary", outline=True)),
        dbc.Col(dbc.Card(card_content_4, color="secondary", outline=True)),
    ],
    className="mb-4",
)

row_3 = dbc.Row(
    [
        dbc.Col(dbc.Card(card_content_5, color="secondary", outline=True)),
        dbc.Col(dbc.Card(card_content_6, color="secondary", outline=True)),
    ],
    className="mb-4",
)

cards = html.Div([row_1, row_2, row_3])

esquema = dbc.Row(
    [
        dbc.Col(forumulario),
        dbc.Col(cards),

    ],
    no_gutters=True,
)



button = html.Div(
    [
        dbc.Button("Click me", id="example-button", className="mr-2"),
        html.Span(id="example-output", style={"vertical-align": "middle"}),
    ]
)


layout = html.Div([
    html.H1("Predicting Saber Pro Scores"),
    esquema,
])

@app.callback(Output("mout_01", "children"), [Input("m016", "n_clicks"),
                                               Input("m01", "value"),
                                               Input("m03", "value"),
                                               Input("m05", "value"),
                                               Input("m07", "value"),
                                               Input("m014", "value"),
                                               Input("m015", "value"),
                                               Input("m012", "value"),
                                               Input("m013", "value"),
                                               Input("m09", "value"),
                                               Input("m011", "value"),
                                               Input("m010", "value")])

                
                
def modelos(n_clicks, m01, m03, m05, m07,m014, m015,m012,m013,m09,m011, m010):
    if n_clicks is None:
        return ""
    else:

        hscore = 100
        hmvalue = 100
        agevalue = 30
        saber11 = 2014
        saberpro = 2019
        paydwayscholar = 0
        paydwayparent = 0
        mof = 0
        credito=0
        mama_1 = 0
        mama_3 = 0
        mama_4 = 0
        mama_5 = 0
        mama_m = m012
        credito_m= m014
        costo = m013
        costo_1 = 0
        costo_2 = 0
        costo_3 = 0
        costo_no = 0
        genero = m010
        if genero == 'M':
            mof = 1
        else:
            mof = 0
        hmvalue = float(m03)
        hscore = float(m01)
        agevalue = float(m07)
        saber11 = float(m09)
        saberpro = float(m011)
        timesaber = saberpro -saber11
        
        paydway = m015
###################################
        if paydway == 'Parents':
            paydwayparent = 1
        else:
            if paydway == 'Scholarship':
                paydwayscholar = 1
            else:
                paydwayparent = 0
                paydwayscholar = 0
 ####################################
        if credito_m == 'YES':
            credito = 1
        else:
            credito = 0
#########################################
        if mama_m == '1':
            mama_1 = 1
        else:
            if mama_m == '3':
                mama_3 = 1
            else:
                if mama_m == '4':
                    mama_4 = 1
                else:
                    if mama_m == '5':
                        mama_5 = 1
                    else:
                        mama_1 = 0
                        mama_3 = 0
                        mama_4 = 0
                        mama_5 = 0
#########################################
        if costo == '1':
            costo_1 = 1
        else:
            if costo == '2':
                costo_2 = 1
            else:
                if costo == '3':
                    costo_3 = 1
                else:
                    if costo == '5':
                        costo_no = 1
                    else:
                        costo_1 = 0
                        costo_2 = 0
                        costo_3 = 0
                        costo_no = 0


        ModelQRPrueba = joblib.load('ModelQR.pkl')
        QR1 = np.round(ModelQRPrueba.predict([[hscore, hmvalue, 59, agevalue, timesaber, mof, 1, paydwayscholar, credito, paydwayparent, mama_1, mama_3, mama_4, mama_5, costo_1, costo_2, costo_3, costo_no]]),
                       0)
        X1 = int(QR1[0])
        
        
        return X1
        
  ##########################################################################################################
@app.callback(Output("mout_02", "children"), [Input("m016", "n_clicks"),
                                               Input("m01", "value"),
                                               Input("m03", "value"),
                                               Input("m05", "value"),
                                               Input("m07", "value"),
                                               Input("m014", "value"),
                                               Input("m015", "value"),
                                               Input("m012", "value"),
                                               Input("m013", "value"),
                                               Input("m09", "value"),
                                               Input("m011", "value"),
                                               Input("m010", "value"),
                                               Input("m06", "value"),
                                               Input("m08", "value")])

                
                
def modelos2(n_clicks, m01, m03, m05, m07,m014, m015,m012,m013,m09,m011, m010,m06,m08):
    if n_clicks is None:
        return ""
    else:
        dept1 = pd.read_sql("SELECT Lat,Lon FROM departamento_detallado where Departamento='"+m06+"'", engine.connect())
        dept2 = pd.read_sql("SELECT Lat,Lon FROM departamento_detallado where Departamento='"+m08+"'", engine.connect())
        lon1=dept1.values.tolist()[0][0]
        lat1=dept1.values.tolist()[0][1]
        lon2=dept2.values.tolist()[0][0]
        lat2=dept2.values.tolist()[0][1]
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
        # haversine formula 
        dlon = lon2 - lon1 
        dlat = lat2 - lat1 
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a)) 
        # Radius of earth in kilometers is 6371
        km = 6371* c
        #############################################################################################################################################
        cluster_1=0
        cluster_2=0
        cluster_3=0
        cluster_4=0
        cluster = pd.read_sql("SELECT clusterdepartamentoescalado FROM departamento_detallado WHERE departamento='"+m08+"'", engine.connect())
        cluster_m = cluster.values.tolist()[0][0]
        if cluster_m == 1:
            cluster_1 = 1
        elif cluster_m == 2:
            cluster_2 = 1
        elif cluster_m == 3:
            cluster_3 = 1            
        elif cluster_m == 4:
            cluster_4 = 1           
        elif cluster_m == 4:
            cluster_4 = 1        
            
        ###############################################################################################################################################
        hscore = 100
        hmvalue = 100
        agevalue = 30
        saber11 = 2014
        saberpro = 2019
        paydwayscholar = 0
        paydwayparent = 0
        mof = 0
        credito=0
        mama_1 = 0
        mama_3 = 0
        mama_4 = 0
        mama_5 = 0
        mama_m = m012
        credito_m= m014
        costo = m013
        costo_1 = 0
        costo_2 = 0
        costo_3 = 0
        costo_no = 0
        genero = m010
        if genero == 'M':
            mof = 1
        else:
            mof = 0
        hmvalue = float(m03)
        hscore = float(m01)
        agevalue = float(m07)
        saber11 = float(m09)
        saberpro = float(m011)
        timesaber = saberpro -saber11
        
        paydway = m015
###################################
        if paydway == 'Parents':
            paydwayparent = 1
        else:
            if paydway == 'Scholarship':
                paydwayscholar = 1
            else:
                paydwayparent = 0
                paydwayscholar = 0
 ####################################
        if credito_m == 'YES':
            credito = 1
        else:
            credito = 0
#########################################
        if mama_m == '1':
            mama_1 = 1
        else:
            if mama_m == '3':
                mama_3 = 1
            else:
                if mama_m == '4':
                    mama_4 = 1
                else:
                    if mama_m == '5':
                        mama_5 = 1
                    else:
                        mama_1 = 0
                        mama_3 = 0
                        mama_4 = 0
                        mama_5 = 0
#########################################
        if costo == '1':
            costo_1 = 1
        else:
            if costo == '2':
                costo_2 = 1
            else:
                if costo == '3':
                    costo_3 = 1
                else:
                    if costo == '5':
                        costo_no = 1
                    else:
                        costo_1 = 0
                        costo_2 = 0
                        costo_3 = 0
                        costo_no = 0


        ModelRE = joblib.load('ModelRE.pkl')
        RE=np.round(ModelRE.predict([[
                                        hscore,
                                        hmvalue,
                                        154,
                                        agevalue,
                                        timesaber,
                                        mof,
                                        km,
                                        paydwayscholar,
                                        credito,
                                        paydwayparent,
                                        mama_1,
                                        mama_3,
                                        mama_4,
                                        mama_5,
                                        costo_1,
                                        costo_2,
                                        costo_3,
                                        costo_no
                                        ]]),0)
        READING=int(RE[0])
        X2 = READING

        
        return X2

 ##########################################################################################################
@app.callback(Output("mout_03", "children"), [Input("m016", "n_clicks"),
                                               Input("m01", "value"),
                                               Input("m03", "value"),
                                               Input("m05", "value"),
                                               Input("m07", "value"),
                                               Input("m014", "value"),
                                               Input("m015", "value"),
                                               Input("m012", "value"),
                                               Input("m013", "value"),
                                               Input("m09", "value"),
                                               Input("m011", "value"),
                                               Input("m010", "value")])

                
                
def modelos3(n_clicks, m01, m03, m05, m07,m014, m015,m012,m013,m09,m011, m010):
    if n_clicks is None:
        return ""
    else:

        hscore = 100
        hmvalue = 100
        agevalue = 30
        saber11 = 2014
        saberpro = 2019
        paydwayscholar = 0
        paydwayparent = 0
        mof = 0
        credito=0
        mama_1 = 0
        mama_3 = 0
        mama_4 = 0
        mama_5 = 0
        mama_m = m012
        credito_m= m014
        costo = m013
        costo_1 = 0
        costo_2 = 0
        costo_3 = 0
        costo_no = 0
        genero = m010
        if genero == 'M':
            mof = 1
        else:
            mof = 0
        hmvalue = float(m03)
        hscore = float(m01)
        agevalue = float(m07)
        saber11 = float(m09)
        saberpro = float(m011)
        timesaber = saberpro -saber11
        
        paydway = m015
###################################
        if paydway == 'Parents':
            paydwayparent = 1
        else:
            if paydway == 'Scholarship':
                paydwayscholar = 1
            else:
                paydwayparent = 0
                paydwayscholar = 0
 ####################################
        if credito_m == 'YES':
            credito = 1
        else:
            credito = 0
#########################################
        if mama_m == '1':
            mama_1 = 1
        else:
            if mama_m == '3':
                mama_3 = 1
            else:
                if mama_m == '4':
                    mama_4 = 1
                else:
                    if mama_m == '5':
                        mama_5 = 1
                    else:
                        mama_1 = 0
                        mama_3 = 0
                        mama_4 = 0
                        mama_5 = 0
#########################################
        if costo == '1':
            costo_1 = 1
        else:
            if costo == '2':
                costo_2 = 1
            else:
                if costo == '3':
                    costo_3 = 1
                else:
                    if costo == '5':
                        costo_no = 1
                    else:
                        costo_1 = 0
                        costo_2 = 0
                        costo_3 = 0
                        costo_no = 0


        ModelQRPrueba = joblib.load('ModelQR.pkl')
        QR1 = np.round(ModelQRPrueba.predict([[hscore, hmvalue, 59, agevalue, timesaber, mof, 1, paydwayscholar, credito, paydwayparent, mama_1, mama_3, mama_4, mama_5, costo_1, costo_2, costo_3, costo_no]]),
                       0)
        X1 = int(QR1[0])
        X2 = X1 + 12
        X3 = X1 + 8
        X4 = X1 + 4
        X5 = X1 + 5
        X6 = X1 + 15
        
        return X3

     ##########################################################################################################
@app.callback(Output("mout_04", "children"), [Input("m016", "n_clicks"),
                                               Input("m01", "value"),
                                               Input("m03", "value"),
                                               Input("m05", "value"),
                                               Input("m07", "value"),
                                               Input("m014", "value"),
                                               Input("m015", "value"),
                                               Input("m012", "value"),
                                               Input("m013", "value"),
                                               Input("m09", "value"),
                                               Input("m011", "value"),
                                               Input("m010", "value")])

                
                
def modelos4(n_clicks, m01, m03, m05, m07,m014, m015,m012,m013,m09,m011, m010):
    if n_clicks is None:
        return ""
    else:

        hscore = 100
        hmvalue = 100
        agevalue = 30
        saber11 = 2014
        saberpro = 2019
        paydwayscholar = 0
        paydwayparent = 0
        mof = 0
        credito=0
        mama_1 = 0
        mama_3 = 0
        mama_4 = 0
        mama_5 = 0
        mama_m = m012
        credito_m= m014
        costo = m013
        costo_1 = 0
        costo_2 = 0
        costo_3 = 0
        costo_no = 0
        genero = m010
        if genero == 'M':
            mof = 1
        else:
            mof = 0
        hmvalue = float(m03)
        hscore = float(m01)
        agevalue = float(m07)
        saber11 = float(m09)
        saberpro = float(m011)
        timesaber = saberpro -saber11
        
        paydway = m015
###################################
        if paydway == 'Parents':
            paydwayparent = 1
        else:
            if paydway == 'Scholarship':
                paydwayscholar = 1
            else:
                paydwayparent = 0
                paydwayscholar = 0
 ####################################
        if credito_m == 'YES':
            credito = 1
        else:
            credito = 0
#########################################
        if mama_m == '1':
            mama_1 = 1
        else:
            if mama_m == '3':
                mama_3 = 1
            else:
                if mama_m == '4':
                    mama_4 = 1
                else:
                    if mama_m == '5':
                        mama_5 = 1
                    else:
                        mama_1 = 0
                        mama_3 = 0
                        mama_4 = 0
                        mama_5 = 0
#########################################
        if costo == '1':
            costo_1 = 1
        else:
            if costo == '2':
                costo_2 = 1
            else:
                if costo == '3':
                    costo_3 = 1
                else:
                    if costo == '5':
                        costo_no = 1
                    else:
                        costo_1 = 0
                        costo_2 = 0
                        costo_3 = 0
                        costo_no = 0


        ModelQRPrueba = joblib.load('ModelQR.pkl')
        QR1 = np.round(ModelQRPrueba.predict([[hscore, hmvalue, 59, agevalue, timesaber, mof, 1, paydwayscholar, credito, paydwayparent, mama_1, mama_3, mama_4, mama_5, costo_1, costo_2, costo_3, costo_no]]),
                       0)
        X1 = int(QR1[0])
        X2 = X1 + 12
        X3 = X1 + 8
        X4 = X1 + 4
        X5 = X1 + 5
        X6 = X1 + 15
        
        return X4

     ##########################################################################################################
@app.callback(Output("mout_05", "children"), [Input("m016", "n_clicks"),
                                               Input("m01", "value"),
                                               Input("m03", "value"),
                                               Input("m05", "value"),
                                               Input("m07", "value"),
                                               Input("m014", "value"),
                                               Input("m015", "value"),
                                               Input("m012", "value"),
                                               Input("m013", "value"),
                                               Input("m09", "value"),
                                               Input("m011", "value"),
                                               Input("m010", "value")])

                
                
def modelos5(n_clicks, m01, m03, m05, m07,m014, m015,m012,m013,m09,m011, m010):
    if n_clicks is None:
        return ""
    else:

        hscore = 100
        hmvalue = 100
        agevalue = 30
        saber11 = 2014
        saberpro = 2019
        paydwayscholar = 0
        paydwayparent = 0
        mof = 0
        credito=0
        mama_1 = 0
        mama_3 = 0
        mama_4 = 0
        mama_5 = 0
        mama_m = m012
        credito_m= m014
        costo = m013
        costo_1 = 0
        costo_2 = 0
        costo_3 = 0
        costo_no = 0
        genero = m010
        if genero == 'M':
            mof = 1
        else:
            mof = 0
        hmvalue = float(m03)
        hscore = float(m01)
        agevalue = float(m07)
        saber11 = float(m09)
        saberpro = float(m011)
        timesaber = saberpro -saber11
        
        paydway = m015
###################################
        if paydway == 'Parents':
            paydwayparent = 1
        else:
            if paydway == 'Scholarship':
                paydwayscholar = 1
            else:
                paydwayparent = 0
                paydwayscholar = 0
 ####################################
        if credito_m == 'YES':
            credito = 1
        else:
            credito = 0
#########################################
        if mama_m == '1':
            mama_1 = 1
        else:
            if mama_m == '3':
                mama_3 = 1
            else:
                if mama_m == '4':
                    mama_4 = 1
                else:
                    if mama_m == '5':
                        mama_5 = 1
                    else:
                        mama_1 = 0
                        mama_3 = 0
                        mama_4 = 0
                        mama_5 = 0
#########################################
        if costo == '1':
            costo_1 = 1
        else:
            if costo == '2':
                costo_2 = 1
            else:
                if costo == '3':
                    costo_3 = 1
                else:
                    if costo == '5':
                        costo_no = 1
                    else:
                        costo_1 = 0
                        costo_2 = 0
                        costo_3 = 0
                        costo_no = 0


        ModelQRPrueba = joblib.load('ModelQR.pkl')
        QR1 = np.round(ModelQRPrueba.predict([[hscore, hmvalue, 59, agevalue, timesaber, mof, 1, paydwayscholar, credito, paydwayparent, mama_1, mama_3, mama_4, mama_5, costo_1, costo_2, costo_3, costo_no]]),
                       0)
        X1 = int(QR1[0])
        X2 = X1 + 12
        X3 = X1 + 8
        X4 = X1 + 4
        X5 = X1 + 5
        X6 = X1 + 15
        
        return X5

     ##########################################################################################################
@app.callback(Output("mout_06", "children"), [Input("m016", "n_clicks"),
                                               Input("m01", "value"),
                                               Input("m03", "value"),
                                               Input("m05", "value"),
                                               Input("m07", "value"),
                                               Input("m014", "value"),
                                               Input("m015", "value"),
                                               Input("m012", "value"),
                                               Input("m013", "value"),
                                               Input("m09", "value"),
                                               Input("m011", "value"),
                                               Input("m010", "value"),
                                               Input("m06", "value"),
                                               Input("m08", "value")])

                
                
def modelos6(n_clicks, m01, m03, m05, m07,m014, m015,m012,m013,m09,m011, m010,m06,m08):
    if n_clicks is None:
        return ""
    else:

        hscore = 100
        hmvalue = 100
        agevalue = 30
        saber11 = 2014
        saberpro = 2019
        paydwayscholar = 0
        paydwayparent = 0
        mof = 0
        credito=0
        mama_1 = 0
        mama_3 = 0
        mama_4 = 0
        mama_5 = 0
        mama_m = m012
        credito_m= m014
        costo = m013
        costo_1 = 0
        costo_2 = 0
        costo_3 = 0
        costo_no = 0
        genero = m010
        if genero == 'M':
            mof = 1
        else:
            mof = 0
        hmvalue = float(m03)
        hscore = float(m01)
        agevalue = float(m07)
        saber11 = float(m09)
        saberpro = float(m011)
        timesaber = saberpro -saber11
        
        paydway = m015
###################################
        if paydway == 'Parents':
            paydwayparent = 1
        else:
            if paydway == 'Scholarship':
                paydwayscholar = 1
            else:
                paydwayparent = 0
                paydwayscholar = 0
 ####################################
        if credito_m == 'YES':
            credito = 1
        else:
            credito = 0
#########################################
        if mama_m == '1':
            mama_1 = 1
        else:
            if mama_m == '3':
                mama_3 = 1
            else:
                if mama_m == '4':
                    mama_4 = 1
                else:
                    if mama_m == '5':
                        mama_5 = 1
                    else:
                        mama_1 = 0
                        mama_3 = 0
                        mama_4 = 0
                        mama_5 = 0
#########################################
        if costo == '1':
            costo_1 = 1
        elif costo == '2':
            costo_2 = 1
        elif costo == '3':
            costo_3 = 1
        elif costo == '5':
            costo_no = 1                       
                        
        dept1 = pd.read_sql("SELECT Lat,Lon FROM departamento_detallado where Departamento='"+m06+"'", engine.connect())
        dept2 = pd.read_sql("SELECT Lat,Lon FROM departamento_detallado where Departamento='"+m08+"'", engine.connect())
        lon1=dept1.values.tolist()[0][0]
        lat1=dept1.values.tolist()[0][1]
        lon2=dept2.values.tolist()[0][0]
        lat2=dept2.values.tolist()[0][1]
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
        # haversine formula 
        dlon = lon2 - lon1 
        dlat = lat2 - lat1 
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a)) 
        # Radius of earth in kilometers is 6371
        km = 6371* c
        #############################################################################################################################################
        cluster_1=0
        cluster_2=0
        cluster_3=0
        cluster_4=0
        cluster = pd.read_sql("SELECT clusterdepartamentoescalado FROM departamento_detallado WHERE departamento='"+m08+"'", engine.connect())
        cluster_m = cluster.values.tolist()[0][0]
        if cluster_m == 1:
            cluster_1 = 1
        elif cluster_m == 2:
            cluster_2 = 1
        elif cluster_m == 3:
            cluster_3 = 1            
        elif cluster_m == 4:
            cluster_4 = 1           
        elif cluster_m == 4:
            cluster_4 = 1     

        ModelCI = joblib.load('ModelCI.pkl')
        CI=np.round(ModelCI.predict([[
                                    hscore,
                                    hmvalue,
                                    146,
                                    agevalue,
                                    timesaber,
                                    mof,
                                    km,
                                    paydwayscholar,
                                    credito,
                                    paydwayparent,
                                    mama_1,
                                    mama_3,
                                    mama_4,
                                    mama_5,
                                    cluster_1,
                                    cluster_2,
                                    cluster_3,
                                    cluster_4,
                                    costo_1,
                                    costo_2,
                                    costo_3,
                                    costo_no
                                    ]]),0)
        CITIZEN=int(CI[0])
        X6 = int(QR1[0])
        
        return X6
