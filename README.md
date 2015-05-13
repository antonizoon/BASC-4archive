## BASC-4archive

An initiative by the Bibliotheca Anonoma to rescue and rehost the 4archive.

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