from matplotlib import pyplot as plt
from matplotlib import animation

def visualize(simulator):
    X = [p.x for p in simulator.particles]
    Y = [p.y for p in simulator.particles]

    fig = plt.figure()
    ax = plt.subplot(111, aspect='equal')
    line, = ax.plot(X, Y, 'ro')

    # Axis limits
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)

    def init():
        line.set_data([], [])
        return line,
    
    def animate(i):
        # let the particle evolve for 0.01 time units
        simulator.evolve_numpy(0.01)
        X = [p.x for p in simulator.particles]
        Y = [p.y for p in simulator.particles]

        line.set_data(X, Y)
        return line,
    
    anim = animation.FuncAnimation(fig, animate, init_func=init, blit=True, interval=10, cache_frame_data=False)
    plt.show()