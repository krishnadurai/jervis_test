import sys
from contextlib import contextmanager
from StringIO import StringIO

@contextmanager
def captured_output():
	''' Function for safely stealing output and errors from the
		standard console.
	'''
	new_out, new_err = StringIO(), StringIO()
	old_out, old_err = sys.stdout, sys.stderr
	try:
		sys.stdout, sys.stderr = new_out, new_err
		yield sys.stdout, sys.stderr
	finally:
		sys.stdout, sys.stderr = old_out, old_err

cook_string_for_list = lambda to_str_list: ' '.join(\
							[str(item) for item in to_str_list])
