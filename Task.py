import time
import shlex
import subprocess
import os


class Task:
    def __init__(self, cmd, cwd, log_path):
        self.cmd = cmd
        self.cwd = cwd
        self.log = open(os.path.join(log_path, "log.txt"), "w")
        self.err = open(os.path.join(log_path, "err.txt"), "w")
        self.state = None

    def start(self):
        self.start_time = time.time()
        # cmd_list = shlex.split(self.cmd)
        # self.process = subprocess.Popen(cmd_list, cwd=self.cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        self.process = subprocess.Popen(self.cmd, cwd=self.cwd, shell=True, stdout=self.log, stderr=self.err)

    def check(self):
        rcode = self.process.poll()
        # print(time.asctime(time.localtime(time.time())), " Check rcode = ",rcode)
        if rcode == None:
            return None
        elif rcode == 0:
            self.data = self.process.communicate(b'\n')
            self.state = 0
            self.end_time = time.time()
            self.log.close()
            self.err.close()
            return rcode
        elif rcode != 0:
            self.data = self.process.communicate(b'\n')
            self.state = rcode
            self.end_time = time.time()
            self.log.close()
            self.err.close()
            return rcode

    def terminate(self):
        self.process.terminate()
        self.data = self.process.communicate()
        self.state = -1
        self.end_time = time.time()
        self.log.close()
        self.err.close()
        return self.state

    def get_run_time(self):
        return self.end_time-self.start_time


