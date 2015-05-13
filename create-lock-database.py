#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# BASC Macrochan Scraper: 0-create-database.py
#
# This script creates a database to hold all the
# image metadata in a queriable location. Macrochan
# is an image database after all, it should be exported
# into one.

import os
import sqlite3

# our own libraries
from utils import *

if __name__ == '__main__':
	# current working directory
	workdir = os.path.join(os.getcwd(), "4archive")
	mkdirs(workdir)				# ensure that the workdir exists
	# filename of database
	db_fname = os.path.join(workdir, 'lock.sqlite')

	# delete database if it already exists
	try:
		os.remove(db_fname)
	except OSError:
		pass

	# create a database to store macrochan data
	conn = sqlite3.connect(db_fname)
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
