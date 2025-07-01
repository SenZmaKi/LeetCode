from pathlib import Path
import sys
from typing import NamedTuple

import requests

from scripts.common import run_cmd

LEET_CODE_API_ENTRY = "https://leetcode-api-pied.vercel.app"
PROBLEMS_FOLDER = Path("./leetcode/")


class ProblemMetadata(NamedTuple):
    id: int
    url: str
    title: str
    diffculty: str


def get_problem_metadata(id: int) -> ProblemMetadata:
    resp = requests.get(f"{LEET_CODE_API_ENTRY}/problem/{id}")
    resp_json = resp.json()

    if resp.status_code == 404:
        raise ValueError(f"Problem with id: {id} not found. Response json: {resp_json}")
    return ProblemMetadata(
        url=resp_json["url"],
        title=resp_json["title"],
        id=id,
        diffculty=resp_json["difficulty"],
    )


def create_problem_file(problem: ProblemMetadata) -> Path:
    filename = problem.title.lower().replace(" ", "_")
    filepath = PROBLEMS_FOLDER / f"{filename}.py"
    with filepath.open("w") as f:
        contents = f"# {problem.id}. {problem.title}\n# {problem.url}\n# {problem.diffculty}\n\n\n"
        f.write(contents)
    return filepath


def main() -> None:
    if len(sys.argv) < 1:
        raise ValueError("No problem id provided")
    id = int(sys.argv[1])
    problem = get_problem_metadata(id)
    filepath = create_problem_file(problem)
    run_cmd(["code", str(filepath)], shell=True)


if __name__ == "__main__":
    main()
