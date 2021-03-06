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

* /a/ - Animu and Mango ()
* (UPLOADED) /adv/ - Advice (63 Threads, attaliates)
* (UPLOADED) /asp/ - (12 Threads, tabris)
* (UPLOADED) /an/ - Animals (12 Threads, 338MB, tabris)
* (UPLOADED) /biz/ - Business and Finance (26 Threads, tabris)
* (UPLOADED) /c/ - Cute (50 Threads, tabris)
* (UPLOADED) /cgl/ - Cosplay (27 Threads)
* (UPLOADED) /ck/ - Cooking (46 Threads)
* (DONE) /co/ - Comics and Cartoons (719 Threads, attaliates)
* (UPLOADED) /cm/ - Cute/Male (attaliates)
* (UPLOADED) /diy/ - Do-it-Yourself (39 Threads, 265.9MB, tabris)
* /e/ - Ecchi (169 Threads, tabris)
* (DONE) /fa/ - Fashion (2483 Threads, YSVPS)
* /fit/ - Fitness (439 Threads, tabris)
* (DONE) /g/ - Technology (2188 Threads, jkid)
* (UPLOADED) /h/ - Hentai (264 Threads, YSVPS)
* /hc/ - (195 Threads, tabris)
* (UPLOADED) /i/ - Oekaki (attaliates)
* (UPLOADED) /ic/ - (41 Threads, tabris)
* (UPLOADED) /int/ - International (327 Threads, attaliates)
* (UPLOADED) /jp/ - Otaku Culture (YSVPS)
* (DONE) /k/ - Weapons (422 Threads, annemarie)
* (UPLOADED) /lit/ - Literature (142 Threads, tabris)
* (UPLOADING) /m/ Mecha (626 Threads)
* /mu/ - Music (4455 Threads, annemarie)
* (DONE) /mlp/ - Ponies (jkid)
* (UPLOADED) /po/ - Papercraft and Origami (5 threads, 29.2MB, tabris)
* (DONE) /pol/ Politically Incorrect (905 Threads, Chrysoloras)
* /r/ - Requests (121 Threads, tabris)
* (UPLOADED) /s/ - Sexy Beautiful Women (793 Threads, YSVPS)
* (UPLOADED) /sci/ - Science (126 Threads, attaliates)
* (UPLOADING) /soc/ - Social (attaliates)
* (UPLOADING) /sp/ - Sports (158 Threads, 3312MB, attaliates)
* (UPLOADED) /t/ - Torrents (158 Threads, attaliates)
* (UPLOADED) /tg/ - Traditional Games (222 Threads, YSVPS)
* (DONE) /tv/ - Television and Movies (282 Threads, jkid)
* (UPLOADED) /toy/ - Toys (110 Threads, YSVPS)
* (UPLOADED) /trv/ - Travel (187 Threads, YSVPS)
* /v/ - Video Games (5855 Threads, jkid)
* (UPLOADING) /vg/ - Video Games Generals (567 Threads, YSVPS)
* (UPLOADED) /vp/ - Pokemon (368 Threads, tabris)
* (UPLOADED) /vr/ - Retro Games (22 Threads, tabris)
* (UPLOADED) /w/ - Anime/Wallpapers (164 Threads, YSVPS)
* (UPLOADED) /x/ - Paranormal (448 Threads, attaliates)
* (UPLOADED) /y/ - Yaoi (45 threads, 1.7GB, tabris)
