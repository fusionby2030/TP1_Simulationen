import numpy as np


class Particle:
    """ A class representing a 1d particle """

    def __init__(self, y, vy, lattice=True):
        self.position = np.array(y, dtype='float32')
        self.velocity = np.array(vy, dtype='float32')
        self.lattice = lattice

    @property
    def y(self):
        return self.position

    @y.setter
    def y(self, value):
        self.position = value

    @property
    def vy(self):
        return self.velocity

    @vy.setter
    def vy(self, value):
        self.velocity = value

    def collision(self, particle2):
        return self.y == particle2.y

    def advance(self, dt):
        if self.lattice:
            pass
        else:
            self.y = self.y + self.vy*dt - 0.5 * g * dt ** 2
            self.vy = self.vy - g * dt


class Simulation:
    """ A class for simple Free Fall simulation"""

    def __init__(self, n):
        self.n = n
        self.particles = []
        height = 0
        increment = 5
        for _ in range(n):
            if height == increment*(n-1):
                self.particles.append(Particle(height, 0, lattice=False))
            else:
                self.particles.append(Particle(height, 0))
            height += increment

    def advance(self, dt):
        for p in self.particles:
            p.advance(dt)

    def handle_collision(self):
        for p1 in self.particles:
            for p2 in self.particles:
                if p1 == p2:
                    continue
                else:
                    if p1.collision(p2):
                        p1.lattice = False
                        self.particles.remove(p2)
                        p1.vy = 0.5*p2.vy

    @property
    def positions(self):
        return [p.y for p in self.particles]

    def simulate(self):
        dt = 0.01
        time = dt
        print('\n# initial positions')
        print(self.positions)
        for _ in range(101):
            self.advance(dt)
            self.handle_collision()
            if _ % 10 == 0:
                print('\n# positions after t =  {}'.format(time))
                print(self.positions)
            time += dt


if __name__ == '__main__':
    g = 10
    p1 = Particle(10, 0, lattice=False)
    p2 = Particle(8.75, 0)
    print(p1.collision(p2))
    p1.advance(0.5)
    print(p1.y, p1.vy)
    print(p1.collision(p2))
    Sim = Simulation(6)
    Sim.simulate()