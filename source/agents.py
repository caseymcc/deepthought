import json
from enum import Enum

class AgentType(Enum):
    Assistant = 1
    UserProxy = 2
AgentTypeEnum = {type.name: type.value for type in AgentType}

class AgentConfig:
    def __init__(self, name, type, server_name, system_message):
        self.name = name
        self.type = AgentTypeEnum[type]
        self.server_name = server_name
        self.system_message = system_message
    def __repr__(self):
        return f"Agent(name={self.name}, server_name={self.server_name}, system_message={self.system_message})"

class AgentsConfig:
    def __init__(self):
        self.agents = []

    def load(self, filename):
        with open("agents.json", "r") as file:
            agents_data = json.load(file)
        self.agents = [AgentConfig(**agent_data) for agent_data in agents_data]

    def get_agent(self, name):
        for agent in self.agents:
            if agent.name == name:
                return agent
        return None

class Agent:
    def __init__(self, name, system_message):
        self.name = name
        self.system_message = system_message
        self.server = None

    def __repr__(self):
        return f"Agent(name={self.name}, system_message={self.system_message} server={self.server})"

