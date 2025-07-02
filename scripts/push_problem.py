import sys
from scripts.common import run_cmd, log

log = log.getChild("push_problem")


def get_commit_from_new_files() -> str:
    log.info("Retrieving commit from new files")
    output = run_cmd(["git", "status", "-s"])
    new_files_suffix = "A  "
    file_names = [
        f_name.replace(new_files_suffix, "").replace(
            "leetcode/", ""
        )  # Remove git added tag and leetcode/ dir from file name
        for f_name in output.splitlines()
        if f_name.startswith(new_files_suffix)  # Only include added files
    ]
    if not file_names:
        raise ValueError(
            f"No added file names detected\n git status -s output: {output}"
        )
    log.info(f"New files: {file_names}")
    joined_names = " ".join(file_names)
    commit = f"Add {joined_names}"
    return commit


def main() -> None:
    run_cmd(["git", "add", "."])
    commit = sys.argv[1] if len(sys.argv) > 1 else get_commit_from_new_files()
    run_cmd(["git", "commit", "-am", commit])
    run_cmd(["git", "push"])
    log.info("Successfully pushed problem")


if __name__ == "__main__":
    main()
