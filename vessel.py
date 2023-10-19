class Vaisseau:
    def _init_(self, coordinates, max_hits, weapon):
        self.coordinates = coordinates
        self.max_hits = max_hits
        self.weapon = weapon

    def go_to(self, x, y, z):

        pass

    def get_coordinates(self):

        return self.coordinates

    def fire_at(self, x, y, z):

        pass
class Cruiser(Vaisseau):
    def _init_(self, x=0, y=0):
        coordinates = (x, y, 0)
        max_hits = 6
        weapon = "Anti-air"
        super()._init_(coordinates, max_hits, weapon)


class Submarine(Vaisseau):
    def _init_(self, x=0, y=0, z=-1):
        coordinates = (x, y, z)
        max_hits = 2
        weapon = "Lance-torpilles"
        super()._init_(coordinates, max_hits, weapon)


class Fregate(Vaisseau):
    def _init_(self, x=0, y=0):
        coordinates = (x, y, 0)
        max_hits = 5
        weapon = "Lance-missiles antisurface"
        super()._init_(coordinates, max_hits, weapon)


class Destroyer(Vaisseau):
    def _init_(self, x=0, y=0):
        coordinates = (x, y, 0)
        max_hits = 4
        weapon = "Lance-torpilles"
        super()._init_(coordinates, max_hits, weapon)


class Aircraft(Vaisseau):
    def _init_(self, x=0, y=0, z=1):
        coordinates = (x, y, z)
        max_hits = 1
        weapon = "Lance-missiles antisurface"
        super()._init_(coordinates, max_hits, weapon)