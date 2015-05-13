#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# BASC 4archive: generate-url-lists.py

# This Python script generates a list of all images used by the 4archive from the SQL dump (converted to SQLite)

import sqlite3
import re

from utils import *

# sql query to obtain all image urls, along with other helpful info
url_query = """SELECT threads.board,
	threads.thread_id,
	posts.chan_id AS post_id,
	posts.image_url,
	posts.chan_image_name AS image_name
FROM posts
INNER JOIN threads ON threads.id = posts.threads_id
WHERE posts.image_url NOT NULL
ORDER BY threads.board,
		threads.thread_id,
		posts.chan_id;"""

def main():
	# define current working directory
	workdir = os.path.join(os.getcwd(), "4archive")
	imgurl_fname = "imageurls.txt"
	db_fname = os.path.join(workdir, "4archive.sqlite")
	
	# connect to the database
	conn = sqlite3.connect(db_fname)
	c = conn.cursor()
	
	# run sql_query and store in variable
	c.execute(url_query)
	rows = c.fetchall()
	
	# iterate through data
	for row in rows:
		# data variables
		board = row[0]
		thread_id = str(row[1])
		post_id = str(row[2])
		image_url = row[3]
		image_name = row[4]
		
		# create folder structure
		thread_path = os.path.join(workdir, board, thread_id)
		mkdirs(thread_path)
		
		# write current image URL to a file in folder structure, append
		with open(os.path.join(workdir, thread_path, imgurl_fname), "a+") as f:
			# ignore 404 urls
			regex404 = re.compile("/images/\w+-404")
			if (regex404.match(image_url)):
				continue
			else:
				f.write(image_url)
				f.write("\n")
		
	# close database when finished
	conn.close()

if __name__ == '__main__':
	main()