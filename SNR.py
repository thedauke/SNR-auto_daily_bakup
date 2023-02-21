import paramiko
import os.path
import time

# Define a list of dictionaries for the devices
devices = [
    {
        'ip': 'host ip',
        'username': 'username_of_ssh',
        'password': 'password_of_ssh',
        'hostname': 'hostname_of_device',
    },
    {
        'ip': 'host ip of 2d device',
        'username': 'username_of_ssh',
        'password': 'password_of_ssh',
        'hostname': 'hostname_of_device',
    },
]

tryloop=0

# Loop over the devices and retrieve the configurations
for device in devices:
    connected = False
    while not connected:
        try:
            # Connect to the device over SSH
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(device['ip'], username=device['username'], password=device['password'])
            connected = True
        except Exception as e:
            print(f"Failed to connect to {device['ip']}: {e}")
            time.sleep(5)
            tryloop=tryloop+1
            if tryloop==10:
                print("something wrong :( I tried to connect to the device 10 times, no results then ")
                connected = True

    # Connect to the device over SSH
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(device['ip'], username=device['username'], password=device['password'])

    # Execute the "show run" command
    stdin, stdout, stderr = ssh.exec_command("show run")
    sh_run = stdout.read().decode()
     
    hostname = str(device['hostname'])

    # Write the output to a file
    with open(f"/home/user/SNR/{hostname}.txt", "w") as f:
        f.write(sh_run)

    # Close the SSH connection
    ssh.close()
