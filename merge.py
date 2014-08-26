import os
import time
import sys
import shutil
from subprocess import call
import pdb

dir = sys.argv[1]
under = len(sys.argv) == 3 and sys.argv[2] == "under"
over = len(sys.argv) == 3 and sys.argv[2] == "over"

if under:
	print "merging all tiles UNDER current tileset"
if over:
	print "merging all tiles OVER current tileset"

for x in range(-26, 26):
	print x
	for y in range(-26, 26):
		source = "%s/%d,%d.png" % (dir, x, y);
		dest = "master/%d,%d.png" % (x, y);
		if not os.path.exists(source):
			continue

		if not os.path.exists(dest):
			print source
			shutil.copyfile(source, dest)
			if under:
				os.utime(dest, (0, 0))
			print "new %s" % source
			continue

		desttime = os.path.getmtime(dest)
		if not over and (under or os.path.getmtime(source) < desttime):
			# print "older: %s %d" % (source, os.path.getmtime(dest))
			call("composite -compose Dst_Over %s %s %s" % (source, dest, dest), shell=True)
			# print "under %s" % source
		else:
			call("composite -compose Over %s %s %s" % (source, dest, dest), shell=True)
			print "over %s" % source
			os.utime(dest, (desttime, desttime))

		