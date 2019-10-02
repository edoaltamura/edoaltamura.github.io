from map_plot_parameters import set_defaults_plot
from matplotlib import pyplot as plt
from os import getcwd, chdir
import numpy as np
from astropy.constants import c

# Initialise the parameters
set_defaults_plot()
chdir('C://Users//edoar//OneDrive//Documenti//OPTICON 2019//QUASARS//.')
print('PWD:\t', getcwd())

def catalogue_pick(ID_spec):
	# Reconver the catalogue of quasars	
	cat =  ['Gaia_QSO_1114+1549',
			'Gaia_QSO_1112+1410', 
			'Gaia_QSO_1103+1325', 
			'Gaia_QSO_1327+3527', 
			'Gaia_QSO_1314+3421', 
			'Gaia_QSO_1456+3152',
			'Gaia_QSO_1309+2904', 
			'Gaia_QSO_1505+3317',
			'Gaia_QSO_1237+1233', 
			'Gaia_QSO_1218+0832', 
			'Gaia_QSO_1213+1420', 
			'Gaia_QSO_1203+1118', 
			'Gaia_QSO_1203+0652', 
			'Gaia_QSO_1100+1310',
			'Gaia_QSO_1144+1235']
	
	return str(cat[int(ID_spec)])


def recover_spec(ID_spec, format_ = 'array'):
	file_name = 'flux_' + catalogue_pick(ID_spec) + '.tab'
	print('QSO:\t', catalogue_pick(ID_spec), '\t\tOpening file...')
	f = open(file_name, 'r')

	# Ignore headers
	# header1 = f.readline()
	# header2 = f.readline()
	# header3 = f.readline()
	data = []
	for line in f:
	    line = line.strip()
	    columns = line.split()

	    # Initialise line-handler
	    source = {}
	    source['lambda'] = float(columns[0])
	    source['flux'] = float(columns[1])
	    data.append(source)
                                                 
	# Return array of dictionaries
	if format_ == 'dict':
		return data
	elif format_ == 'array':
		wavelength = [data[i]['lambda'] for i in range(len(data))]
		flux = [data[i]['flux'] for i in range(len(data))]
		return np.asarray(wavelength), np.asarray(flux)

def smooth(y, box_pts):
    box = np.ones(box_pts)/box_pts
    y_smooth = np.convolve(y, box, mode='same')                                                                                  
    return y_smooth

def doppler_shift(wavelength, redshift):
	return wavelength / (redshift*c.value)

def init_plot():
	# Initialise plot with common features
	fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(17, 10))	
	axes.set_xlabel(r'$\lambda \qquad\mathrm{[A]}$')
	axes.set_ylabel(r'$Flux \qquad \mathrm{[mJy]}$')
	return fig, axes

def quick_plot(ID_spec):	
	x, y = recover_spec(ID_spec, format_='array')
	# x = doppler_shift(x, 3.5)
	y = smooth(y, 10)
	fig, axes = init_plot()
	axes.plot(x,y, c = 'b', linewidth=1, linestyle='-')
	plt.show()

quick_plot(11)