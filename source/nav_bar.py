from dash import html
import dash_bootstrap_components as dbc

def create_navbar():
    """
    Creates a navigation bar for the app using Dash Bootstrap Components.
    """
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Tasks", href="/")),
            dbc.NavItem(dbc.NavLink("Agents", href="/data")),
            ],
        brand="My Dash App",
        brand_href="/",
        color="primary",
        dark=True,
    )
    return navbar