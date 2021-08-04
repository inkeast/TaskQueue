import Task
import time

cmd = "python \"C:\\andre.qingyu.wu\\Breath\\train_cov1d.py\""
cwd = "C:\\andre.qingyu.wu\\Breath\\"

def main():
    task = Task.Task(cmd, cwd, "./")
    task.start()
    while task.check() is None:
        time.sleep(1)
    print(task.data)
    print(task.get_run_time())
    print(task.state)


if __name__ == '__main__':
    main()
