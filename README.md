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
* (DONE) /adv/ - Advice (63 Threads, attaliates)
* (UPLOADED) /asp/ - (12 Threads, tabris)
* (DONE) /an/ - Animals (12 Threads, 338MB, tabris)
* (DONE, accidentally uploaded adv?) /biz/ - Business and Finance (26 Threads, tabris)
* (UPLOADED) /c/ - Cute (50 Threads, tabris)
* (UPLOADED) /cgl/ - Cosplay (27 Threads)
* (DONE, maybe uploaded?) /ck/ - Cooking (46 Threads)
* /co/ - Comics and Cartoons (719 Threads, attaliates)
* (DONE) /cm/ - Cute/Male (attaliates)
* (DONE) /diy/ - Do-it-Yourself (39 Threads, 265.9MB, tabris)
* /e/ - Ecchi (169 Threads, tabris)
* /fit/ - Fitness (439 Threads, tabris)
* () /int/ - International (327 Threads, attaliates)
* (UPLOADED) /lit/ - Literature (142 Threads, tabris)
* /m/ Mecha (626 Threads)
* (DONE) /po/ - Papercraft and Origami (5 threads, 29.2MB, tabris)
: /pol/ Politically Incorrect (905 Threads, Chrysoloras)
* (UPLOADING) /s/ - Sexy Beautiful Women (793 Threads, YSVPS)
* (UPLOADED) /sci/ - Science (126 Threads, attaliates)
* (DONE) /sp/ - Sports (158 Threads, 3312MB, attaliates)
* (UPLOADING) /t/ - Torrents (158 Threads, attaliates)
* (DONE) /toy/ - Toys (110 Threads, YSVPS)
* (DONE) /trv/ - Travel (187 Threads, YSVPS)
* /v/ - Video Games (5851 Threads, Chrysoloras)
* (UPLOADING) /vg/ - Video Games Generals (567 Threads, YSVPS)
* (DONE) /vp/ - Pokemon (368 Threads, tabris)
* /vr/ - Retro Games (22 Threads, tabris)
* (DONE) /x/ - Paranormal (448 Threads, attaliates)
* (UPLOADED) /y/ - Yaoi (45 threads, 1.7GB, tabris)