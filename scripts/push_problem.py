import sys
from scripts.common import run_cmd


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
