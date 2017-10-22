an experiment in subtree for back end and front end projects 

➜  ~ cd /home/panda/Documents/testsubtrees/myfrontend/;git add .;git commit -S;git push -u origin --all;ng build --aot true --target production --environment prod;rsync -av dist /home/panda/Documents/testsubtrees;cd /home/panda/Documents/testsubtrees/dist;git add .;git commit -S;git push -u origin --all;
On branch master
Your branch is up-to-date with 'origin/master'.

nothing to commit, working tree clean
Branch master set up to track remote branch master from origin.
Everything up-to-date
Date: 2017-10-22T16:38:08.927Z                                                          
Hash: 4c7a5a50d2ea5e7bb8d6
Time: 9413ms
chunk {0} polyfills.14173651b8ae6311a4b5.bundle.js (polyfills) 61.4 kB {4} [initial] [rendered]
chunk {1} main.eeea714052f89ca56c76.bundle.js (main) 3.19 kB {3} [initial] [rendered]
chunk {2} styles.d41d8cd98f00b204e980.bundle.css (styles) 0 bytes {4} [initial] [rendered]
chunk {3} vendor.3ec61cf6f4565d4400d6.bundle.js (vendor) 215 kB [initial] [rendered]
chunk {4} inline.a22cf2dffd606d1b176c.bundle.js (inline) 1.45 kB [entry] [rendered]
sending incremental file list
dist/
dist/3rdpartylicenses.txt
dist/favicon.ico
dist/index.html
dist/inline.a22cf2dffd606d1b176c.bundle.js
dist/main.eeea714052f89ca56c76.bundle.js
dist/polyfills.14173651b8ae6311a4b5.bundle.js
dist/styles.d41d8cd98f00b204e980.bundle.css
dist/vendor.3ec61cf6f4565d4400d6.bundle.js

sent 291,535 bytes  received 172 bytes  583,414.00 bytes/sec
total size is 290,742  speedup is 1.00
On branch master
Your branch is up-to-date with 'origin/master'.

nothing to commit, working tree clean
Branch master set up to track remote branch master from origin.
Everything up-to-date
➜  dist git:(master) git config --global commit.gpgsign true
➜  dist git:(master) gpg --list-secret-keys
/home/panda/.gnupg/pubring.kbx
------------------------------
sec   rsa4096 2017-10-21 [SC]
      7B7F0ED2B9379E7B52458808780BC5E23A6110A3
uid           [ultimate] Private Hunan Panda <kddc@protonmail.com>
ssb   rsa4096 2017-10-21 [E]

➜  dist git:(master) git config --global user.signingkey 7B7F0ED2B9379E7B52458808780BC5E23A6110A3
➜  dist git:(master) cd /home/panda/Documents/testsubtrees/myfrontend/;git add .;git commit -S;git push -u origin --all;ng build --aot true --target production --environment prod;rsync -av dist /home/panda/Documents/testsubtrees;cd /home/panda/Documents/testsubtrees/dist;git add .;git commit -S;git push -u origin --all;
[master f6a1fba] add a background color
 2 files changed, 18 insertions(+), 13 deletions(-)
 rewrite src/app/app.component.html (91%)
Counting objects: 6, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (6/6), done.
Writing objects: 100% (6/6), 1.21 KiB | 1.21 MiB/s, done.
Total 6 (delta 4), reused 0 (delta 0)
remote: Resolving deltas: 100% (4/4), completed with 4 local objects.
To github.com:privatehunanpanda/01angular.git
   32f3690..f6a1fba  master -> master
Branch master set up to track remote branch master from origin.
Date: 2017-10-22T16:43:16.469Z                                                          
Hash: 8606781cba313aaa9895
Time: 7170ms
chunk {0} polyfills.14173651b8ae6311a4b5.bundle.js (polyfills) 61.4 kB {4} [initial] [rendered]
chunk {1} main.c79178e055d5e66a6026.bundle.js (main) 3.38 kB {3} [initial] [rendered]
chunk {2} styles.d41d8cd98f00b204e980.bundle.css (styles) 0 bytes {4} [initial] [rendered]
chunk {3} vendor.3ec61cf6f4565d4400d6.bundle.js (vendor) 215 kB [initial] [rendered]
chunk {4} inline.6811a8ae54e0c8418390.bundle.js (inline) 1.45 kB [entry] [rendered]
sending incremental file list
dist/
dist/3rdpartylicenses.txt
dist/favicon.ico
dist/index.html
dist/inline.6811a8ae54e0c8418390.bundle.js
dist/main.c79178e055d5e66a6026.bundle.js
dist/polyfills.14173651b8ae6311a4b5.bundle.js
dist/styles.d41d8cd98f00b204e980.bundle.css
dist/vendor.3ec61cf6f4565d4400d6.bundle.js

