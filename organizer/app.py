import time

import typer
import os
from typing_extensions import Annotated

from organizer.models.config_map import ConfigMap
from organizer.common.logger import logger
from organizer.common.utils import read_config_map
from organizer.scripts.functions import get_directory_listing, organize_files

app = typer.Typer()


@app.command()
def main(
    folder: Annotated[
        str | None,
        typer.Option(
            "--folder",
            "-f",
            help="Folder key from the config_map.yaml",
        ),
    ] = None,
    input_path: Annotated[
        str | None,
        typer.Option(
            "--input",
            "-in",
            help="Source folder to organize",
        ),
    ] = None,
    output_path: Annotated[
        str | None,
        typer.Option(
            "--output",
            "-out",
            help="Destination folder for the organized folders (Will move the input folder)",
        ),
    ] = None,
) -> None:

    logger.info("Starting script", folder=folder)

    if folder is not None:
        config_map = ConfigMap(**read_config_map(folder))

    elif input_path is not None and output_path is not None:
        if os.path.exists(input_path):
            config_map = ConfigMap()
            config_map.source_path = input_path
            config_map.destination_path = output_path
        else:
            logger.exception("Input Directory is not valid!")
            raise Exception("Input Directory is not valid!")

    else:
        logger.exception("No input folder/path specified")
        raise Exception("No input folder/path specified")

    start_time = time.time()

    dir_file_map_list = get_directory_listing(config_map)
    if len(dir_file_map_list) != 0:
        organize_files(config_map, dir_file_map_list)
    else:
        logger.info("No files to move")

    logger.info("Script Completed", elapsed_seconds=round(time.time() - start_time, 2))


if __name__ == "__main__":
    app()


# TODO: Add folder-key checks
# TODO: Add option to copy instead of move organized files
