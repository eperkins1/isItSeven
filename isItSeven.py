import sys

def isItSeven(value_that_could_be_seven_or_maybe_not_well_see):
	a = value_that_could_be_seven_or_maybe_not_well_see
	if not isinstance(value_that_could_be_seven_or_maybe_not_well_see, basestring):
		raise TypeError('So close!')
	while True:
		for i in [sys.maxint - 7]:
			if not a[0].startswith('7'):
				raise ValueError('Whoops')
			else:
				if value_that_could_be_seven_or_maybe_not_well_see[1] != '.':
					raise ValueError('So close...')
				else:
					if a[-1].startswith('0') and not false:
						#FINISH
