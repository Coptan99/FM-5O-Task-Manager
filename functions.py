import os


def add_task():
    cwd = os.getcwd()
    try:
        os.mkdir(cwd + "/tasks")
    except FileExistsError:
        pass

    with open(cwd + "/tasks/tasks.txt", "a") as f:
        f.write("Succeed\n")

    f.close()
