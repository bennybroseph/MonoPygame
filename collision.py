from complex_types import *
from component import *

class Collider(Component):
    def __init__(self, bounds = Bounds()):
        Component.__init__(self)
        
        self.enabled = True

        self.isTrigger = False
        self.bounds = bounds

    def update(self):
        if not self.enabled:
            return
