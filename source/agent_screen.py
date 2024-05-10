from dash import html

agent_layout = html.Div(
    [
        html.Div(
            [
                dcc.Listbox(
                    id="agent-list",
                    options=[{"label": agent["name"], "value": agent["name"]} for agent in agents_data],
                    multi=True,
                )
            ],
            style={"width": "30%", "display": "inline-block"},
        ),
        html.Div(
            id="agent-info",
            style={"width": "70%", "display": "inline-block", "vertical-align": "top"},
        ),
    ])