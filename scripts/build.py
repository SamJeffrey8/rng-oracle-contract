import subprocess
from pathlib import Path

from src.on_chain import oracle


def main():
    script = Path(oracle.__file__).absolute()
    subprocess.run(f"opshin build {script}".split())


if __name__ == "__main__":
    main()
