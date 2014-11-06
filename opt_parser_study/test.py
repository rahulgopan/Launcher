#!/usr/bin/python

import os
from optparse import OptionParser,OptionGroup
import sys

parser = OptionParser()
'''
parser.add_option("-f", "--file", dest="filename", help="write report to FILE", metavar="FILE")
(options, args) = parser.parse_args()

usage = "usage: %prog [options] arg1 arg2"

if options.filename == None :
	print parser.print_help()

else :
	os.system ('echo "Test" > %s' % options.filename) 
'''

usage = "usage: %prog [options]"
parser.add_option("-t", "--testbed", dest="testbed", help="mention the testbed to be used eg : w1-pamo-nehl")
parser.add_option("-b", "--branch", dest="branch", help="branch eg : vmcore-main,vmkernel-main")
parser.add_option("-c", "--change", dest="change", help="change no eg : 2403389, 2789346")
group = OptionGroup(parser, "Optional options")
group.add_option("-r", "--run", dest="run", help="specify 1 if you want to run the test")
group.add_option("-l", "--runlist",dest="runlist", help="specify the runlist")
parser.add_option_group(group)
(options, args) = parser.parse_args()

if options.testbed == None or options.branch == None or options.change == None :
	print usage
	print parser.print_help()
	sys.exit(2)
else :
	print "TestBed : %s" % options.testbed
	print "Branch : %s" % options.branch
	print "Change : %s" % options.change

os.system('echo %s %s %s > Trigger' % (options.testbed,options.branch,options.change))

if options.run != None :
	if options.runlist == None :
		print "Speicify the runlist to run"
		os.system('echo " " > Trigger')
		sys.exit(2)
	else :	
		os.system('echo %s %s %s %s > Trigger'% (options.testbed,options.branch,options.change,options.runlist))


