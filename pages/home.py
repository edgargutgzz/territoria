import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/")


# Page layout

layout = dbc.Container([

    # Navbar
    dbc.Navbar(
        dbc.Container([

            html.A(
                dbc.Row(
                    dbc.Col(html.Img(src="assets/georregias_logo.jpeg", height="30px")),
                    align="center", className="g-0"
                ),
                href="/"
            ),

            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),

            dbc.Collapse(
                dbc.Nav([
                    dbc.NavItem(dbc.NavLink("Territoria", href="/territoria", style={"font-size": "18px"})), 
                    dbc.NavItem(dbc.NavLink("Sección Violeta", href="/seccionvioleta", style={"font-size": "18px"})) 
                ], className="ms-auto", navbar=True),
                id="navbar-collapse", navbar=True,
            ),

        ]), color="#FFFFFF", dark=False,
    ),

    # Banner photo
    dbc.Row(
        dbc.Col(
            html.Img(
                src="assets/georregias_banner.jpg",
                style={'width': '100%', 'object-fit': 'cover'}
            )
        ),
        className="pt-1", 
        justify="center"
    ),

    # Texto principal - Desktop
    dbc.Row([
        dbc.Col([
            html.P([
                "Somos una colectiva enfocada en urbanismo feminista y cultura de cuidados que busca promover"
                " herramientas para que otras mujeres, de cualquier edad y origen,",
                html.Strong(" puedan habitar la ciudad y los espacios públicos de manera segura.")
            ], style={"font-size": "26px", 'text-align': 'center'}), 
        ], lg = 12)
    ],
        className="px-5 mx-4 pt-5 pb-5 d-none d-lg-block",
        justify="center"
    ),

    # Texto principal - Mobile
    dbc.Row([
        dbc.Col([
            html.P([
                "Somos una colectiva enfocada en urbanismo feminista y cultura de cuidados que busca promover"
                " herramientas para que otras mujeres, de cualquier edad y origen,",
                html.Strong(" puedan habitar la ciudad y los espacios públicos de manera segura.")
            ], style={"font-size": "22px", 'text-align': 'center'}), 
        ], lg = 12)
    ],
        className="px-4 pt-5 pb-5 d-lg-none",
        justify="center"
    ),

    # Footer - Desktop
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
        className="pt-2 pb-3 d-none d-lg-block",
        justify="center"
    ),

    # Footer - Mobile
    dbc.Row([
        dbc.Col([
            html.B(
                "¿Quieres ayudarnos a generar espacios seguros para todas y todos?",
                style={"font-size": "18px"}
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
        className="pt-2 pb-3 d-lg-none",
        justify="center"
    )

])