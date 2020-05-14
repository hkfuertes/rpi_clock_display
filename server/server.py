from flask import Flask
import os, signal, subprocess
app = Flask(__name__)

pid_file = os.path.join(os.path.dirname(__file__), '../current.pid')
gui_pid = open(pid_file, 'r').read()

app_py = os.path.join(os.path.dirname(__file__), '../gui/app.py')

@app.route("/kill-gui")
def kill_gui():
    os.kill(int(gui_pid), signal.SIGUSR1)
    return "GUI with PID: {} Killed!".format(gui_pid)

@app.route("/start-gui")
def start_gui():
    if not os.path.isfile(pid_file):
        process = subprocess.Popen(["python3",app_py])
        gui_pid = process.pid
        return "GUI Started with PID: {}!".format(gui_pid)
    else:
        return "Already Started!"

if __name__ == "__main__":
    app.run()