import pexpect
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env
ftp_password = os.getenv( "AWM_ASSET_FTP_PASSWORD" )
ftp_username = os.getenv( "AWM_ASSET_FTP_USERNAME" )
ftp_hostname = os.getenv( "AWM_ASSET_FTP_HOSTNAME" )

def ftp_upload():
    # FTP server details
    ftp_server  = ftp_hostname
    username    = ftp_username 
    password    = ftp_password
    directory_to_create = "wednesday_may"
    file_to_upload = "pexpect_script.py"
    
    # Start the FTP session
    child = pexpect.spawn(f'ftp {ftp_server}')
    
    # Wait for the login prompt and send the username
    child.expect('Name .*: ')
    child.sendline(username)
    
    # Wait for the password prompt and send the password
    child.expect('Password:')
    child.sendline(password)
    
    # Wait for the FTP prompt
    child.expect('ftp> ')

    child.sendline( "passive" )
    child.expect('ftp> ')
    
    # Create a new directory
    child.sendline(f'mkdir {directory_to_create}')
    
    # Wait for the FTP prompt
    child.expect('ftp> ')
    
    # Change to the new directory
    child.sendline(f'cd {directory_to_create}')
    
    # Wait for the FTP prompt
    child.expect('ftp> ')
    
    # Upload the file
    child.sendline(f'put {file_to_upload}')
    
    # Wait for the FTP prompt
    child.expect('ftp> ')
    
    # Exit the FTP session
    child.sendline('bye')
    
    # Close the child process
    child.close()

if __name__ == "__main__":
    ftp_upload()
