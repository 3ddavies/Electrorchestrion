import argparse
verbpa = argparse.ArgumentParser()
verbpa.add_argument('-v', '--verbose', action="store_true", help="enables verbose output (debug)")
vera = verbpa.parse_args()
if vera.verbose:
	def verpri(stuff):
		print(stuff)
else:
	def verpri(stuff):
		pass
