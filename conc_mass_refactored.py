import numpy as np
from math import sqrt
from warnings import warn
import test_helpers

###########################################################################################

def conc_mass_orig(loglogmass, modelname):

	if modelnamename=='dutton_macchio14':
		if logmass < 10:
			conc=4
		else:
			conc = logmass**0.05
	else:
		if logmass < 10:
			conc=4
		else:
			conc = 4.*logmass/4

	return conc


###########################################################################################
# Refactored version below
###########################################################################################


#####################  SOME SPECIFIC MODELS #####################
def conc_mass_dutton_macchio14(logmass):
	""" Concentration-mass model calibrated in Dutton & Macchio (2014). 

	Parameters 
	----------
	logmass : array 
		Halo masses, specified in logarithmic units. 

	Returns 
	-------
	conc : array 
		Halo concentrations. 
	"""

	conc = np.where(logmass < 10, 4, logmass**0.445)
	return conc

def conc_mass_whatever(logmass):
	return logmass

#####################

####################################################################
############## PRIMARY METHOD CALLED BY OUTSIDE WORLD ##############

def conc_mass(logmass, modelname=None, testmode=False):
	""" Function specifying the relationship between halo mass and 
	NFW profile concentration. Multiple models are supported, including 
	Dutton & Macchio (2014), and whatever. 

	Parameters 
	----------
	logmass : array 
		Halo masses, specified in logarithmic units. 

	modelname : string, optional 
		String used to specify which model is chosen. 
		If None, the default model will be selected.
		The default model is set in the retrieve_model function. 

	testmode : bool, optional 
		If set to True, the code will run in Test Mode, and many sanity 
		checks will be performed while the functions evaluate. 

	Returns 
	-------
	conc : array 
		Halo concentrations. 

	"""

	# First make sure the input is a numpy type object
	# If not, convert it. 
	logmass = test_helpers.get_array_like(logmass, 
		array_name='logmass', 
		called_funcname='conc_mass')

	# Now do some sanity checks in the event that we are running in testmode
	if testmode==True: 
		test_helpers.test_sensible_values(
		logmass, 0.1, 100, 
		called_funcname='conc_mass', array_name = 'logmass')

	# Grab the model we want based on the input modelname
	conc_function = retrieve_model(modelname, testmode)

	return conc_function(logmass)

####################################################################

def retrieve_model(modelname, testmode=False):
	""" Function whose sole purpose is to retrieve the requested model. 

	Parameters 
	----------
	modelname : string 

	testmode : bool, optional 
		If set to True, the code will run in Test Mode, and many sanity 
		checks will be performed while the functions evaluate. 

	Returns 
	-------
	model : function object 

	"""
	default_model = conc_mass_dutton_macchio14

	if modelname=='dutton_macchio14': 
		return conc_mass_dutton_macchio14

	elif modelname=='whatever':
		return conc_mass_whatever

	elif modelname==None:
		msg = "No modelname provided. Choosing default = "+default_model.__name__
		if testmode==True: print(msg)
		return default_model

	else:
		msg = ("Input modelname does not correspond to \n"
			"any of the supported model names, which are "
			"'dutton_macchio14' and 'whatever'\n"
			"Choosing "+default_model.__name__+" as default")
		warn(msg)
		return default_model



