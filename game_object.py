from pygame_object import PygameObject
from transform import Transform, Component

class GameObject(PygameObject):
    _gameObjects = []

    def __init__(self, tag = "", name = "New GameObject"):
        assert isinstance(tag, str)

        PygameObject.__init__(self, name)

        self.tag = tag
        self.transform = Transform()

        self._components = [self.transform]

        GameObject._gameObjects.append(self)

    def update(self):
        """Updates the gameobject and all components"""
        for component in self._components:
            component.update()

    def add_component(self, component):
        if isinstance(component, type):
            component = component()

        assert isinstance(component, Component)

        self._components.append(component)
        component.gameObject = self

        return component

    def get_component(self, type):
        """Grabs a component by 'type'"""
        for component in self._components:
            if isinstance(component, type):
                return component

        return None

    def __del__(self):
        GameObject._gameObjects.remove(self)