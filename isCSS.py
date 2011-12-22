import argparse, re, string

def parseStyleAndClass( line ):
	classAttr = re.search( "class\s*=\s*['\"]([^'\"]*)['\"]", line )
	styleAttr = re.search( "style\s*=\s*['\"]([^'\"]*)['\"]", line )

	retval = {}
	if styleAttr:
		retval["styleAttr"] = cleanStyles( styleAttr.group(1) )
	if classAttr:
		retval["classAttr"] = classAttr.group(1)

	return retval

def cleanStyles( styles ):
    retval = []
    for style in styles.split(";"):
        cleanStyle = style.strip()
        if cleanStyle:
            retval.append( cleanStyle )

    return retval

# def injectClasses( line ):

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
