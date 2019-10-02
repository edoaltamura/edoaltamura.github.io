from colossus.cosmology import cosmology
from colossus.lss import mass_function
import numpy as np
from matplotlib import pyplot as plt
from map_plot_parameters import set_defaults_plot
import matplotlib.animation as animation
from matplotlib.widgets import Slider

# Initialise the parameters
set_defaults_plot()
cosmology.setCosmology('WMAP9')
masses = np.logspace(11, 16, 300)

# Create the figure
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(10, 7))

# Initialise the STATIC figure elements
ax.axvline(x=1e13, color='k', linewidth=1, linestyle='dotted')
ax.set_xlabel(r'$M/\mathrm{M_{\odot}}$', fontsize=20)
ax.set_ylabel(r'$d n/d \ln (M)$', fontsize=20)
ax.set_xscale('log')

# Enter 0 for animation, 1 for statis image
functionality = 1

if functionality:
    ax.plot(masses, mass_function.massFunction(masses, 1., mdef = 'fof', model = 'watson13'), color = 'blue', alpha=1)
    ax.text(1e14, 0.3, r'$z = 1$', fontsize=20, color='k')
    plt.savefig('mass_function.png')
    #plt.show()

else:
    # Initialise the DYNAMIC figure elements
    line, = ax.plot(masses, mass_function.massFunction(masses, 0.0, mdef = 'fof', model = 'watson13'), color = 'red', alpha=0.5)
    line__, = ax.plot([1e13], [mass_function.massFunction(1e13, 0.0, mdef = 'fof', model = 'watson13')], color = 'red', alpha=0.7, marker='o', markersize=10)
    annotation = ax.text(1e14, 0.3, r'$z = 10$', fontsize=20, color='k')



    def init():  # only required for blitting to give a clean slate.
        line.set_ydata([np.nan] * len(masses))
        line__.set_ydata([np.nan])
        annotation.set_text(np.nan)
        return line,annotation

    def animate(i):
        line.set_ydata(mass_function.massFunction(masses, -i/10+10, mdef = 'fof', model = 'watson13'))
        line__.set_ydata(mass_function.massFunction(1e13, -i/10+10, mdef = 'fof', model = 'watson13'))
        annotation.set_text(r'$z = {%.2f}$' % (-i/10+10))
        return line,annotation, line__


    ani = animation.FuncAnimation(
        fig, animate, init_func=init, interval=50, blit=True, save_count=5, frames = range(0, 100, 1))


    # Save video: use ffmpeg encoding
    # Set up formatting for the movie files
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=15, metadata=dict(artist='Edoardo Altamura'), bitrate=1800)
    ani.save('mass_function.mp4', writer=writer)
    plt.show()