sent 291,724 bytes  received 172 bytes  583,792.00 bytes/sec
total size is 290,933  speedup is 1.00
[master 6d41c65] add a background color
 3 files changed, 3 insertions(+), 1 deletion(-)
 create mode 100644 inline.6811a8ae54e0c8418390.bundle.js
 create mode 100644 main.c79178e055d5e66a6026.bundle.js
Counting objects: 5, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (5/5), done.
Writing objects: 100% (5/5), 3.36 KiB | 3.36 MiB/s, done.
Total 5 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To github.com:privatehunanpanda/privatehunanpanda.github.io.git
   0b84c5e..6d41c65  master -> master
Branch master set up to track remote branch master from origin.
➜  dist git:(master) cd /home/panda/Documents/testsubtrees/myfrontend/;git add .;git commit -S;git push -u origin --all;ng build --aot true --target production --environment prod;rsync -av dist /home/panda/Documents/testsubtrees;cd /home/panda/Documents/testsubtrees/dist;git add .;git commit -S;git push -u origin --all;
[master 101d4a4] text align center for article
 1 file changed, 3 insertions(+), 2 deletions(-)
Counting objects: 5, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (5/5), done.
Writing objects: 100% (5/5), 1.11 KiB | 1.11 MiB/s, done.
Total 5 (delta 3), reused 0 (delta 0)
remote: Resolving deltas: 100% (3/3), completed with 3 local objects.
To github.com:privatehunanpanda/01angular.git
   f6a1fba..101d4a4  master -> master
Branch master set up to track remote branch master from origin.
Date: 2017-10-22T16:45:23.173Z                                                          
Hash: ac6bddb33bf81b6918cf
Time: 7246ms
chunk {0} polyfills.14173651b8ae6311a4b5.bundle.js (polyfills) 61.4 kB {4} [initial] [rendered]
chunk {1} main.97e4eb7349a1b6728c12.bundle.js (main) 3.4 kB {3} [initial] [rendered]
chunk {2} styles.d41d8cd98f00b204e980.bundle.css (styles) 0 bytes {4} [initial] [rendered]
chunk {3} vendor.3ec61cf6f4565d4400d6.bundle.js (vendor) 215 kB [initial] [rendered]
chunk {4} inline.ff7d5b3975b57f5c972c.bundle.js (inline) 1.45 kB [entry] [rendered]
sending incremental file list
dist/
dist/3rdpartylicenses.txt
dist/favicon.ico
dist/index.html
dist/inline.ff7d5b3975b57f5c972c.bundle.js
dist/main.97e4eb7349a1b6728c12.bundle.js
dist/polyfills.14173651b8ae6311a4b5.bundle.js
dist/styles.d41d8cd98f00b204e980.bundle.css
dist/vendor.3ec61cf6f4565d4400d6.bundle.js

sent 291,735 bytes  received 172 bytes  583,814.00 bytes/sec
total size is 290,951  speedup is 1.00
[master 4460bd8] text align center the article
 3 files changed, 3 insertions(+), 1 deletion(-)
 create mode 100644 inline.ff7d5b3975b57f5c972c.bundle.js
 create mode 100644 main.97e4eb7349a1b6728c12.bundle.js
Counting objects: 5, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (5/5), done.
Writing objects: 100% (5/5), 3.39 KiB | 3.39 MiB/s, done.
Total 5 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To github.com:privatehunanpanda/privatehunanpanda.github.io.git
   6d41c65..4460bd8  master -> master
