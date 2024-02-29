"""Benchmark the performance of the particle simulator.+"""
from random import uniform

from particle import Particle
from particle_simulator import ParticleSimulator

def benchmark(npart=100, method='python'):
    particles = [
        Particle(uniform(-1.0, 1.0), uniform(-1.0, 1.0), uniform(-1.0, 1.0))
        for i in range(npart)
    ]

    simulator = ParticleSimulator(particles)
    
    if method == 'python':
        simulator.evolve_python(0.1)
    
    elif method == 'numpy':
        simulator.evolve_numpy(0.1)

if __name__ == '__main__':
    benchmark()