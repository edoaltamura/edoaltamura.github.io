def set_defaults_plot():

	from matplotlib import rc, rcParams
	rc('text', usetex=0)
	rc('savefig', dpi=100)       # higher res outputs

	### AXES
	rcParams['axes.facecolor']	= 'white'   # axes background color
	rcParams['axes.edgecolor']	= 'k'   # axes edge color
	rcParams['axes.linewidth']	= 0.8     # edge linewidth
	rcParams['axes.grid']		= False   # display grid or not
	rcParams['axes.titlesize']	= 'large'   # fontsize of the axes title
	rcParams['axes.titlepad']	=  6.0     # pad between axes and title in points
	rcParams['axes.labelsize']	=  17  # fontsize of the x any y labels
	rcParams['axes.labelpad']	=  7.0     # space between label and axis


	### TICKS
	# see http://matplotlib.org/api/axis_api.html#matplotlib.axis.Tick
	rcParams['xtick.top']           = False   # draw ticks on the top side
	rcParams['xtick.bottom']        = True   # draw ticks on the bottom side
	rcParams['xtick.major.size']    = 3.5      # major tick size in points
	rcParams['xtick.minor.size']    = 2      # minor tick size in points
	rcParams['xtick.major.width']   = 0.8    # major tick width in points
	rcParams['xtick.minor.width']   = 0.6    # minor tick width in points
	rcParams['xtick.major.pad']     = 3.5      # distance to major tick label in points
	rcParams['xtick.minor.pad']     = 3.4      # distance to the minor tick label in points
	rcParams['xtick.color']         = 'k'      # color of the tick labels
	rcParams['xtick.labelsize']     = 17 #'large' # fontsize of the tick labels
	rcParams['xtick.direction']     = 'out'    # direction: in, out, or inout
	rcParams['xtick.minor.visible'] = False  # visibility of minor ticks on x-axis
	rcParams['xtick.major.top']     = True   # draw x axis top major ticks
	rcParams['xtick.major.bottom']  = True   # draw x axis bottom major ticks
	rcParams['xtick.minor.top']     = True   # draw x axis top minor ticks
	rcParams['xtick.minor.bottom']  = True   # draw x axis bottom minor ticks

	rcParams['ytick.left']          = True   # draw ticks on the left side
	rcParams['ytick.right']         = False  # draw ticks on the right side
	rcParams['ytick.major.size']    = 3.5      # major tick size in points
	rcParams['ytick.minor.size']    = 2      # minor tick size in points
	rcParams['ytick.major.width']   = 0.8    # major tick width in points
	rcParams['ytick.minor.width']   = 0.6    # minor tick width in points
	rcParams['ytick.major.pad']     = 3.5      # distance to major tick label in points
	rcParams['ytick.minor.pad']     = 3.4      # distance to the minor tick label in points
	rcParams['ytick.color']         = 'k'      # color of the tick labels
	rcParams['ytick.labelsize']     = 17 #'large' # fontsize of the tick labels
	rcParams['ytick.direction']     = 'out'    # direction: in, out, or inout
	rcParams['ytick.minor.visible'] = False  # visibility of minor ticks on y-axis
	rcParams['ytick.major.left']    = True   # draw y axis left major ticks
	rcParams['ytick.major.right']   = True   # draw y axis right major ticks
	rcParams['ytick.minor.left']    = True   # draw y axis left minor ticks
	rcParams['ytick.minor.right']   = True   # draw y axis right minor ticks

	### GRIDS
	rcParams['grid.color']       =   'k'    # grid color
	rcParams['grid.linestyle']   =   '--'         # dashed
	rcParams['grid.linewidth']   =   0.6       # in points
	rcParams['grid.alpha']       =   0.2       # transparency, between 0.0 and 1.0

	### FIGURE
	# See http://matplotlib.org/api/figure_api.html#matplotlib.figure.Figure
	rcParams['figure.titlesize'] = 'large'      # size of the figure title (Figure.suptitle())
	rcParams['figure.titleweight'] = 'normal'   # weight of the figure title
	rcParams['figure.figsize']   = 6.4, 4.8   # figure size in inches
	rcParams['figure.dpi']       = 100      # figure dots per inch
	rcParams['figure.facecolor'] = 'white'   # figure facecolor; 0.75 is scalar gray
	rcParams['figure.edgecolor'] = 'white'   # figure edgecolor
	rcParams['figure.autolayout'] = True  # When True, automatically adjust subplot
	                            # parameters to make the plot fit the figure
	rcParams['figure.max_open_warning'] = 20  # The maximum number of figures to open through
	                               # the pyplot interface before emitting a warning.
	                               # If less than one this feature is disabled.


	rcParams['text.color'] = 'white'
	rcParams['axes.labelcolor'] = 'k'

def test_plot():
	import numpy as np
	from matplotlib import pyplot as plt
	mean = [0, 0]
	cov = [[1, 1], [1, 2]]
	x, y = np.random.multivariate_normal(mean, cov, 10000).T
	plt.hist2d(x, y, bins=30, cmap='Blues')
	cb = plt.colorbar()
	cb.set_label(r'$\mathrm{counts\ in\ bin}$')
	plt.show()

def test_plot_smoothed():
	from scipy.stats import gaussian_kde
	import numpy as np
	from matplotlib import pyplot as plt
	mean = [0, 0]
	cov = [[1, 1], [1, 2]]
	x, y = np.random.multivariate_normal(mean, cov, 10000).T
	# fit an array of size [Ndim, Nsamples]
	data = np.vstack([x, y])
	kde = gaussian_kde(data)

	# evaluate on a regular grid
	xgrid = np.linspace(-3.5, 3.5, 100)
	ygrid = np.linspace(-6, 6, 100)
	Xgrid, Ygrid = np.meshgrid(xgrid, ygrid)
	Z = kde.evaluate(np.vstack([Xgrid.ravel(), Ygrid.ravel()]))

	# Plot the result as an image
	plt.imshow(Z.reshape(Xgrid.shape),
	           origin='lower', aspect='auto',
	           extent=[-3.5, 3.5, -6, 6],
	           cmap='Blues')
	cb = plt.colorbar()
	cb.set_label("density")
	plt.show()


"""
# Example of implementation
set_defaults_plot()
test_plot()
"""