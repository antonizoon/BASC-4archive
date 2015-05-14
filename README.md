## BASC-4archive

An initiative by the Bibliotheca Anonoma to rescue and rehost the 4archive.

### Dependencies

* python3-requests
* python3-docopts
* python3-sqlite3

### Usage

```bash
# create a project folder
mkdir 4archive/
# download 4archive SQLite dump from the Internet Archive
wget # coming soon
# unzip SQLite dump into project folder
7z x 4archive_dump-sqlite.7z 4archive/
# create <board>/<thread> folders
python3 generate-url-lists.py
python3 generate-thread-list.py
python3 create-lock-database.py

# begin downloading all images (can take a while, and needs lots of space)
python3 4archive-img-dl.py
```

### Progress

~250 per folder for NSFW imageboards

* /a/ - Animu and Mango (in progress, chrysoloras)
* /an/ - Animals (12 Threads, 317MB)
* /diy/ - Do-it-Yourself (39 Threads, 265.9MB)
* /lit/ - Literature (142 Threads)
* /po/ - Papercraft and Origami (5 threads, 21.6MB)
* /sp/ - Sports (158 Threads, 3312MB)
* /vp/ - Pokemon (368 Threads, tabris)
* /x/ - Paranormal (448 Threads)
* /y/ - Yaoi (45 threads, 1.7GB)