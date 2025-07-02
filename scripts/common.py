import logging
import subprocess
import sys

log = logging.getLogger("leetcode")
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("leetcode.log"),
    ],
)
logger_blocklist = [
    "urllib3",
]
for module in logger_blocklist:
    logging.getLogger(module).setLevel(logging.WARNING)

cmd_log = log.getChild("cmd")


def run_cmd(cmd: list[str], **kwargs) -> str:
    cmd_log.info(f"Running command: {cmd}, subprocess kwargs: {kwargs}")
    proc = subprocess.run(cmd, capture_output=True, text=True, **kwargs)

    if proc.returncode:
        print(proc.stdout)
        print(proc.stderr, file=sys.stderr)
        proc.check_returncode()
    return proc.stdout
