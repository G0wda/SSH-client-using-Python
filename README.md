# Interactive SSH Client

This project is a **simple interactive SSH client written in Python** using the **Paramiko** library.

The code opens an SSH connection to a remote host and provides a **fully interactive terminal session**, similar to running `ssh` from the command line.

---

## What This Code Does

* Connects to a remote machine over SSH
* Opens an interactive shell using a PTY
* Forwards local keyboard input to the remote shell
* Displays remote command output in real time
* Restores the local terminal state on exit

This allows you to run normal shell commands exactly as if you logged in using `ssh`.

---

## Requirements

### System

* Linux or macOS
* Python 3

> This script does not work on Windows because it uses `termios` and `tty`.

### Python dependency

```
paramiko
```

Install it with:

```bash
pip install paramiko
```

---

## Usage

Run the script with a hostname and username:

```bash
python3 ssh-client.py <HOSTNAME> <USERNAME>
```

Example:

```bash
python3 ssh-client.py 192.168.16.13 netvoid
```

You will be prompted to enter the SSH password.

---

## How It Works (Brief)

* Uses `paramiko.SSHClient` to establish an SSH connection
* Calls `invoke_shell()` to start an interactive shell
* Sets the local terminal to raw mode
* Uses `select()` to handle input/output without blocking
* Sends keyboard input directly to the SSH channel
* Prints remote output to the local terminal

---

## Files

```
ssh-client.py   # Interactive SSH client
```

---

## Exit

To exit the remote session:

```bash
exit
```

or press `Ctrl+C`.

---

## License

MIT License
