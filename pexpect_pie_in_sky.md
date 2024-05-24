I want to create a system to communicate to a remote server doing FTP operations.

I want the interface to have outputs of a menu, the current directory on the local system, the current directory on the remote server, and an `ls` of each from the current directory.  So a typical output would be:
```bash
    ///////////////////////// main ftp menu ////////////////////////////
    1. List files on remote server
    2. List files on local system
    3. Change directory on remote server    
    4. Change directory on local server
    5. put file

    Local Directory: /home/adamsl/pexpect_controls
    (myenv) adamsl@penguin:~/pexpect_control$ cd myenv/
    (myenv) adamsl@penguin:~/pexpect_control/myenv$ ls -lart
    total 8
    drwxr-xr-x 1 adamsl adamsl   0 May 24 17:51 include
    -rw-r--r-- 1 adamsl adamsl  75 May 24 17:51 pyvenv.cfg
    lrwxrwxrwx 1 adamsl adamsl   3 May 24 17:51 lib64 -> lib
    drwxr-xr-x 1 adamsl adamsl  18 May 24 17:51 lib
    drwxr-xr-x 1 adamsl adamsl  56 May 24 17:51 .
    drwxr-xr-x 1 adamsl adamsl 160 May 24 17:52 bin
    drwxr-xr-x 1 adamsl adamsl 122 May 24 18:11 ..
    (myenv) adamsl@penguin:~/pexpect_control/myenv$ 


    Remote Directory: /public_html/reports/
    ftp> ls
    227 Entering Passive Mode (192,185,149,234,194,232)
    150 Accepted data connection
    drwxr-x---    4 awmasset   99               4096 May 24 00:24 .
    drwx--x--x   21 awmasset   awmasset         4096 May 22 21:17 ..
    -rw-r--r--    1 awmasset   awmasset          289 May 24 00:24 .htaccess
    -rw-r--r--    1 awmasset   awmasset          289 Apr 18 00:27 .htaccess.phpupgrader.96bfac3b
    -rw-r--r--    1 awmasset   awmasset          289 Apr 18 00:27 .htaccess.phpupgrader.initial
    drwxr-xr-x    3 awmasset   awmasset         4096 Oct  9  2023 .well-known
    drwxr-xr-x    3 awmasset   awmasset         4096 May 20 18:53 reports
    226-Options: -a -l 
    226 7 matches total
    ftp>
```
Notice the `tab` in front of everything.  I want this for padding.


If I press 4 ( Change directory on local server ), the Python script that you write should ask me for a directory to change to, change to it, and perform the neccessary `ls` command to show the new menu screen with the new directory contents.

So if I press 4, I get an input prompt:
```bash What directory do you want to change to? ```

Then I enter:
```bash myenv ```

The output with the new directory change should be:
```bash
    ///////////////////////// main ftp menu ////////////////////////////
    1. List files on remote server
    2. List files on local system
    3. Change directory on remote server    
    4. Change directory on local server
    5. put file

    Local Directory: /home/adamsl/
    (myenv) adamsl@penguin:~/pexpect_control$ ls -lart
    total 12
    drwxr-xr-x 1 adamsl adamsl 2006 May 24 17:27 ..
    drwxr-xr-x 1 adamsl adamsl  118 May 24 17:27 .git
    -rw-r--r-- 1 adamsl adamsl 1250 May 24 17:41 pexpect_upload.py
    -rw-r--r-- 1 adamsl adamsl  761 May 24 17:51 create_venv.py
    drwxr-xr-x 1 adamsl adamsl   56 May 24 17:51 myenv
    drwxr-xr-x 1 adamsl adamsl  122 May 24 18:11 .
    -rw-r--r-- 1 adamsl adamsl 2135 May 24 18:22 pexpect_pie_in_sky.md
    (myenv) adamsl@penguin:~/pexpect_control$ 


    Remote Directory: /public_html/reports/
    ftp> ls
    227 Entering Passive Mode (192,185,149,234,194,232)
    150 Accepted data connection
    drwxr-x---    4 awmasset   99               4096 May 24 00:24 .
    drwx--x--x   21 awmasset   awmasset         4096 May 22 21:17 ..
    -rw-r--r--    1 awmasset   awmasset          289 May 24 00:24 .htaccess
    -rw-r--r--    1 awmasset   awmasset          289 Apr 18 00:27 .htaccess.phpupgrader.96bfac3b
    -rw-r--r--    1 awmasset   awmasset          289 Apr 18 00:27 .htaccess.phpupgrader.initial
    drwxr-xr-x    3 awmasset   awmasset         4096 Oct  9  2023 .well-known
    drwxr-xr-x    3 awmasset   awmasset         4096 May 20 18:53 reports
    226-Options: -a -l 
    226 7 matches total
    ftp>
```

When the Python script starts, it should login to the ftp server, setp to passive mode and change to the puplic_html
directory so we can start navigating, putting and pulling files.


use these credentials for the FTP login:
```
name = "ftp_username"
password = "ftp_password"
```
