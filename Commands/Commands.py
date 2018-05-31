import subprocess
import time
from multiprocessing import Pool


def execute_commands(command):
    myProcess = subprocess.Popen(command, shell=True)
    start = time.time()
    if myProcess.poll() is None:  # if process not completed
        myProcess.wait()  # wait till successfull execution
    end = time.time()
    print("my process sucessfully terminated")
    return end - start


if __name__ == '__main__':
    commands = [
        'sleep 3',
        'ls -l /',
        'find /',
        'sleep 4',
        'find /usr',
        'date',
        'sleep 5',
        'uptime'
    ]
    pool = Pool()  # Create pool object
    execution_times = list(pool.map(execute_commands, commands))
    # Using pool.map to lauch each command in a Seperate process running simulataneously
    print("Minimum is:", min(execution_times), "Maximum is:", max(execution_times), "Average is:",
          sum(execution_times) / len(execution_times), "Total elapsed time is:", sum(execution_times))
