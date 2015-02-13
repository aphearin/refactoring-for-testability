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
	conc = np.where(logmass < 10, 4, logmass**0.445)
	return conc

def conc_mass_whatever(logmass):
	return logmass

#####################

def retrieve_model(modelname, testmode=False):
	""" Function whose sole purpose is to retrieve the requested model
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

##################### PRIMARY METHOD #####################

def conc_mass(logmass, modelname=None, testmode=False):

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


