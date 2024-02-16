class ParticleSimulator:
    def __init__(self, particles):
        self.particles = particles
    
    def evolve(self, dt):
        timestep = 0.00001
        nsteps = int(dt/timestep)

        for p in self.particles:
            t_x_ang = timestep * p.ang_vel
            for i in range(nsteps):
                # calculate the direction
                norm = (p.x**2 + p.y**2)**0.5
                p.x, p.y = (p.x - t_x_ang * p.y/norm, p.y + t_x_ang * p.x/norm)