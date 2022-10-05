from pathlib import Path
from typing import Any

import typer


app = typer.Typer()


@app.command('run')
def main(directory: str = typer.Argument(..., help="The path in which to sort")):
    directory = Path(directory)

    if not directory.exists():
        typer.secho("The path specified doesn't exists")
        raise typer.Exit()

    typer.secho("Here is the list of found files", fg=typer.colors.BRIGHT_BLUE)

    for files in directory.iterdir():
        typer.secho(f"'{files}'", fg=typer.colors.BRIGHT_RED)

    extension_mapping: dict[str | Any, str | Any] = {
        ".json": "Documents",
        ".js": "Documents",
        ".odp": "Documents",
        ".ppt": "Documents",
        ".docx": "Documents",
        ".xls": "Documents",
        ".doc": "Documents",
        ".css": "Documents",
        ".pages": "Documents",
        ".mp3": "Music",
        ".wav": "Music",
        ".flac": "Music",
        ".gif": "Images",
        ".png": "Images",
        ".jpg": "Images",
        ".jpeg": "Images",
        ".bmp": "Images",
        ".mov": "Videos",
        ".webm": "Videos",
        ".mp4": "Videos",
        ".avi": "Videos",
        ".iso": "Compressed",
        ".zip": "Compressed",
        ".rar": "Compressed",
        ".tar.gz": "Compressed",
        ".exe": "Setup"
    }

    typer.confirm("Do you want to sort ? ", abort=True)

    files = [f for f in directory.iterdir() if f.is_file()]

    for file in files:
        # We get the specified folder according to the suffix of the file.
        target_folder = extension_mapping.get(file.suffix, "Divers")

        # We get the specified absolute path of the target folder concatenate with the base path.
        target_folder_absolute = directory / target_folder

        # Now we create the folder
        target_folder_absolute.mkdir(exist_ok=True)

        # Now we concatenate the file name with the absolute path
        target_file = target_folder_absolute / file.name

        # Finally we move the file
        file.rename(target_file)


if __name__ == "__main__":
    app()

