add projects here

➜  ~ ls -a
.                  .bashrc  Desktop     .gnome         .multirust       .npm               .profile                   Templates  .zcompdump                   .zsh-update
..                 bin      Documents   .gnupg         Music            .oh-my-zsh         Public                     Videos     .zcompdump-ubuntugnome4-5.2
.angular-cli.json  .cache   Downloads   .ICEauthority  .nano            package-lock.json  .rustup                    .viminfo   .zprofile
.bash_history      .cargo   .gconf      .local         nightly.desktop  Pictures           .ssh                       .vscode    .zsh_history
.bash_logout       .config  .gitconfig  .mozilla       node_modules     .pki               .sudo_as_admin_successful  .yarn      .zshrc
➜  ~ python3 --version
Python 3.6.3
➜  ~ cd Documents/testsubtree       
cd: no such file or directory: Documents/testsubtree
➜  ~ cd Documents/testsubtrees
➜  testsubtrees ls -a
.  ..  dist  myfrontend
➜  testsubtrees mkdir mybackend
➜  testsubtrees cd mybackend 
➜  mybackend ls -a
.  ..
➜  mybackend code .
➜  mybackend git add .;git commit -S;git push -u origin --all;
fatal: Not a git repository (or any of the parent directories): .git
fatal: Not a git repository (or any of the parent directories): .git
fatal: Not a git repository (or any of the parent directories): .git
➜  mybackend git init
Initialized empty Git repository in /home/panda/Documents/testsubtrees/mybackend/.git/
➜  mybackend git:(master) ✗ git add .;git commit -S;git push -u origin --all;
[master (root-commit) 584c688] add gitignore
 1 file changed, 2 insertions(+)
 create mode 100644 .gitignore
fatal: 'origin' does not appear to be a git repository
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
➜  mybackend git:(master) git add .;git commit -S;                         
On branch master
nothing to commit, working tree clean
➜  mybackend git:(master) pip --version
zsh: command not found: pip
➜  mybackend git:(master) python3 -m venv venv
➜  mybackend git:(master) source venv/bin/activate
(venv) ➜  mybackend git:(master) ls -a
.  ..  .git  .gitignore  venv
(venv) ➜  mybackend git:(master) ls -a
.  ..  .git  .gitignore  venv
(venv) ➜  mybackend git:(master) pip --version
pip 9.0.1 from /home/panda/Documents/testsubtrees/mybackend/venv/lib/python3.6/site-packages (python 3.6)
(venv) ➜  mybackend git:(master) pip install --upgrade * 
Collecting venv
  Could not find a version that satisfies the requirement venv (from versions: )
No matching distribution found for venv
(venv) ➜  mybackend git:(master) pip install --upgrade pip pip3 setuptools
Requirement already up-to-date: pip in ./venv/lib/python3.6/site-packages
Collecting pip3
  Could not find a version that satisfies the requirement pip3 (from versions: )
No matching distribution found for pip3
(venv) ➜  mybackend git:(master) pip install --upgrade pip setuptools 
Requirement already up-to-date: pip in ./venv/lib/python3.6/site-packages
Collecting setuptools
  Using cached setuptools-36.6.0-py2.py3-none-any.whl
Installing collected packages: setuptools
  Found existing installation: setuptools 32.3.1
    Uninstalling setuptools-32.3.1:
      Successfully uninstalled setuptools-32.3.1
Successfully installed setuptools-36.6.0
(venv) ➜  mybackend git:(master) pip install hug --upgrade
Collecting hug
  Downloading hug-2.3.2.tar.gz (65kB)
    100% |████████████████████████████████| 71kB 1.9MB/s 
Collecting falcon==1.3.0 (from hug)
  Downloading falcon-1.3.0-py2.py3-none-any.whl (150kB)
    100% |████████████████████████████████| 153kB 3.9MB/s 
Collecting requests (from hug)
  Downloading requests-2.18.4-py2.py3-none-any.whl (88kB)
    100% |████████████████████████████████| 92kB 4.0MB/s 
