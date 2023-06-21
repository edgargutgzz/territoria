import dash
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/seccionvioleta")


# Page layout

layout = dbc.Container([

    # Navbar
    dbc.Navbar(
        dbc.Container([

            html.A(
                dbc.Row(
                    dbc.Col(html.Img(src="assets/georregias_logo.jpeg", height="30px")),
                    align="center", className="g-0"
                ), href="/"
            ),

            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),

            dbc.Collapse(
                dbc.Nav([
                    dbc.NavItem(dbc.NavLink("Territoria", href="/territoria", style={"font-size": "18px"})),
                    dbc.NavItem(dbc.NavLink("Sección Violeta", href="/seccionvioleta", style={"font-size": "18px"}))
                ], className="ms-auto", navbar=True),
                id="navbar-collapse", navbar=True,
            )

        ]), color="#FFFFFF", dark=False,
    ),

    # Banner photo
    dbc.Row(
        dbc.Col(html.Img(src="assets/seccionvioleta_banner.jpg", className="img-fluid", style = {'height': '650px'})),
        className="pt-1", justify="center"
    ),

    # Texto principal
    dbc.Row([
        dbc.Col([
            html.P([
                "La Sección Violeta es una",
                html.Strong(" guía gratuita, práctica, accesible e inclusiva para mujeres de todos los"
                            " contextos"),
                " que se encuentren en situaciones de vulnerabilidad para que, en caso de una emergencia o"
                " situación de riesgo, conozcan las asociaciones, instituciones y colectivos a quienes pueden"
                " recurrir."
            ]),
            html.P([
                "Consulta la Sección Violeta ",
                html.A(" aquí", href="https://commons.wikimedia.org/wiki/File:Secci%C3%B3n_Violeta.pdf",
                       style={"color": "#A777B1"}, target="_blank"),
                "."
            ])
            ,
        ], style={"font-size": "24px", "text-align": "center"}, lg=11
        ),

    ],  className="pt-5 pb-5",
        justify="center"
    ),

    # Footer
    dbc.Row([
        dbc.Col([
            html.B(
                "¿Quieres ayudarnos a generar espacios seguros para todas y todos?",
                style={"font-size": "20px"}
            ),  
            html.P(
                "Envíanos un mensaje y platiquemos 💜",
                style={"font-size": "16px"},
                className = "pt-4"
            ),
            html.Div([
                html.A(
                    html.Img(src="assets/instagram.png", height="28px"),
                    href="https://www.instagram.com/georregias", target="_blank",
                    style={'margin-right': '20px'}  
                ),
                html.A(
                    html.Img(src="assets/facebook.png", height="28px"),
                    href="https://www.facebook.com/Georregias", target="_blank"
                )
            ], 
                style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center'},
                className = "pt-1"
            ),
            html.P(
                "georregias@gmail.com",
                style={"font-size": "16px"},
                className = "pt-3"
            ),
        ],  style={"background-color":"#F6F8FA", "text-align": "center"},
            className = "py-4"

        )
    ],
        className="pt-2 pb-3",
        justify="center"
    )




], fluid=False)