from complex_types import Bounds
from component import Component

class Collider(Component):
    def __init__(self, bounds = Bounds()):
        assert(bounds, Bounds)

        Component.__init__(self)

        self.enabled = True

        self.isTrigger = False
        self.bounds = bounds

    def update(self):
        if not self.enabled:
            return
        #TODO: Update stuff
