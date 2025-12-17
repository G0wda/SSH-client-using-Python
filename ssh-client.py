
import paramiko
import sys
import termios
import tty
import os
import select
import signal
import getpass

hostname = sys.argv[1]
username = sys.argv[2]
port = 22

password = getpass.getpass("Enter password: ")

# Save local terminal state
oldtty = termios.tcgetattr(sys.stdin)

def restore_terminal():
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, oldtty)

def resize_pty(channel):
    rows, cols = os.popen('stty size', 'r').read().split()
    channel.resize_pty(width=int(cols), height=int(rows))

def signal_handler(sig, frame):
    restore_terminal()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(
        hostname=hostname,
        port=port,
        username=username,
        password=password
    )

    channel = ssh.invoke_shell()
    resize_pty(channel)

    # Set terminal to raw mode
    tty.setraw(sys.stdin.fileno())

    print(f"\nConnected to {hostname}. Interactive shell started.\n")

    while True:
        r, w, e = select.select([channel, sys.stdin], [], [])

        if channel in r:
            data = channel.recv(1024)
            if not data:
                break
            sys.stdout.write(data.decode(errors="ignore"))
            sys.stdout.flush()

        if sys.stdin in r:
            x = sys.stdin.read(1)
            if not x:
                break
            channel.send(x)

except Exception as e:
    print("Error:", e)

finally:
    restore_terminal()
    ssh.close()
