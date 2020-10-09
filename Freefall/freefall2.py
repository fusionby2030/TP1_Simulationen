import numpy as np
import itertools as it
import matplotlib.pyplot as plt

class Particle:
    """ A class representing a 2-d particle """

    def __init__(self, x0, y0, vx0, vy0, radius=0.01, lattice=True):
        self.r = np.array((x0, y0))
        self.v = np.array((vx0, vy0))
        self.radius = radius
        self.lattice = lattice

    @property
    def x(self):
        return self.r[0]

    @x.setter
    def x(self, value):
        self.r[0] = value

    @property
    def y(self):
        return self.r[1]

    @y.setter
    def y(self, value):
        self.r[1] = value

    @property
    def vx(self):
        return self.v[0]

    @vx.setter
    def vx(self, value):
        self.v[0] = value

    @property
    def vy(self):
        return self.v[1]

    @vy.setter
    def vy(self, value):
        self.v[1] = value

    def collision(self, other):
        """ Does the circle of this particle overlap with another? """
        return np.hypot(*(self.r - other.r)) < self.radius + other.radius

    def advance(self, dt):
        if self.lattice:
            pass
        else:
            # if self.y + self.radius < self.radius:
                # self.vy = - self.vy
                # pass

            self.y += self.vy * dt - 0.5 * g * dt ** 2
            self.vy += -g * dt


class Simulation:
    """ A class for elastic or inelastic collisions
     the domain is carried out on height = 25? """

    def __init__(self, n, radius=0.5):
        """
        Initialize the simulation with n Particles with radii raduis
        """
        self.init_particles(n, radius)

    def init_particles(self, n, radius):
        """
        Initialize the n particles of te simulation.
        Positions are on the same x axis, however y's are evenly spaced by some height
        """

        self.n = n
        self.particles = []
        height = 0.0
        increment = 2.0
        for _ in range(self.n):
            x = 5.0
            y = height
            vx, vy = 0.0, 0.0
            if height == increment * (n - 1):
                particle = Particle(x, y, vx, vy, radius, lattice=False)
            else:
                particle = Particle(x, y, vx, vy, radius)
            self.particles.append(particle)
            height += increment

    def handle_collisions(self):

        pairs = it.combinations(range(self.n), 2)
        for i, j in pairs:
            if self.particles[i].collision(self.particles[j]):
                print('\n# COLLISION ALLERT COLLISION ALERT HALLO DU SPIESER \n \n #############')
                self.particles[i].lattice = False
                self.particles[j].lattice = False
                self.particles[i].v, self.particles[j].v = self.particles[j].v, self.particles[i].v
                print(self.positions)
                print(self.velocities)

    def advance(self, dt):
        for i, p in enumerate(self.particles):
            p.advance(dt)
        self.handle_collisions()



    @property
    def positions(self):
        return np.array([p.r for p in self.particles])

    @property
    def velocities(self):
        return np.array([p.v for p in self.particles])

    def simulate(self, dt=0.005, timesteps=1000):
        y_positions = []
        y_velocities = []
        print('\n# Initial Positions')
        print(sim.positions)
        print('\n# Initial Velocities')
        print(sim.velocities)
        for _ in range(timesteps):
            self.advance(dt)
            if _ % 100 == 0:
                print('\n# positions & velocities after t =  {}'.format(_*dt))
                print(self.positions)
                print('\n')
                print(self.velocities)
            y_positions.append(self.positions[0:self.n, 1])
            y_velocities.append(self.velocities[0:self.n, 1])
        y_positions = np.array(y_positions)
        y_velocities = np.array(y_velocities)
        time_range = np.arange(0, dt*timesteps, step=dt)
        self.draw_graph(y_positions, time_range)
        self.draw_graph(y_velocities, time_range)

    def draw_graph(self, positions, y):
        for _ in range(self.n):
            p = np.array(positions[:, _])
            plt.plot(y, p)
        plt.show()





if __name__ == '__main__':
    nparticles = 30
    raddi = 0.05
    g = 10.0
    sim = Simulation(nparticles, raddi)
    sim.simulate()
