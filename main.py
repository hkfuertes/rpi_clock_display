import os, signal, subprocess

app_py = os.path.join(os.path.dirname(__file__), 'gui/app.py')
server_py = os.path.join(os.path.dirname(__file__), 'server/server.py')
pid_file = os.path.join(os.path.dirname(__file__), 'current.pid')


def receive_signal(signum, frame):
    if signum == signal.SIGTERM:
        # Stop all
        print("[!] Closing the apps!")
        os.kill(app_py_pid, signal.SIGTERM)
        os.kill(server_py_pid, signal.SIGTERM)
        os.remove(pid_file)
        quit()

    elif signum == signal.SIGUSR1:
        # Restart GUI
        print("[!] Restarting GUI!")
        os.kill(app_py_pid, signal.SIGTERM)
        app_py_pid = subprocess.Popen(["python3",app_py]).pid

if __name__ == '__main__':
    # Saving the curren PID
    file = open(pid_file,'w') 
    file.write("{}".format(os.getpid())) 
    file.close()

    # Launching the processes
    print("[+] Starting GUI!")
    app_py_pid = subprocess.Popen(["python3",app_py]).pid
    print("[+] Starting Server!")
    server_py_pid = subprocess.Popen(["python3",server_py]).pid

    # Prepare for good closing
    signal.signal(signal.SIGUSR1, receive_signal)
    signal.signal(signal.SIGTERM, receive_signal)