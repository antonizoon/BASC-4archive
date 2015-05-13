#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# BASC 4archive: generate-thread-list.py

# This Python script generates a JSON list of all threads, ordered by board, 4archive from the SQL dump (converted to SQLite)

import json
import sqlite3

from utils import *

json_fname = "thread-list.json"
db_fname = "4archive.sqlite"
# sql query to obtain all thread ids, along with other helpful info
thread_query = """SELECT board, thread_id FROM threads ORDER BY board, thread_id;"""

def main():
	# define current working directory
	workdir = os.path.join(os.getcwd(), "4archive")
	
	# if no ./4archive folder found, ask the user to run generate-url-lists.py
	if not os.path.isdir(workdir):
		print("Could not find the folder ./4archive/. Please run `python3 generate-url-lists.py` first.")
		sys.exit(1)
	
	# connect to the database
	conn = sqlite3.connect(db_fname)
	c = conn.cursor()
	
	# run sql_query and store in variable
	c.execute(thread_query)
	rows = c.fetchall()
	
	# create list of dictionaries to store thread data
	thread_dict = []
	
	# iterate through data
	for row in rows:
		# data variables
		board = row[0]
		thread_id = str(row[1])
#		post_id = str(row[2])
		
		# structure (per dictionary):
		# board: <4chan board>
		# thread: <thread>
		# posts: [<post 1>, <post 2>, ...]
		thread_dict.append({'board' : board, 'thread' : thread_id})
		
	# write JSON dictionary to a file in folder structure, truncate
	with open(os.path.join(workdir, json_fname), "w") as f:
		f.write(json.dumps(thread_dict, sort_keys=True, indent=4, separators=(',', ': ')))
		
	# close database when finished
	conn.close()

if __name__ == '__main__':
	main()