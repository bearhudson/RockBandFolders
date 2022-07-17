# RockBandFolders
For Lucius

```bash
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Try the new cross-platform PowerShell https://aka.ms/pscore6

PS C:\Users\Brian> wsl
rian@DESKTOP-8AV5GSK:~$ cd /mnt/c/Users/Brian/
brian@DESKTOP-8AV5GSK:/mnt/c/Users/Brian$ git clone https://github.com/bearhudson/RockBandFolders.git
Cloning into 'RockBandFolders'...
remote: Enumerating objects: 22, done.
remote: Counting objects: 100% (22/22), done.
remote: Compressing objects: 100% (16/16), done.
remote: Total 22 (delta 6), reused 17 (delta 4), pack-reused 0
Unpacking objects: 100% (22/22), 10.12 KiB | 33.00 KiB/s, done.

brian@DESKTOP-8AV5GSK:/mnt/c/Users/Brian$ cd RockBandFolders/
brian@DESKTOP-8AV5GSK:/mnt/c/Users/Brian/RockBandFolders$ mv ../Downloads/Ro
Rock Band Blitz.AQEZ-CLo.rar.part  Rock Band Blitz.rar
brian@DESKTOP-8AV5GSK:/mnt/c/Users/Brian/RockBandFolders$ mv ../Downloads/Rock\ Band\ Blitz.rar .
brian@DESKTOP-8AV5GSK:/mnt/c/Users/Brian/RockBandFolders$ ll
total 1066752
drwxrwxrwx 1 brian brian       4096 Jul 17 10:39  ./
drwxrwxrwx 1 brian brian       4096 Jul 17 10:39  ../
drwxrwxrwx 1 brian brian       4096 Jul 17 10:39  .git/
-rwxrwxrwx 1 brian brian          8 Jul 17 10:39  .gitignore*
drwxrwxrwx 1 brian brian       4096 Jul 17 10:39  .idea/
-rwxrwxrwx 1 brian brian      11357 Jul 17 10:39  LICENSE*
-rwxrwxrwx 1 brian brian         29 Jul 17 10:39  README.md*
-rwxrwxrwx 1 brian brian 1092334647 Jul 17 10:39 'Rock Band Blitz.rar'*
-rwxrwxrwx 1 brian brian       1285 Jul 17 10:39  main.py*

Brian@DESKTOP-8AV5GSK:/mnt/c/Users/Brian/RockBandFolders$ sudo apt update
Brian@DESKTOP-8AV5GSK:/mnt/c/Users/Brian/RockBandFolders$ sudo apt install unrar
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following NEW packages will be installed:
  unrar
0 upgraded, 1 newly installed, 0 to remove and 275 not upgraded.
Need to get 113 kB of archives.
After this operation, 406 kB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu focal/multiverse amd64 unrar amd64 1:5.6.6-2build1 [113 kB]
Fetched 113 kB in 0s (1486 kB/s)
Selecting previously unselected package unrar.
(Reading database ... 31836 files and directories currently installed.)
Preparing to unpack .../unrar_1%3a5.6.6-2build1_amd64.deb ...
Unpacking unrar (1:5.6.6-2build1) ...
Setting up unrar (1:5.6.6-2build1) ...
update-alternatives: using /usr/bin/unrar-nonfree to provide /usr/bin/unrar (unrar) in auto mode
Processing triggers for man-db (2.9.1-1) ...

brian@DESKTOP-8AV5GSK:/mnt/c/Users/Brian/RockBandFolders$ unrar x Rock\ Band\ Blitz.rar
Extracting  Rock Band Blitz/The All-American Rejects - Kids in the Street/vocals.ogg  OK
All OK

brian@DESKTOP-8AV5GSK:/mnt/c/Users/Brian/RockBandFolders$ ./main.py
0) .git
1) .gitignore
2) .idea
3) LICENSE
4) main.py
5) README.md
6) Rock Band Blitz
7) Rock Band Blitz.rar
Input Folder Number: 6
Copying album.png to new home in Avenged Sevenfold / So Far Away...
Copying drums_1.ogg to new home in Avenged Sevenfold / So Far Away...
Copying drums_2.ogg to new home in Avenged Sevenfold / So Far Away...
Copying guitar.ogg to new home in Avenged Sevenfold / So Far Away...
Copying keys.ogg to new home in Avenged Sevenfold / So Far Away...
Copying vocals.ogg to new home in The All-American Rejects / Kids in the Street...
brian@DESKTOP-8AV5GSK:/mnt/c/Users/Brian/RockBandFolders$ ls
 LICENSE   README.md  'Rock Band Blitz'  'Rock Band Blitz.rar'   main.py

brian@DESKTOP-8AV5GSK:/mnt/c/Users/Brian/RockBandFolders$ cd Rock\ Band\ Blitz/
brian@DESKTOP-8AV5GSK:/mnt/c/Users/Brian/RockBandFolders/Rock Band Blitz$ ls
'Avenged Sevenfold'  'Fall Out Boy'            'Iron Maiden'                      'My Chemical Romance'    'Rick Springfield'
'Barenaked Ladies'   'Foo Fighters'            'Kelly Clarkson'                    Pink                     Shinedown
 Blink-182           'Foster the People'       'Kool & The Gang'                   Queen                    Soundgarden
'Collective Soul'    'Fun. ft. Janelle Monáe'  'Living Colour'                    'Quiet Riot'             'Tears for Fears'
'Elton John'         'Great White'             'Maroon 5 ft. Christina Aguilera'  'Red Hot Chili Peppers'  'The All-American Rejects'
```
