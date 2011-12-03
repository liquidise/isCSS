import argparse, re, string

args = argparse.ArgumentParser()
args.add_argument( "--html", required = True )
args.add_argument( "--css", required = False )

htmlPath = args.parse_args().html
cssPath = args.parse_args().css

htmlF = open( htmlPath, 'rw' )

for line in htmlF:
	if re.search("<[a-z]+[^>]+style\s*=\s*", line):
		print line,