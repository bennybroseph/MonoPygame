"""Contains the base Behaviour class and MonoBehaviour class"""
from component import Component

class Behaviour(Component):
    """Basic class which defines a behaviour component"""
    def __init__(self, tag = "", name = "New Behaviour"):
        Component.__init__(self, tag, name)

        self.enabled = True

class MonoBehaviour(Behaviour):
    """Class which defines a MonoBehaviour capable of using custom behaviour"""
    def __init__(self, tag = "", name = "New MonoBehaviour"):
        Component.__init__(self, tag, name)