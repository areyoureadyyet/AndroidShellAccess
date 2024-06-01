import os
from pyfiglet import Figlet
from colorama import Fore, Style
import sys

# Set the font for the Figlet text
font = 'slant'
f = Figlet(font=font)

# Print the banner
print(Fore.RED)
print(f.renderText("ANDROID"))
print(f.renderText("SHELL"))
print(f.renderText("ACCESS"))
print(Style.RESET_ALL)

# Help text for commands
help_text = """
1. **File and Directory Operations:**
   - `ls`: List files and directories.
   - `cd <directory>`: Change directory.
   - `mkdir <directory>`: Create a new directory.
   - `rmdir <directory>`: Remove a directory.
   - `cp <source> <destination>`: Copy files.
   - `mv <source> <destination>`: Move or rename files.
   - `rm <file>`: Delete a file.

2. **File Content Operations:**
   - `cat <file>`: Display file content.
   - `more <file>` / `less <file>`: View file content page by page.

3. **System Information:**
   - `pwd`: Print working directory.
   - `uname -a`: Display system information.
   - `top`: Display running processes.
   - `ps`: List running processes.
   - `df`: Display disk space usage.
   - `free`: Display memory usage.

4. **Network Operations:**
   - `ping <host>`: Check connectivity to a host.
   - `ifconfig` / `ip addr`: Display network interfaces.

5. **Package Management:**
   - `pm list packages`: List installed packages.
   - `pm uninstall <package>`: Uninstall a package.
   - `pm install <path-to-apk>`: Install an APK.

6. **Miscellaneous:**
   - `date`: Display or set the system date and time.
   - `reboot`: Reboot the device (requires appropriate permissions).
   - `chmod <permissions> <file>`: Change file permissions.
7. **Environment Variables:**
   - `env`: Displays all environment variables.
8. **Find Commands**
   - `which <command>`: Shows if the command exists.
9. **System Utilities**
   - `uptime`: Find how long the system has been running.
   - `cat /proc/cpuinfo`: Find CPU information.
   - `cat /proc/meminfo`: Find memory information.
`quit`: Quit the command line.
"""
print(Fore.GREEN)
print(help_text)
print(Fore.WHITE, Style.RESET_ALL)

# Main loop to accept commands
running = True
while running:
    cmd = input("Enter command: ")
    if cmd.strip().lower() == "quit":
        running = False
        print("Exiting...")
    else:
        os.system(cmd)