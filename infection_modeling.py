# import SEIR_modeling as seir
import networkx as nx
import random


class Infection:
    def __init__(self, infectionCoefficient, mortalityCoefficient, immunityCoefficient):
        self.infectionCoefficient = infectionCoefficient
        self.mortalityCoefficient = mortalityCoefficient
        self.immunityCoefficient = immunityCoefficient
        # self.totalInfected = 0
        # self.totalRecovered = 0
        # self.totalCasualties = 0


class Person:
    def __init__(self):
        self.susceptible = True
        self.exposed = False
        self.infected = False
        self.alive = True

    def get_infected(self, infectionCoefficient):
        if self.alive and self.susceptible and self.exposed and not self.infected:
            infected = random.random() <= infectionCoefficient
            if infected:
                self.infected = True
                self.susceptible = False

    def infect_other(self, other, infectionCoefficient):
        if self.infected:
            other.exposed = True
            other.get_infected(infectionCoefficient)

    def recover(self, immunityCoefficient):
        if random.random() <= immunityCoefficient:
            self.susceptible = False
        else:
            self.susceptible = True

        self.exposed = False
        self.infected = False

    def mortality(self, mortalityCoefficient):
        if random.random() <= mortalityCoefficient:
            self.alive = False



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
            return True
        else:
            print(f'One of the towns does not exist in the World. Towns: {self.towns}')
            return False

    def show_neighbors(self):
        for town in self.towns:
            print(f"Town {town}'s Neighbors: {list(self.connections.neighbors(town))}")

    def is_neighbor(self, town1, town2):
        neighbors = list(self.connections.neighbors(town1))
        return town2 in neighbors

