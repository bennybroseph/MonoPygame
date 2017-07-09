from component import *

class Behaviour(Component):
    def __init__(self, tag = "", name = "New Behaviour"):
        Component.__init__(self, tag, name)

        self.enabled = True

class MonoBehaviour(Behaviour):
    def __init__(self, tag = "", name = "New MonoBehaviour"):
        Component.__init__(self, tag, name)