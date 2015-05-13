#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# BASC 4archive: 4archive-img-dl.sh
# 
# This script downloads all images from the 4archive's third-party image hosting services.

import sys
import time
import sqlite3
from glob import glob
from os.path import basename
from urllib.parse import urlparse

from utils import *

def main():
	# delay between downloads
	delay = 2
	delay404 = 30
	
	# define current working directory
	workdir = os.path.join(os.getcwd(), "4archive")
	db_fname = os.path.join(workdir, "4archive.sqlite")
	lockdb_fname = os.path.join(workdir, "lock.sqlite")
	imgurl_fname = "imageurls.txt"
	
	# sql query to obtain all thread ids, along with other helpful info
#	thread_query = """SELECT board, thread_id FROM threads ORDER BY board, thread_id;"""
	thread_query = """SELECT board, thread_id FROM threads WHERE board = "y" ORDER BY board, thread_id;"""
	
	# if no ./4archive folder found, ask the user to run generate-url-lists.py
	if not os.path.isdir(workdir):
		print("Could not find the folder ./4archive/. Please run `python3 generate-url-lists.py` first.")
		sys.exit(1)

	# connect to the database
	conn = sqlite3.connect(db_fname)
	c = conn.cursor()
	
	# run sql_query and store in variable
	c.execute(thread_query)
	data = c.fetchall()
	
	# determine amount of rows in table, and calculate where to stop
	# should be 0 for empty database
	c.execute('SELECT COUNT(*) FROM threads')
	count = c.fetchall()
	row_amt = count[0][0]
	print("Table 'threads' has {} rows.".format(row_amt))
	stop = row_amt

	# create a lock database to keep track of progress
	lock_conn = sqlite3.connect(lockdb_fname)
	lock_c = lock_conn.cursor()
	
	# determine amount of rows in table with imageext, and calculate where to start
	# should be 0 at beginning
	lock_c.execute('SELECT COUNT(*) FROM savedthreads')
	count = lock_c.fetchall()
	row_amt = count[0][0]
	print("Starting at {} on table 'threads'.".format(0))
	start = row_amt
	
	# iterate download through rows, board and thread_id as columns
	for index in range(start, stop):
		# grab data
		board = data[index][0]
		thread = data[index][1]
		
		# set path as board/thread as specified by chan.zip
		path = os.path.join(workdir, str(board), str(thread))
		print(":: Thread /{}/{}".format(board, thread))
		
		# open each imageurls.txt and download all images from them
		with open(os.path.join(path, imgurl_fname), "r") as f:
			for url in f:
				
				# obtain filename from URL
				filename = basename(urlparse(url).path).strip()
				
				# download file, board/thread/files
				if not download_file(os.path.join(path, "files", filename), url, clobber=True):
					print("   Could not download {}, retrying in {}".format(filename, delay404))
					
					# retry 5 times after 30 sec. delay if 404
					for x in range(0, 5):
						time.sleep(delay404)
						if download_file(os.path.join(path, "files", filename), url, clobber=True):
							break
				else:
					print("   Downloaded", filename)
				
				# take a short break
				time.sleep(delay)
				
		# save progress
		lock_c.execute('INSERT OR IGNORE INTO savedthreads (board, thread) VALUES (?, ?)', [board, thread])
		lock_conn.commit()
		
	# close connections when finished
	conn.close()
	lock_conn.close()


if __name__ == '__main__':
	# retry loop: in case of failure or timeout, wait 60 sec. and try again
	# by default, try 5 times
	for i in range(1, 5):
		print("Attempt {}:".format(i))
		main()
		print("Restarting script in {} seconds...".format())
		time.delay(60)