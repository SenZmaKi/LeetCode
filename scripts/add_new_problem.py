import subprocess
import sys


def run_cmd(cmd: list[str]) -> str:
    proc = subprocess.run(cmd, capture_output=True, text=True)

    if proc.returncode:
        print(proc.stdout)
        print(proc.stderr, file=sys.stderr)
        proc.check_returncode()
    return proc.stdout


def get_commit_from_new_files() -> str:
    output = run_cmd(["git", "status", "-s"])
    file_names = [f_name.split(" ", 2)[-1] for f_name in output.splitlines()]
    joined_names = " ".join(file_names)
    commit = f"Add {joined_names}"
    return commit


def main() -> None:
    commit = sys.argv[1] if len(sys.argv) > 1 else get_commit_from_new_files()
    run_cmd(["git", "add", "."])
    run_cmd(["git", "commit", "-am", commit])
    run_cmd(["git", "push"])


if __name__ == "__main__":
    main()
