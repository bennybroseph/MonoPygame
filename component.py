from pygame_object import PygameObject

class Component(PygameObject):
    _components = []

    @staticmethod
    def _awake():
        for component in Component._components:
            if not component._isAwake:
                component.awake()
                component._isAwake = True
    @staticmethod
    def _start():
        for component in Component._components:
            if not component._isStarted:
                component.start()
                component._isStarted = True
    @staticmethod
    def _fixed_update():
        for component in Component._components:
            component.fixed_update()
    @staticmethod
    def _update():
        for component in Component._components:
            component.update()
    @staticmethod
    def _late_update():
        for component in Component._components:
            component.late_update()

    def __init__(self, name = "New Component"):

        PygameObject.__init__(self, name)

        self._isAwake = False
        self._isStarted = False

        self.gameObject = None

        Component._components.append(self)

    @property
    def transform(self):
        return self.gameObject.transform

    @property
    def tag(self):
        return self.gameObject.tag

    def awake(self):
        """Called when the component is created"""
        pass
    def start(self):
        """Called after start"""
        pass
    def fixed_update(self):
        """Updates the component each physics step"""
        pass
    def update(self):
        """Updates the component once per frame"""
        pass
    def late_update(self):
        """Called after update"""
        pass

    def __del__(self):
        Component._components.remove(self)