Collecting python-mimeparse>=1.5.2 (from falcon==1.3.0->hug)
  Downloading python_mimeparse-1.6.0-py2.py3-none-any.whl
Collecting six>=1.4.0 (from falcon==1.3.0->hug)
  Using cached six-1.11.0-py2.py3-none-any.whl
Collecting idna<2.7,>=2.5 (from requests->hug)
  Downloading idna-2.6-py2.py3-none-any.whl (56kB)
    100% |████████████████████████████████| 61kB 5.1MB/s 
Collecting urllib3<1.23,>=1.21.1 (from requests->hug)
  Downloading urllib3-1.22-py2.py3-none-any.whl (132kB)
    100% |████████████████████████████████| 133kB 2.7MB/s 
Collecting certifi>=2017.4.17 (from requests->hug)
  Downloading certifi-2017.7.27.1-py2.py3-none-any.whl (349kB)
    100% |████████████████████████████████| 358kB 2.3MB/s 
Collecting chardet<3.1.0,>=3.0.2 (from requests->hug)
  Downloading chardet-3.0.4-py2.py3-none-any.whl (133kB)
    100% |████████████████████████████████| 143kB 3.2MB/s 
Building wheels for collected packages: hug
  Running setup.py bdist_wheel for hug ... error
  Complete output from command /home/panda/Documents/testsubtrees/mybackend/venv/bin/python3 -u -c "import setuptools, tokenize;__file__='/tmp/pip-build-mzi3yytx/hug/setup.py';f=getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec'))" bdist_wheel -d /tmp/tmpfnokhdb4pip-wheel- --python-tag cp36:
  usage: -c [global_opts] cmd1 [cmd1_opts] [cmd2 [cmd2_opts] ...]
     or: -c --help [cmd1 cmd2 ...]
     or: -c --help-commands
     or: -c cmd --help
  
  error: invalid command 'bdist_wheel'
  
  ----------------------------------------
  Failed building wheel for hug
  Running setup.py clean for hug
Failed to build hug
Installing collected packages: python-mimeparse, six, falcon, idna, urllib3, certifi, chardet, requests, hug
  Running setup.py install for hug ... done
Successfully installed certifi-2017.7.27.1 chardet-3.0.4 falcon-1.3.0 hug-2.3.2 idna-2.6 python-mimeparse-1.6.0 requests-2.18.4 six-1.11.0 urllib3-1.22
(venv) ➜  mybackend git:(master) pip install hug --upgrade
Requirement already up-to-date: hug in ./venv/lib/python3.6/site-packages
Requirement already up-to-date: falcon==1.3.0 in ./venv/lib/python3.6/site-packages (from hug)
Requirement already up-to-date: requests in ./venv/lib/python3.6/site-packages (from hug)
Requirement already up-to-date: six>=1.4.0 in ./venv/lib/python3.6/site-packages (from falcon==1.3.0->hug)
Requirement already up-to-date: python-mimeparse>=1.5.2 in ./venv/lib/python3.6/site-packages (from falcon==1.3.0->hug)
Requirement already up-to-date: certifi>=2017.4.17 in ./venv/lib/python3.6/site-packages (from requests->hug)
Requirement already up-to-date: idna<2.7,>=2.5 in ./venv/lib/python3.6/site-packages (from requests->hug)
Requirement already up-to-date: urllib3<1.23,>=1.21.1 in ./venv/lib/python3.6/site-packages (from requests->hug)
Requirement already up-to-date: chardet<3.1.0,>=3.0.2 in ./venv/lib/python3.6/site-packages (from requests->hug)
(venv) ➜  mybackend git:(master) code .
(venv) ➜  mybackend git:(master) pip install --upgrade autopep8
Collecting autopep8
  Downloading autopep8-1.3.3.tar.gz (108kB)
    100% |████████████████████████████████| 112kB 2.7MB/s 
Collecting pycodestyle>=2.3 (from autopep8)
  Downloading pycodestyle-2.3.1-py2.py3-none-any.whl (45kB)
    100% |████████████████████████████████| 51kB 4.7MB/s 
