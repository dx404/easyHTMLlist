#!/usr/local/bin/python
'''
Created on Sep 10, 2013

@author: duozhao
The python document works as a parser to tranlate indented text to HTML list format
The parser builds a syntax tree from the input text. By walking the syntax tree in 
depth first search, it emits the HTML list code. 
'''

import sys

class iNode (object):
    indentSymbol = '   '
    
    def __init__(self, level, data, htmlListElement='ul', enableInfo=True):
        self.level = level
        self.data = data
        self.parent = None
        self.childlist = []
        self.htmlListElement = htmlListElement
        self.listStartTag = '<' + htmlListElement + '>'
        self.listEndTag = '</' + htmlListElement + '>'
        self.enableLevelInfo = enableInfo
        self.sourceLine = -1
        self.levelTrace = []
    
    @staticmethod
    def makeNode(text, htmlListElement='ul', enableInfo=True):
        level = 0
        for c in text:
            if c == '\t':
                level += 1
            else:
                break
        
        data = text.lstrip('\t').rstrip('\n')
        return iNode(level, data, htmlListElement, enableInfo)
        
    def walk(self):
        baseIndent = self.indentSymbol * (2 * self.level + 1)
        attribute = \
            ' data-src-line="' + \
                str(self.sourceLine) + '"'\
            ' data-level="' + \
                '-'.join([str(t) for t in self.levelTrace]) + '"' \
            if self.enableLevelInfo else ''
            
        if self.childlist:
            print baseIndent + '<li' + attribute + '>' + self.data
            self.walk_childlist()
            print baseIndent + '</li>'
        else:
            print baseIndent + '<li' + attribute + '>'  + self.data + '</li>'
            
    
    def walk_childlist(self):
        if self.childlist:
            baseIndent = self.indentSymbol * (2 * self.level + 2)
            print baseIndent + self.listStartTag
            for child in self.childlist:
                child.walk()
            print baseIndent + self.listEndTag
            return True
        else:
            return False
            

class iTree (object):
    def __init__(self, htmlListElement, enableInfo):
        self.root = iNode(-1, '', htmlListElement, enableInfo)
        self.root.listStartTag = '<' + self.root.htmlListElement + ' class="duo-list">'
        self.hanger =  self.root
    
    @staticmethod
    def makeTree(text, htmlListElement='ul', enableInfo=True):
        iTreeInstance = iTree(htmlListElement, enableInfo)
        for num, line in enumerate(text.split('\n')):
            node = iNode.makeNode(line, htmlListElement, enableInfo)
            node.sourceLine = num + 1
            iTreeInstance.append(node)
                  
        return iTreeInstance
    
    def append(self, node):
        if node.level == self.hanger.level + 1:
            crossbar = self.hanger.childlist
            crossbar.append(node)
            node.parent = self.hanger
            innerMostOrder = len(crossbar)
            node.levelTrace = self.hanger.levelTrace + [innerMostOrder]
        elif node.level == self.hanger.level + 2:
            self.hanger =  self.hanger.childlist[-1]
            self.append(node)
        elif node.level <= self.hanger.level:
            for i in xrange(self.hanger.level + 1, node.level, -1):
                self.hanger = self.hanger.parent
            self.append(node)
        else:
            errorMsg = '<span style="color:red;">\
                        ==Incorrect indentation (too many indents) at: \
                        Line:' + str(node.sourceLine) + \
                        '-->' + node.data + '</span>'
            node.data = errorMsg
            node.level = self.hanger.level + 1
            self.append(node)
   
    def walk(self):
        self.root.walk_childlist()
        

if __name__ == '__main__':
    print "<!-- HTML nested list Generation Tool by Duo Zhao -->"
    operation = sys.argv[1]
    lines = []  
    htmlListElement = 'ol' if 'o' in operation else 'ul'
    enableInfo = False if 'r' in operation else True
    if operation[:2] == '-f':
        filename = sys.argv[2]
        f = open(filename, 'r')
        text = f.read()
        listTree = iTree.makeTree(text, htmlListElement, enableInfo)
        listTree.walk()
    elif operation[:2] == '-s':
        text = sys.argv[2]
        listTree = iTree.makeTree(text, htmlListElement, enableInfo)
        listTree.walk()
    else:
        print "no such an option"

            
                
            
            
