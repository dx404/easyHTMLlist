#!/usr/local/bin/python
import sys
import re

# author: Duo Zhao
# line level
# add id class what's that to <ul> or to <li>?
# 

indentSymbol = '  '
def countIndent(textline):
	level = 0
	for c in textline:
		if c != '\t' :
			break
		level = level + 1
	return level

def lineStrip(lineContent):
	line = lineContent
	line = line.lstrip('\t').rstrip('\n')
	return line

def loadLinkAnchor(lineContent):
	line = lineContent
	if '-->' in lineContent:
		text, url = lineContent.split('-->')
		text = text.strip() 
		url = '"' + url.strip() + '"'
		line = '<a href=' + url + '>' + text + '</a>'
	return line
	
def text2htmlList(lineList):
	global indentSymbol
	lineList = lineList + ['']
	levelList = {}
	for num, line in enumerate(lineList):
		levelList[num] = countIndent(line)
	# Add vritual guard indentation level for boundary
	levelList[-1] = -1
	levelList[len(lineList) - 1] = -1
	
	relLevelList = {}
	for num, line in enumerate(lineList):
		relLevelList[num] = levelList[num] - levelList[num - 1]
	
	level = -1	
	for num, line in enumerate(lineList):
		rel_level = relLevelList[num]
		content = lineStrip(lineList[num])
		content = loadLinkAnchor(content)
		if rel_level == 0:
			print '</li>'
		elif rel_level == 1:
			level += 1
			sys.stdout.write('\n' + indentSymbol * level  + '<ul>\n')
			level += 1
		elif rel_level < 0:
			print '</li>'
			print indentSymbol * (level - 1) + '</ul>'
			level -= 2
			for step in reversed(xrange(-rel_level - 1)):
				print indentSymbol * level  + '</li>'
				print indentSymbol * (level - 1) + '</ul>'
				level -= 2
		else:
			print "==== Indentation Error==="		
		
		if content: 
			sys.stdout.write(indentSymbol * level  + '<li>' + content)

def main():
	operation = sys.argv[1]
	lines = []
	if operation == '-f':
		filename = sys.argv[2]
		f = open(filename, 'r')
		for line in f:
			if line:
				lines.append(line)
		text2htmlList(lines)
	elif operation[:2] == '-s':
		stringText = sys.argv[2].strip('\n')
		lines = re.split('\n+', stringText)
		text2htmlList(lines)
	else:
		print "no such an option"

main()
	
