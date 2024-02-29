import numpy as np

class ParticleSimulator:
    def __init__(self, particles):
        self.particles = particles
    
    def evolve_python(self, dt):
        timestep = 0.00001
        nsteps = int(dt/timestep)

        for p in self.particles:
            t_x_ang = timestep * p.ang_vel
            for i in range(nsteps):
                # calculate the direction
                norm = (p.x**2 + p.y**2)**0.5
                p.x, p.y = (p.x - t_x_ang * p.y/norm, p.y + t_x_ang * p.x/norm)
    
    def evolve_numpy(self, dt):
        timestep = 0.00001
        nsteps = int(dt/timestep)

        r_i = np.array([[p.x, p.y] for p in self.particles])
        ang_vel_i = np.array([p.ang_vel for p in self.particles])

        for i in range(nsteps):
            norm_i = np.sqrt((r_i ** 2).sum(axis=1))
            v_i = r_i[:, [1, 0]]
            v_i[:, 0] *= -1
            v_i /= norm_i[:, np.newaxis]
            d_i = timestep * ang_vel_i[:, np.newaxis] * v_i
            r_i += d_i

            for i, p in enumerate(self.particles):
                p.x, p.y = r_i[i]