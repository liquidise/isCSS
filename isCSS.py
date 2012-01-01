from BeautifulSoup import BeautifulSoup
import argparse, re, string

def cleanInput( styles, regex ):
	retval = []
	for style in re.split( regex, styles ):
		cleanStyle = style.strip()
		if cleanStyle:
			retval += [ cleanStyle ]

	retval.sort()
	return retval

def printCSS( name, styles ):
	print "." + name + " {\n\t" + string.join( styles, ";\n\t" ) + ";\n}"


args = argparse.ArgumentParser()
args.add_argument( "--html", required = True )
args.add_argument( "--css", required = False )

htmlF = open( args.parse_args().html, "r+" )

cssPath = args.parse_args().css
if cssPath:
	cssF = open( cssPath, "r+" )

soup = BeautifulSoup( htmlF )

count = 0
for element in soup.findAll( attrs={"style": re.compile(".*")} ):
	classes = None
	newClassName = None
	styles = cleanInput( element['style'], ";" )

	if "is" in element:
		newClassName = element['is']
	elif "id" in element:
		newClassName = element['id']
	else:
		newClassName = "newClass" + str(count)
		count += 1

	if "class" in element:
		print element['class']
		element['class'] += " " + newClassName
	else:
		element['class'] = newClassName

	printCSS( newClassName, styles )
	del element['style']

htmlF.write( str(soup) )
