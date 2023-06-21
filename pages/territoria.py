import dash
from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/territoria")


# Map switches - Móvil
switches_movil = html.Div([
    dbc.Label(
        "Explora el mapa 👇"
    ),
    dbc.Checklist(
        options=[
            {"label": "⚪ Estaciones de metro", "value": 1},
            {"label": "🔵 Reportes de violencia de género al 911", "value": 2},
            {"label": "🟣 Percepción de espacio inseguro o de peligro", "value": 3},
            {"label": "🟢 Percepción de espacio seguro", "value": 4},
        ],
        value=[1, 2, 3],
        id="switches-input-movil",
        switch=True,
        inline = True,
        input_checked_style = {"backgroundColor": "#5C6369", "borderColor": "#5C6369"}
    )
])

# Map switches - Desktop
switches_desktop = html.Div([
    dbc.Label(
        "Explora el mapa 👇"
    ),
    dbc.Checklist(
        options=[
            {"label": "⚪ Estaciones de metro", "value": 1},
            {"label": "🔵 Reportes de violencia de género al 911", "value": 2},
            {"label": "🟣 Percepción de espacio inseguro o de peligro", "value": 3},
            {"label": "🟢 Percepción de espacio seguro", "value": 4},
        ],
        value=[1, 2, 3],
        id="switches-input-desktop",
        switch=True,
        inline = True,
        input_checked_style = {"backgroundColor": "#5C6369", "borderColor": "#5C6369"}
    )
])


# Map's title
info_icon = html.I(className = "fas fa-info-circle", style = dict(display = "inline-block"))

btn_text = html.Div("Territoria", style = dict(paddingRight = "2vw", display = "inline-block"))

map_title = html.Span([btn_text, info_icon])


# Page layout
layout = html.Div([

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

    # Mapa - Móvil
    dbc.Row(

        # Sidebar and Map
        dbc.Col([
            # Map
            dcc.Graph(
                figure = {},
                config = {'displaylogo': False},
                style = {"height": "100vh", "width": "100%"},
                id = "mapa-movil"
            ),
            # Title
            dbc.Button(
                map_title,
                id = "open-offcanvas",
                n_clicks = 0,
                style = {"position": "absolute", "top": "5%", "left": "50%",
                        "transform": "translate(-50%, -50%)"},
                outline = False,
                color = "secondary",
                class_name="md-4 mx-auto"
            ),
            # Sidebar
            dbc.Offcanvas(
                [
                    html.P(
                        "Territoria es un mapa que visualiza los datos oficiales de violencia de género a"
                        "partir de las llamadas del 911 y la percepción de seguridad de las mujeres en el espacio "
                        "público."
                    ),
                    html.P([
                        "Conoce más sobre el proyecto ",
                        html.A(
                            "aquí",
                            href="https://drive.google.com/file/d/19SiUAV-BB0WWd54x-h_HUlszXqKOTKcN/view?usp=sharing",
                            target="_blank",
                            style={"color": "#A777B1"}
                        ),
                        ".",
                        html.Hr(),
                    ]),
                    html.Div(switches_movil, id="radioitems-checklist-output")
                ],
                id="offcanvas",
                title="Territoria",
                is_open=False,
                placement="start"
            )
        ],
            style = {"position": "relative"},
            className="pt-1 d-lg-none"
        )
    ),

    # Mapa - Desktop
    dbc.Row([

        # Sidebar
        dbc.Col([
            html.H4("Territoria", className = "px-4 pt-3"),
            html.P(
                "Territoria es un mapa que visualiza los datos oficiales de violencia de género a"
                "partir de las llamadas del 911 y la percepción de seguridad de las mujeres en el espacio "
                "público.", className = "px-4"
            ),
            html.P([
                "Conoce más sobre el proyecto ",
                html.A(
                    "aquí",
                    href="https://drive.google.com/file/d/19SiUAV-BB0WWd54x-h_HUlszXqKOTKcN/view?usp=sharing",
                    target="_blank",
                    style={"color": "#A777B1"}
                ),
                ".",
                html.Hr()
            ],
                className = "px-4"
            ),
            html.Div(
                switches_desktop,
                id="radioitems-checklist-output",
                className = "px-4"
            )
        ],
            lg = 3,
            xl = 3,
            className = "pt-1 d-none d-lg-block"
        ),

        # Map
        dbc.Col([
            dcc.Graph(
                figure={},
                config={'displaylogo': False},
                style={"height": "100vh", "width": "100%"},
                id="mapa-desktop",
            )
        ],
            lg = 9,
            xl = 9,
            className = "pt-1 d-none d-lg-block"
        )

    ])

])