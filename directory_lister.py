import os
from ftplib import FTP
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env
ftp_password = os.getenv( "AWM_ASSET_FTP_PASSWORD" )
ftp_username = os.getenv( "AWM_ASSET_FTP_USERNAME" )
ftp_hostname = os.getenv( "AWM_ASSET_FTP_HOSTNAME" )

def print_menu():
    print("\t///////////////////////// main ftp menu ////////////////////////////")
    print("\t1. List files on remote server")
    print("\t2. List files on local system")
    print("\t3. Change directory on remote server")
    print("\t4. Change directory on local server")
    print("\t5. Make new directory for report files")
    print("\t6. Put file")

def list_local_directory():
    current_dir = os.getcwd()
    print(f"\n\tLocal Directory: {current_dir}")
    os.system('ls -lart')

def list_remote_directory( ftp ):
    print("\n\tRemote Directory: " + ftp.pwd())
    ftp.retrlines('LIST')

def change_local_directory():
    new_dir = input("\n\tWhat directory do you want to change to? ")
    try:
        os.chdir(new_dir)
        print(f"\tChanged local directory to {os.getcwd()}")
    except FileNotFoundError:
        print(f"\tDirectory {new_dir} not found.")
    except NotADirectoryError:
        print(f"\t{new_dir} is not a directory.")

def change_remote_directory( ftp ):
    new_dir = input("\n\tWhat directory do you want to change to on the remote server? ")
    try:
        ftp.cwd(new_dir)
        print(f"\tChanged remote directory to {ftp.pwd()}")
    except Exception as e:
        print(f"\tError: {e}")

def put_file( ftp ):
    filename = input("\n\tEnter the filename to put on the remote server: ")
    if os.path.isfile(filename):
        with open(filename, 'rb') as file:
            ftp.storbinary(f'STOR {os.path.basename(filename)}', file)
            print(f"\tUploaded {filename} to remote server.")
    else:
        print(f"\tFile {filename} does not exist.")

def make_remote_directory( ftp ):
    new_dir = input("\n\tEnter the name of the new directory to create on the remote server: ")
    try:
        ftp.cwd( "reports/2024/may" )
        ftp.mkd(new_dir)
        print(f"\tCreated new directory: {new_dir}")
    except Exception as e:
        print(f"\tError: {e}")


def main():
    ftp = FTP( ftp_hostname )
    ftp.login( user=ftp_username, passwd=ftp_password )
    ftp.set_pasv(True)
    ftp.cwd('/public_html')

    while True:
        print_menu()
        choice = input("\n\tEnter your choice: ")

        if choice == '1':
            list_remote_directory( ftp )
        elif choice == '2':
            list_local_directory()
        elif choice == '3':
            change_remote_directory( ftp )
        elif choice == '4':
            change_local_directory()
        elif choice == '5':
            make_remote_directory( ftp )
        elif choice == '6':
            put_file( ftp )
        else:
            print("\tInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