Building wheels for collected packages: autopep8
  Running setup.py bdist_wheel for autopep8 ... error
  Complete output from command /home/panda/Documents/testsubtrees/mybackend/venv/bin/python3 -u -c "import setuptools, tokenize;__file__='/tmp/pip-build-yltzr4ho/autopep8/setup.py';f=getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec'))" bdist_wheel -d /tmp/tmpdfpurrdhpip-wheel- --python-tag cp36:
  usage: -c [global_opts] cmd1 [cmd1_opts] [cmd2 [cmd2_opts] ...]
     or: -c --help [cmd1 cmd2 ...]
     or: -c --help-commands
     or: -c cmd --help
  
  error: invalid command 'bdist_wheel'
  
  ----------------------------------------
  Failed building wheel for autopep8
  Running setup.py clean for autopep8
Failed to build autopep8
Installing collected packages: pycodestyle, autopep8
  Running setup.py install for autopep8 ... done
Successfully installed autopep8-1.3.3 pycodestyle-2.3.1
(venv) ➜  mybackend git:(master) ✗ autopep8 --in-place api.py 
(venv) ➜  mybackend git:(master) ✗ pip freeze >> requirements.txt                                                    
(venv) ➜  mybackend git:(master) ✗ python api.py 
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
127.0.0.1 - - [22/Oct/2017 11:56:26] "GET / HTTP/1.1" 404 935
127.0.0.1 - - [22/Oct/2017 11:56:26] "GET /favicon.ico HTTP/1.1" 404 935
127.0.0.1 - - [22/Oct/2017 11:56:41] "GET /happy_birthday HTTP/1.1" 400 62
127.0.0.1 - - [22/Oct/2017 11:56:55] "GET /happy_birthday?name=kushal&age=23 HTTP/1.1" 200 26
^C%                                                                                                                                                                                      (venv) ➜  mybackend git:(master) ✗ python api_test.py
(venv) ➜  mybackend git:(master) ✗ git remote add origin git@github.com:privatehunanpanda/02hug.git
(venv) ➜  mybackend git:(master) ✗ git add .;git commit -S;git push -u origin --all;                    
Aborting commit due to empty commit message.
oCounting objects: 3, done.
Writing objects: 100% (3/3), 880 bytes | 880.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To github.com:privatehunanpanda/02hug.git
 * [new branch]      master -> master
Branch master set up to track remote branch master from origin.
(venv) ➜  mybackend git:(master) ✗ code .
(venv) ➜  mybackend git:(master) ✗ git add .;git commit -S;git push -u origin --all;
[master 58659c9] add code so I can ask questions
 4 files changed, 39 insertions(+)
 create mode 100644 api.py
 create mode 100644 api_test.py
 create mode 100644 requirements.txt
Counting objects: 6, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (5/5), done.
Writing objects: 100% (6/6), 1.60 KiB | 1.60 MiB/s, done.
Total 6 (delta 0), reused 0 (delta 0)
To github.com:privatehunanpanda/02hug.git
   584c688..58659c9  master -> master
Branch master set up to track remote branch master from origin.
(venv) ➜  mybackend git:(master) code .
(venv) ➜  mybackend git:(master) python api_test.py                                              
Traceback (most recent call last):
  File "api_test.py", line 14, in <module>
    tests_happy_birthday()
  File "api_test.py", line 10, in tests_happy_birthday
    assert response.status == HTTP_200
NameError: name 'HTTP_200' is not defined
(venv) ➜  mybackend git:(master) ✗ git reset --hard 
HEAD is now at 58659c9 add code so I can ask questions
(venv) ➜  mybackend git:(master) code .      
(venv) ➜  mybackend git:(master) cd ..                    
(venv) ➜  testsubtrees cd .. 
(venv) ➜  Documents cd subtrees 
(venv) ➜  subtrees git init
Initialized empty Git repository in /home/panda/Documents/subtrees/.git/
(venv) ➜  subtrees git:(master) git subtree add --prefix 01angular git@github.com:privatehunanpanda/01angular.git master
fatal: ambiguous argument 'HEAD': unknown revision or path not in the working tree.
Use '--' to separate paths from revisions, like this:
'git <command> [<revision>...] -- [<file>...]'
Working tree has modifications.  Cannot add.
(venv) ➜  subtrees git:(master) git status
On branch master

