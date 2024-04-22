# SSH Login Brute Force

This script is a basic example of a brute-force password attack against an SSH server running on localhost. It tries to log in using a list of common passwords and stops when it finds a valid one.

## Disclaimer

The tools and scripts provided in this repository are made available for educational purposes only and are intended to be used for testing and protecting systems with the consent of the owners. The author does not take any responsibility for the misuse of these tools. It is the end user's responsibility to obey all applicable local, state, national, and international laws. The developers assume no liability and are not responsible for any misuse or damage caused by this program. Under no circumstances should this tool be used for malicious purposes. The author of this tool advocates for the responsible and ethical use of security tools. Please use this tool responsibly and ethically, ensuring that you have proper authorization before engaging any system with the techniques demonstrated by this project.

## Features

- **Automated SSH Password Testing**: Automatically attempts to log into an SSH server using a list of common passwords.
- **Connection Handling**: Utilizes the Paramiko library to manage SSH connections efficiently.
- **Real-Time Feedback**: Provides feedback on each password attempt, indicating success or failure in real-time.
- **Effective Stop**: Ceases execution upon discovering a valid password, optimizing time and resources.

## Prerequisites

- **Operating System**: This script was tested on Kali Linux 2023.4. It should work on other Unix-like systems with appropriate modifications.
- **Python Libraries**:
    - `pwn`: For hacking-related utilities.
    - `paramiko`: For handling SSH connections.
    - Ensure Python is installed along with these libraries.
- **Password List**: The script uses "10-million-password-list-top-100.txt" from the SecLists collection by default. You can download word lists from [SecLists](https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials).
    
    <aside>
    ⚠️ The default Kali SSH configuration will block authentication attempts after 10 attempts (*MaxStartups 10:30:10*). If you want to test 100 connections + the valid password using the above wordlist, you will need to edit your *sshd_config* (for example, by setting *MaxStartups 101*) and restarting the service. Alternatively to test, use a wordlist with less than 10 invalid passwords.
    </aside>
    
    ```bash
    sudo nano /etc/ssh/sshd_config
    MaxStartups 105
    sudo service ssh restart
    sudo service ssh status
    ```
## Installation

1. **Clone the Repository**:
    
    ```bash
    git clone https://github.com/CyberWolfByte/ssh-brute-force.git
    cd ssh-brute-force
    ```
    
2. **Install Python**: Make sure Python is installed on your system. If not, you can install it using your distribution's package manager. For Kali Linux:
    
    ```bash
    sudo apt-get update
    sudo apt-get install python3
    ```
    
3. **Install Required Python Libraries**: Install the `pwn` and `paramiko` libraries using pip:
    
    ```bash
    pip install pwntools paramiko
    ```
    
4. **Download Password List**: Download the "10-million-password-list-top-100.txt" file or other word list of your choice from the SecLists repository. Update the script accordingly to reflect your target word list:
    https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials

5. **Script Modifications**: Update the script accordingly to reflect your target word list if not using the default. Also update the `host` and `username` connection parameters.

## Usage

```bash
python3 ssh_brute_force.py
```

## How It Works

The script operates by iterating through a list of common passwords, attempting to establish an SSH connection for each:

- **Load Password List**: Reads passwords from a file line by line.
- **Attempt Connection**: Uses each password to try and connect to the SSH server using the Paramiko library.
- **Check Connection**: If a connection is successful, it logs the successful password and exits. If unsuccessful, it tries the next password.
- **Error Handling**: Handles exceptions, specifically looking for authentication failures to continue with the next password without crashing.

## Output Example

```bash
[0] Attempting password: '123456'!
[-] Connecting to 127.0.0.1 on port 22: Failed
[X] Invalid password!
[1] Attempting password: 'password'!
[-] Connecting to 127.0.0.1 on port 22: Failed
[X] Invalid password!
[2] Attempting password: '12345678'!
[-] Connecting to 127.0.0.1 on port 22: Failed
[X] Invalid password!
[3] Attempting password: 'qwerty'!
[-] Connecting to 127.0.0.1 on port 22: Failed
[X] Invalid password!
[4] Attempting password: '123456789'!
[-] Connecting to 127.0.0.1 on port 22: Failed
[X] Invalid password!
[5] Attempting password: '12345'!
[-] Connecting to 127.0.0.1 on port 22: Failed
[X] Invalid password!
[6] Attempting password: '1234'!
[-] Connecting to 127.0.0.1 on port 22: Failed
[X] Invalid password!
[7] Attempting password: '111111'!
[-] Connecting to 127.0.0.1 on port 22: Failed
[X] Invalid password!
[8] Attempting password: '1234567'!
[-] Connecting to 127.0.0.1 on port 22: Failed
[X] Invalid password!
[9] Attempting password: 'kali'!
[+] Connecting to 127.0.0.1 on port 22: Done
[*] kali@127.0.0.1:
    Distro    Unknown 
    OS:       linux
    Arch:     amd64
    Version:  6.5.0
    ASLR:     Enabled
[>] Valid password found: 'kali'!
[*] Closed connection to '127.0.0.1'
```

## Contributing

If you have an idea for an improvement or if you're interested in collaborating, you are welcome to contribute. Please feel free to open an issue or submit a pull request.

## License

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see https://www.gnu.org/licenses/.
