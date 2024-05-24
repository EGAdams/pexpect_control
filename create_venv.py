import pexpect

# Function to create a virtual environment
def create_virtualenv(env_name):
    child = pexpect.spawn(f'python3 -m venv {env_name}')
    child.expect(pexpect.EOF)
    print(f"Virtual environment '{env_name}' created.")

# Function to source the virtual environment
def source_virtualenv(env_name):
    activate_script = f'./{env_name}/bin/activate'
    child = pexpect.spawn(f'bash -c "source {activate_script} && echo $VIRTUAL_ENV"')
    child.expect(pexpect.EOF)
    if child.before:
        print(f"Virtual environment '{env_name}' sourced.")
    else:
        print(f"Failed to source virtual environment '{env_name}'.")

# Create and source the virtual environment
env_name = 'myenv'
create_virtualenv(env_name)
source_virtualenv(env_name)