No commits yet

nothing to commit (create/copy files and use "git add" to track)
(venv) ➜  subtrees git:(master) vim README.md
(venv) ➜  subtrees git:(master) ✗ git add README.md; git commit -S;
[master (root-commit) a690cf9] add readme file
 1 file changed, 1 insertion(+)
 create mode 100644 README.md
(venv) ➜  subtrees git:(master) git subtree add --prefix 01angular git@github.com:privatehunanpanda/01angular.git master
git fetch git@github.com:privatehunanpanda/01angular.git master
warning: no common commits
remote: Counting objects: 65, done.
remote: Compressing objects: 100% (49/49), done.
remote: Total 65 (delta 24), reused 55 (delta 14), pack-reused 0
Unpacking objects: 100% (65/65), done.
From github.com:privatehunanpanda/01angular
 * branch            master     -> FETCH_HEAD
Added dir '01angular'
(venv) ➜  subtrees git:(master) git subtree add --prefix 02 hug git@github.com:privatehunanpanda/02hug.git master       
error: parameters were 'hug git@github.com:privatehunanpanda/02hug.git master'
Provide either a commit or a repository and commit.
(venv) ➜  subtrees git:(master) git subtree add --prefix 02hug git@github.com:privatehunanpanda/02hug.git master 
git fetch git@github.com:privatehunanpanda/02hug.git master
warning: no common commits
remote: Counting objects: 9, done.
remote: Compressing objects: 100% (6/6), done.
remote: Total 9 (delta 0), reused 9 (delta 0), pack-reused 0
Unpacking objects: 100% (9/9), done.
From github.com:privatehunanpanda/02hug
 * branch            master     -> FETCH_HEAD
Added dir '02hug'
(venv) ➜  subtrees git:(master) git status
On branch master
nothing to commit, working tree clean
(venv) ➜  subtrees git:(master) git remote add origin git@github.com:privatehunanpanda/meta.git
(venv) ➜  subtrees git:(master) git push -u origin --all
Counting objects: 81, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (74/74), done.
Writing objects: 100% (81/81), 75.24 KiB | 2.69 MiB/s, done.
Total 81 (delta 23), reused 0 (delta 0)
remote: Resolving deltas: 100% (23/23), done.
To github.com:privatehunanpanda/meta.git
 * [new branch]      master -> master
Branch master set up to track remote branch master from origin.
(venv) ➜  subtrees git:(master) git remote add -f 01angular git@github.com:privatehunanpanda/01angular.git       
Updating 01angular
remote: Counting objects: 5, done.
remote: Compressing objects: 100% (1/1), done.
remote: Total 5 (delta 3), reused 5 (delta 3), pack-reused 0
Unpacking objects: 100% (5/5), done.
From github.com:privatehunanpanda/01angular
 * [new branch]      master     -> 01angular/master
(venv) ➜  subtrees git:(master) git fetch 01angular master
From github.com:privatehunanpanda/01angular
 * branch            master     -> FETCH_HEAD
(venv) ➜  subtrees git:(master) git subtree pulll --prefix 01angular 01angular master
Unknown command 'pulll'
(venv) ➜  subtrees git:(master) git subtree pull --prefix 01angular 01angular master 
From github.com:privatehunanpanda/01angular
 * branch            master     -> FETCH_HEAD
Merge made by the 'recursive' strategy.
 01angular/src/app/app.component.css | 3 +++
 1 file changed, 3 insertions(+)
(venv) ➜  subtrees git:(master) git push -u origin --all
Counting objects: 7, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (6/6), done.
Writing objects: 100% (7/7), 1.72 KiB | 1.72 MiB/s, done.
Total 7 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To github.com:privatehunanpanda/meta.git
   b891ff9..8e3491d  master -> master
Branch master set up to track remote branch master from origin.
(venv) ➜  subtrees git:(master) 


