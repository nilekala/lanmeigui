#!/usr/bin/python
#-*- coding:utf-8 -*-
#****************************************************
#         Author: nile cui - nile.cui@gmail.com
#  Last modified: 2014-12-11 10:41
#       Filename: make2html.py
#    Description:
#****************************************************

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import os,time
import subprocess
rlist=[]

def getFetchFile(path,name):
	fname=name
	print path
	dpath=path
	rootFList=os.listdir(dpath);
	dirList=[]
	flist=[]

	print "rootFList-->",rootFList

	for rf in rootFList:
		tpath=''
		#判断是否有readme.md文件
		# print os.path.isfile(rf)
		# if os.path.isfile(rf):
			# 获取所有的文件
			# print rf
			# print fname.lower()
			# print rf.endswith(fname.lower())

			# cs=fname.lower()
			# print "cs-->",cs
		
		if rf.endswith(fname.lower()):
			# print "path[-1:]-->",path[-1:]
			if path[-1:] == '/':
				tpath=path[:-1]
				print "path***********-->",tpath
			else:
				tpath=path
			pwdf=tpath + '/' + rf;
			print "pwdf-->",pwdf
			rlist.append(pwdf.encode('utf-8','ignore'));

		if os.path.isdir(rf):
			#获得所有的目录文件
			pwdr=path+rf
			print "pwdr-->" + repr(pwdr)
			getFetchFile(pwdr,fname)
import copy
if __name__ == '__main__':
	print len(sys.argv)
	if len(sys.argv) is not 2:
		print "Please usage python *.py filename!"
		sys.exit()

	getFetchFile('./',sys.argv[1])
	print "rlist-->",rlist
	for f in rlist:
		# f.encode('utf-8');
		i=len(sys.argv[1])
		print "i=",i
		print -i
		rf=f[:]
		b=f[0:-9].encode('utf-8')
		print b

		# str1="./node_modules/.bin/markdown2bootstrap " +'--outputdir="' + b +'" ' + '"'+rf+'"'
		str1="../node_modules/.bin/markdown2bootstrap " +'--outputdir="./readme" ' + '"'+rf+'"'
		r, w = os.pipe()
		print "str1=",str1
		# p=subprocess.Popen(repr(str1),shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
		p=subprocess.Popen(str1,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
		print p.stdout.readlines();

		time.sleep(0.2);
