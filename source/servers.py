import json

class ServerConfig:
    def __init__(self, name, url, model_name, model_type, api_type, api_token):
        self.name = name
        self.url = url
        self.model_name = model_name
        self.model_type = model_type
        self.api_type = api_type
        self.api_token = api_token
    def __repr__(self):
        return f"Agent(name={self.name}, url={self.url}, model_name={self.model_name}, model_type={self.model_type},
            api_type={self.api_type}, api_token={self.api_token})"


class ServersConfig:
    def __init__(self):
        self.agents = []

    def load(self, filename):
        with open("servers.json", "r") as file:
            json_data = json.load(file)
        self.agents = [ServerConfig(**server_data) for server_data in json_data]

class Server:
    def __init__(self, name, url, model_name, model_type, api_type, api_token):
        self.name = name
        self.url = url
        self.model_name = model_name
        self.model_type = model_type
        self.api_type = api_type
        self.api_token = api_token

    def __repr__(self):
        return f"Agent(name={self.name}, url={self.url}, model_name={self.model_name}, model_type={self.model_type},
            api_type={self.api_type}, api_token={self.api_token})"