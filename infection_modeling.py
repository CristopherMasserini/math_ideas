import SEIR_modeling as seir
import networkx as nx


class Person:
    def __init__(self):
        self.susceptible = True
        self.exposed = False
        self.infected = False
        self.alive = True


class Town:
    def __init__(self, location):
        self.location = location

        self.population = []
        self.max_population = 0

    def add_resident(self):
        pass

    def subtract_resident(self):
        pass


class World:
    def __init__(self):
        self.towns = []
        self.connections = nx.Graph()

    def add_town(self, town):
        self.towns.append(town)
        self.connections.add_node(town)

    def add_town_connection(self, town1, town2):
        if town1 and town2 in self.towns:
            self.connections.add_edge(town1, town2)
        else:
            print(f'One of the towns does not exist in the World. Towns: {self.towns}')
