# aiutocomputerhelp-scan-ssh

This small yet powerful program is designed to scan ports on a specified IP address, checking for the presence of the SSH service. The code relies on two main functionalities: verifying if a port is open and determining whether it responds as an SSH service.

Thanks to Paramiko, a Python package specifically designed for SSH connections, the program accurately checks for the presence of the SSH service and automatically stops the scan if SSH is found on a port. The search loop terminates as soon as the service is detected.

https://www.aiutocomputerhelp.it/nmap-vs-codice-trovare-servizio-ssh-esposto-su-porta-non-standard/
