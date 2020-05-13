from flask import Flask
import os, signal
app = Flask(__name__)

pid_file = os.path.join(os.path.dirname(__file__), '../current.pid')
gui_pid = open(pid_file, 'r').read()

@app.route("/kill-gui")
def hello():
    os.kill(int(gui_pid), signal.SIGUSR1)
    return "GUI with PID: {} Killed!".format(gui_pid)

if __name__ == "__main__":
    app.run()