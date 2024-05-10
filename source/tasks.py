import json
from enum import Enum

class NodeType(Enum):
    LLM = 1
NodeTypeEnum = {type.name: type.value for type in NodeType}

class AgentNode:
    def __init__(self, name, type):
        self.name = name
        self.type = NodeTypeEnum[type]
    def __repr__(self):
        return f"Node(name={self.name}, type={self.type})"

class ConnectionType(Enum):
    Chat = 1
    DM = 2
ConnnectionTypeEnum = {type.name: type.value for type in ConnectionType}

class Connection:
    def __init__(self, name, type, agents):
        self.name = name
        self.type = ConnnectionTypeEnum[type]
        self.agents = agents

    def __repr__(self):
        return f"Connection(name={self.name}, type={self.type}, agents={self.agents})"

class TaskConfig:
    def __init__(self, name, description, prompt, agents, connections):
        self.name = name
        self.description = description
        self.prompt = prompt
        self.agents = [AgentNode(**agent) for agent in agents]
        self.connections = [Connection(**connection) for connection in connections]

    def __repr__(self):
        return f"Task(name={self.name}, description={self.description}, prompt={self.prompt}, agents={self.agents}, connections={self.connections})"

class TasksConfig:
    def __init__(self):
        self.tasks = []

    def load(self, filename):
        with open("tasks.json", "r") as file:
            json_data = json.load(file)
        self.tasks = [TaskConfig(**json_object) for json_object in json_data]

class Task:
    def __init__(self, name, description, prompt, agents, connections):
        self.name = name
        self.description = description
        self.prompt = prompt
        self.agents = []
        self.connections = []

    def __repr__(self):
        return f"Task(name={self.name}, description={self.description}, prompt={self.prompt}, agents={self.agents}, connections={self.connections})"