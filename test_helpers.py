import numpy as np
from warnings import warn

# Here are a couple of boilerplate sanity check functions I use 
# all the time in daily work and keep stored in a module in my PYTHONPATH

def test_sensible_values(array, minval, maxval, 
	called_funcname=None, array_name=''):
	""" Helper function for testing whether some other, external function 
	was passed a reasonable set of inputs. 

	Parameters 
	----------
	array : array 
		Input set of values to the external function. 

	minval : float or int 
		Minimum value that would have been reasonable to pass to the external function. 

	maxval : float or int 
		Maximum value that would have been reasonable to pass to the external function. 

	called_funcname : string, optional 
		Name of the external function whose inputs are being tested. 
		Provides a convenient way to quickly zero in on potential bugs by helping 
		to construct an informative error and/or warning message. 

	array_name : string, optional 
		Variable name of the array whose values are being tested. 
		Provides a convenient way to quickly zero in on potential bugs by helping 
		to construct an informative error and/or warning message. 
	"""
	
	msg = ("at least one element of the input array "+array_name+"\n" + 
		"is outside the reasonable range of %.1f to %.1f \n")
	if called_funcname != None:
		msg = "When calling function "+called_funcname+",\n"+msg

	if np.any(array < minval) or (np.any(array > maxval)):
		raise ValueError(msg % (minval, maxval))

def get_array_like(x, array_name='', called_funcname=None):
	""" Function that converts the input x to a numpy array. 

	Parameters 
	----------
	x : object 
		Can be any input that is desired to be converted. 

	array_name : string, optional 
		Variable name of the array to be converted. 
		Provides a convenient way to quickly zero in on potential bugs by helping 
		to construct an informative error and/or warning message. 

	Returns 
	-------
	y : array 
		Numpy array version of input x. 
	"""

	types_to_convert = [list, tuple, float, int]

	if type(x).__module__ == np.__name__:
		return x

	elif type(x) in types_to_convert:
		msg = "Array "+array_name+" should not be list or tuple\n"+"Converting to ndarray"
		if called_funcname != None:
			msg = msg + "\nIn the future, use ndarray inputs for "+called_funcname
		msg = msg + "\nThis message will not be displayed in the future\n"
		if type(x)==list or type(x)==tuple: warn(msg)
		return np.array(x)

	else:
		msg = "Array "+array_name+" has an insensible type = "+str(type(x))+"\n"
		"Should be ndarray, list, tuple, float_like, or int_like"
		if called_funcname!= None:
			msg = msg + "\n when calling function "+called_funcname
		raise TypeError(msg)



