import subprocess
import sys


def run_cmd(cmd: list[str], shell=False) -> str:
    proc = subprocess.run(cmd, capture_output=True, text=True, shell=shell)

    if proc.returncode:
        print(proc.stdout)
        print(proc.stderr, file=sys.stderr)
        proc.check_returncode()
    return proc.stdout
