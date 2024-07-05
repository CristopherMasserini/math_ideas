import infection_modeling as im

import unittest

def test_world():
    world = im.World()

    def test_add_town():
        world.add_town('A')
        world.add_town('B')
        world.add_town('C')
        world.add_town('D')
        world.add_town('E')
        world.add_town('F')

        assert world.towns == ['A', 'B', 'C', 'D', 'E', 'F']

    def test_add_town_connection():
        connected = world.add_town_connection('A', 'B')
        connectedFalse = world.add_town_connection('A', 'K')

        assert connected is True
        assert connectedFalse is False

    def test_is_neighbor():
        world.add_town_connection('A', 'C')
        world.add_town_connection('A', 'E')

        assert world.is_neighbor('A', 'B') is True
        assert world.is_neighbor('B', 'E') is False

    test_add_town()
    test_add_town_connection()
    test_is_neighbor()