Branch master set up to track remote branch master from origin.
➜  dist git:(master) cd .. 
➜  testsubtrees cd .. 
➜  Documents cd testsubtrees 
➜  testsubtrees cd myfrontend 
➜  myfrontend git:(master) ls -a
.   .angular-cli.json  e2e            .git        karma.conf.js  package.json        README.md  tsconfig.json  yarn.lock
..  dist               .editorconfig  .gitignore  node_modules   protractor.conf.js  src        tslint.json
➜  myfrontend git:(master) ls -a
.   .angular-cli.json  e2e            .git        karma.conf.js  package.json        README.md  tsconfig.json  yarn.lock
..  dist               .editorconfig  .gitignore  node_modules   protractor.conf.js  src        tslint.json
➜  myfrontend git:(master) cd .. 
➜  testsubtrees mybackend 
➜  mybackend git:(master) code .
➜  mybackend git:(master) source venv/bin/activate
(venv) ➜  mybackend git:(master) ✗ code .                               
(venv) ➜  mybackend git:(master) ✗ hug -f api
Traceback (most recent call last):
  File "/home/panda/Documents/testsubtrees/mybackend/venv/bin/hug", line 11, in <module>
    load_entry_point('hug==2.3.2', 'console_scripts', 'hug')()
  File "/home/panda/Documents/testsubtrees/mybackend/venv/lib/python3.6/site-packages/hug/interface.py", line 485, in __call__
    result = self.interface(**pass_to_function)
  File "/home/panda/Documents/testsubtrees/mybackend/venv/lib/python3.6/site-packages/hug/interface.py", line 99, in __call__
    return __hug_internal_self._function(*args, **kwargs)
  File "/home/panda/Documents/testsubtrees/mybackend/venv/lib/python3.6/site-packages/hug/development_runner.py", line 58, in hug
    api_module = importlib.machinery.SourceFileLoader(file.split(".")[0], file).load_module()
  File "<frozen importlib._bootstrap_external>", line 399, in _check_name_wrapper
  File "<frozen importlib._bootstrap_external>", line 823, in load_module
  File "<frozen importlib._bootstrap_external>", line 682, in load_module
  File "<frozen importlib._bootstrap>", line 265, in _load_module_shim
  File "<frozen importlib._bootstrap>", line 684, in _load
  File "<frozen importlib._bootstrap>", line 665, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 674, in exec_module
  File "<frozen importlib._bootstrap_external>", line 780, in get_code
  File "<frozen importlib._bootstrap_external>", line 832, in get_data
FileNotFoundError: [Errno 2] No such file or directory: 'api'
(venv) ➜  mybackend git:(master) ✗ hug -f api.py 
Traceback (most recent call last):
  File "/home/panda/Documents/testsubtrees/mybackend/venv/bin/hug", line 11, in <module>
    load_entry_point('hug==2.3.2', 'console_scripts', 'hug')()
  File "/home/panda/Documents/testsubtrees/mybackend/venv/lib/python3.6/site-packages/hug/interface.py", line 485, in __call__
    result = self.interface(**pass_to_function)
  File "/home/panda/Documents/testsubtrees/mybackend/venv/lib/python3.6/site-packages/hug/interface.py", line 99, in __call__
    return __hug_internal_self._function(*args, **kwargs)
  File "/home/panda/Documents/testsubtrees/mybackend/venv/lib/python3.6/site-packages/hug/development_runner.py", line 58, in hug
    api_module = importlib.machinery.SourceFileLoader(file.split(".")[0], file).load_module()
  File "<frozen importlib._bootstrap_external>", line 399, in _check_name_wrapper
  File "<frozen importlib._bootstrap_external>", line 823, in load_module
  File "<frozen importlib._bootstrap_external>", line 682, in load_module
  File "<frozen importlib._bootstrap>", line 265, in _load_module_shim
  File "<frozen importlib._bootstrap>", line 684, in _load
  File "<frozen importlib._bootstrap>", line 665, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 674, in exec_module
  File "<frozen importlib._bootstrap_external>", line 781, in get_code
  File "<frozen importlib._bootstrap_external>", line 741, in source_to_code
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "api.py", line 15
    return "Happy birthday, friend")
                                   ^
SyntaxError: invalid syntax
(venv) ➜  mybackend git:(master) ✗ hug -f api.py

