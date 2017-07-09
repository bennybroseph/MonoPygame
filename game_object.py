from pygame_object import *
from component import *

class GameObject(PygameObject):
    def __init__(self, name = "New GameObject"):
        PygameObject.__init__(self, name)
        
        self._components = [Component] * 0

    def update(self):
        """Updates the gameobject and all components"""
        for component in self._components:
            component.update()

    def add_component(self, component):
        self._components.append(component)

    def get_component(self, type):
        """
        Grabs a component by 'type'
        """
        for component in self._components:
            if isinstance(component, type):
                return component

        return None