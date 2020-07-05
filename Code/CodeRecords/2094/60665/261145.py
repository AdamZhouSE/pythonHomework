import re

if re.match(r' *[+-]?[0-9]*(\.[0-9]+)?(e[+-]?[0-9]+)? *$',input()) is not None:
	print(True)
else:
	print(False)