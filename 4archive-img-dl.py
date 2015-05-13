#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# BASC 4archive: 4archive-img-dl.py
# 
# This script downloads all images from the 4archive's third-party image hosting services.

import sys
import time
import sqlite3
from docopt import docopt
from glob import glob
from os.path import basename
from urllib.parse import urlparse

from utils import *

__doc__ = """BASC 4archive: 4archive-img-dl.py.
This script downloads all images from the 4archive's third-party image hosting services. 

By default, it will scrape every board, but you can tell it to just scrape one board at a time.

Usage:
  4archive-img-dl.py
  4archive-img-dl.py <board> [--delay=<pause>]
  4archive-img-dl.py --clean
  4archive-img-dl.py (-h | --help)

Options:
  -h --help        Show this screen.
  --clean       Delete lock.sqlite before starting a second dump.
  --delay=<pause>  Delay between image downloads [default: 2].

"""

# define current working directory
workdir = os.path.join(os.getcwd(), "4archive")
db_fname = os.path.join(workdir, "4archive.sqlite")
lockdb_fname = os.path.join(workdir, "lock.sqlite")
imgurl_fname = "imageurls.txt"

# make a new lockdb
def create_database():
	mkdirs(workdir)				# ensure that the workdir exists

	# delete database if it already exists
	try:
		os.remove(lockdb_fname)
	except OSError:
		pass

	# create a database to store macrochan data
	conn = sqlite3.connect(lockdb_fname)
	c = conn.cursor()

	# create `images` table
	c.execute('''CREATE TABLE savedthreads (
	  board text,
	  thread integer
	)''')

	# Save (commit) the database changes
	conn.commit()

	# close sqlite database
	conn.close()

def main():
	# docopts
	args = docopt(__doc__)
	
	# delay between downloads, command line argument with default
	pause = float(args['--delay'])
	delay404 = 30
	
	# create a new lock.sqlite if clean option is given or it doesn't exist
	if (args['--clean']):
		create_database()
		sys.exit(0)

	if (not os.path.exists(lockdb_fname)):
		create_database()
	
	# if no ./4archive folder found, ask the user to run generate-url-lists.py
	if not os.path.isdir(workdir):
		print("Could not find the folder ./4archive/. Please run `python3 generate-url-lists.py` first.")
		sys.exit(1)

	# connect to the database
	conn = sqlite3.connect(db_fname)
	c = conn.cursor()
	
	# sql query to obtain all thread ids, along with other helpful info
	if (args['<board>'] != ''):		# argument for single board
		c.execute("""SELECT board, thread_id FROM threads WHERE board = (?) ORDER BY board, thread_id;""", [sys.argv[1]])
	else:						# scrape all boards
		c.execute("""SELECT board, thread_id FROM threads ORDER BY board, thread_id;""")
	
	# determine amount of rows in table, and calculate where to stop
	# should be 0 for empty database
	data = c.fetchall()
	row_amt = len(data)
	print("{} threads will be downloaded.".format(row_amt))
	stop = row_amt

	# create a lock database to keep track of progress
	lock_conn = sqlite3.connect(lockdb_fname)
	lock_c = lock_conn.cursor()
	
	# determine amount of rows in table with imageext, and calculate where to start
	# should be 0 at beginning
	lock_c.execute('SELECT COUNT(*) FROM savedthreads')
	count = lock_c.fetchall()
	row_amt = count[0][0]
	print("Starting at {} on table 'threads'.".format(row_amt + 1))
	start = int(row_amt)
	
	# iterate download through rows, board and thread_id as columns
	for index in range(start, stop - 1):
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
				time.sleep(pause)
				
		# save progress
		lock_c.execute('INSERT OR IGNORE INTO savedthreads (board, thread) VALUES (?, ?)', [board, thread])
		lock_conn.commit()
		
	# close connections when finished
	conn.close()
	lock_conn.close()
	
	# completion message
	print("Done! If you've been scraping every board, you can now upload the image backup to the Internet Archive.")
	print("If you've only been scraping one board, run \n4archive-img-dl.py --clean \nand start scraping another one.")


if __name__ == '__main__':
	main()