/#######################################################################\
          `.----``..-------..``.----.
         :/:::::--:---------:--::::://.
        .+::::----##/-/oo+:-##----:::://
        `//::-------/oosoo-------::://.       ##    ##  ##    ##    #####
          .-:------./++o/o-.------::-`   ```  ##    ##  ##    ##  ##
             `----.-./+o+:..----.     `.:///. ########  ##    ## ##
   ```        `----.-::::::------  `.-:::://. ##    ##  ##    ## ##   ####
  ://::--.``` -:``...-----...` `:--::::::-.`  ##    ##  ##   ##   ##    ##
  :/:::::::::-:-     `````      .:::::-.`     ##    ##    ####     ######
   ``.--:::::::.                .:::.`
         ``..::.                .::         EMBRACE THE APIs OF THE FUTURE
             ::-                .:-
             -::`               ::-                   VERSION 2.3.2
             `::-              -::`
              -::-`           -::-
\########################################################################/

 Copyright (C) 2016 Timothy Edmund Crosley
 Under the MIT License


Serving on port 8000...

> Reloading due to file change: api.py
Serving on port 8000...

> Reloading due to file change: api.py
Serving on port 8000...
127.0.0.1 - - [22/Oct/2017 12:50:00] "GET /happy_birthday?name=kushal&age=23 HTTP/1.1" 200 26
127.0.0.1 - - [22/Oct/2017 12:50:02] "GET /happy_birthday?name=kushal&age=23 HTTP/1.1" 200 26
127.0.0.1 - - [22/Oct/2017 12:50:04] "GET /happy_birthday HTTP/1.1" 200 35
^C%                                                                                                                                                                                      (venv) ➜  mybackend git:(master) ✗ git add api.py;git commit;git push -u origin --all;
[master eae5f79] add a default parameter for name
 1 file changed, 2 insertions(+), 2 deletions(-)
Counting objects: 3, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 961 bytes | 961.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To github.com:privatehunanpanda/02hug.git
   58659c9..eae5f79  master -> master
Branch master set up to track remote branch master from origin.
(venv) ➜  mybackend git:(master) cd ..     
(venv) ➜  testsubtrees cd .. 
(venv) ➜  Documents cd subtrees 
(venv) ➜  subtrees git:(master) git remote add -f 02hug git@github.com:privatehunanpanda/02hug.git 
Updating 02hug
remote: Counting objects: 3, done.
remote: Compressing objects: 100% (1/1), done.
remote: Total 3 (delta 2), reused 3 (delta 2), pack-reused 0
Unpacking objects: 100% (3/3), done.
From github.com:privatehunanpanda/02hug
 * [new branch]      master     -> 02hug/master
(venv) ➜  subtrees git:(master) git subtree pulll --prefix 01angular 01angular master           
Unknown command 'pulll'
(venv) ➜  subtrees git:(master) git subtree pull --prefix 01angular 01angular master 
remote: Counting objects: 11, done.
remote: Compressing objects: 100% (4/4), done.
remote: Total 11 (delta 7), reused 11 (delta 7), pack-reused 0
Unpacking objects: 100% (11/11), done.
From github.com:privatehunanpanda/01angular
 * branch            master     -> FETCH_HEAD
   32f3690..101d4a4  master     -> 01angular/master
Merge made by the 'recursive' strategy.
 01angular/src/app/app.component.css  |  6 +++++-
 01angular/src/app/app.component.html | 24 +++++++++++++-----------
 2 files changed, 18 insertions(+), 12 deletions(-)
(venv) ➜  subtrees git:(master) git subtree pull --prefix 02hug 02hug master        
From github.com:privatehunanpanda/02hug
 * branch            master     -> FETCH_HEAD
Merge made by the 'recursive' strategy.
 02hug/api.py | 4 ++--
 1 file changed, 2 insertions(+), 2 deletions(-)
(venv) ➜  subtrees git:(master) git push -u origin --all
Counting objects: 18, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (18/18), done.
Writing objects: 100% (18/18), 5.51 KiB | 1.83 MiB/s, done.
Total 18 (delta 7), reused 0 (delta 0)
remote: Resolving deltas: 100% (7/7), completed with 5 local objects.
To github.com:privatehunanpanda/meta.git
   9a25128..d5477df  master -> master
Branch master set up to track remote branch master from origin.
(venv) ➜  subtrees git:(master)  