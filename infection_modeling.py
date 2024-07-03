# import SEIR_modeling as seir
import networkx as nx
import random


class Infection:
    def __init__(self, infectionCoefficient, recoveryCoefficient, immunityCoefficient):
        self.infectionCoefficient = infectionCoefficient
        self.recoveryCoefficient = recoveryCoefficient
        self.immunityCoefficient = immunityCoefficient
        self.totalInfected = 0
        self.totalRecovered = 0
        self.totalCasualties = 0


class Person:
    def __init__(self):
        self.susceptible = True
        self.exposed = False
        self.infected = False
        self.alive = True

    def infect(self, infectionCoefficient):
        if self.alive and self.susceptible and self.exposed and not self.infected:
            infected = random.random() <= infectionCoefficient
            if infected:
                self.infected = True


class Town:
    def __init__(self, location):
        self.location = location

        self.population = []
        self.max_population = 0

    def add_resident(self, person):
        if person not in self.population:
            self.population.append(person)

        if len(self.population) > self.max_population:
            self.max_population = len(self.population)

    def subtract_resident(self, person):
        self.population.remove(person)


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

    def show_neighbors(self):
        for town in self.towns:
            print(f"Town {town}'s Neighbors: {list(self.connections.neighbors(town))}")


world = World()
world.add_town('A')
world.add_town('B')
world.add_town('C')
world.add_town('D')
world.add_town('E')
world.add_town('F')
world.add_town_connection('A', 'B')
world.add_town_connection('A', 'C')
world.add_town_connection('A', 'D')
world.add_town_connection('B', 'E')
world.add_town_connection('B', 'D')
world.add_town_connection('C', 'D')
world.add_town_connection('D', 'E')
world.add_town_connection('E', 'F')

world.show_neighbors()