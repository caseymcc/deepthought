
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc

from agents import *
from servers import *
from tasks import *

from task_screen import task_layout
from agent_screen import agent_layout
from nav_bar import create_navbar

# Initialize Dash app with Bootstrap
#app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
#app.title = "My Dash App"

#app = dash.Dash(__name__)



#agents.load("agents.json")
#
#app.layout = html.Div([
#    dcc.Location(id='url', refresh=False),
#    create_navbar(),
#    html.Div(id='page-content')
#])
#
#@app.callback(Output('page-content', 'children'),
#              [Input('url', 'pathname')])
#def display_page(pathname):
#    if pathname == '/tasks':
#        return task_layout
#    elif pathname == '/agents':
#        return agent_layouts
#        return task_layout

tasks = []
agents = []
servers = []

def get_server(name):
    for server in servers:
        if server.name == name:
            return server
        else:
            llm_config={
                "cache_seed": 42,  # seed for caching and reproducibility
                "config_list": config_list,  # a list of OpenAI API configurations
                "temperature": 0,  # temperature for sampling from the policy
            }
    return None

def get_agent(name):
    for agent in agents:
        if agent.name == name:
            return agent
        else:
            autogen.AssistantAgent(
                name="assistant",
                llm_config={
                    "cache_seed": 42,  # seed for caching and reproducibility
                    "config_list": config_list,  # a list of OpenAI API configurations
                    "temperature": 0,  # temperature for sampling from the policy
                }
            )
    return None

def main():
    servers_config = ServersConfig()
    agents_config = AgentsConfig()
    tasks_config = TasksConfig()

    servers_config.load("servers.json")
    agents_config.load("agents.json")
    tasks_config.load("tasks.json")



    for(task_config in tasks_config.tasks):
        task = Task(
            name=task_config.name,
            description=task_config.description,
            prompt=task_config.prompt,
        )
        task_agents = []

        for(agent_node in task.agents):
            agent = agent_config.get_agent(agent_node.name)

            if(agent.type == AgentType.Assistant):
                agent=

                task_agents.append(agent)


if __name__ == "__main__":
    main()

#    app.run_server(debug=True)