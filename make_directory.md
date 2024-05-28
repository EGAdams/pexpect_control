Here are some ftp commands that I have already written:
```python
def list_remote_directory(ftp):
    print("\n\tRemote Directory: " + ftp.pwd())
    ftp.retrlines('LIST')

def change_remote_directory(ftp):
    new_dir = input("\n\tWhat directory do you want to change to on the remote server? ")
    try:
        ftp.cwd(new_dir)
        print(f"\tChanged remote directory to {ftp.pwd()}")
    except Exception as e:
        print(f"\tError: {e}")
```

Please create the make_remote_directory() method.