import argparse, re, string

def parseStyleAndClass( line ):
	tagName = re.search( "<([a-z]+)", line ).group(1)
	classAttr = re.search( "class\s*=\s*['\"]([^'\"]*)['\"]", line )
	styleAttr = re.search( "style\s*=\s*['\"]([^'\"]*)['\"]", line )

	retval = {}
	if styleAttr:
		retval["styleAttr"] = cleanInput( styleAttr.group(1), ";" )
	if classAttr:
		retval["classAttr"] = cleanInput( classAttr.group(1), "\s+" )

	print tagName,

	return retval

def cleanInput( styles, regex ):
	retval = []
	for style in re.split( regex, styles ):
		cleanStyle = style.strip()
		if cleanStyle:
			retval += [ cleanStyle ]

	retval.sort()
	return retval

args = argparse.ArgumentParser()
args.add_argument( "--html", required = True )
args.add_argument( "--css", required = False )

htmlPath = args.parse_args().html
cssPath = args.parse_args().css

htmlF = open( htmlPath, "r+" )
if cssPath:
	cssF = open( cssPath, "r+" )

for line in htmlF:
	if re.search("<[a-z]+[^>]+style\s*=\s*", line):
		print parseStyleAndClass( line )
