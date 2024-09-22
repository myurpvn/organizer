import time

import typer
import os
from typing_extensions import Annotated

from organizer.models.config_map import ConfigMap
from organizer.common.logger import logger
from organizer.common.utils import read_config_map
from organizer.scripts.functions import (
    get_directory_listing_with_mappings,
    organize_files,
)

app = typer.Typer()


@app.command()
def main(
    folder_key: Annotated[
        str,
        typer.Option(
            "--folder-key",
            "-fkey",
            help="Folder key from the config_map.yaml",
        ),
    ] = "",
    source_path: Annotated[
        str,
        typer.Option(
            "--source",
            "-s",
            help="Source folder to organize",
        ),
    ] = "",
    destination_path: Annotated[
        str,
        typer.Option(
            "--destination",
            "-d",
            help="Destination path to move the organized folders",
        ),
    ] = "",
) -> None:

    params = {
        "source_path": source_path,
        "destination_path": destination_path,
    }

    if folder_key == "":
        config_map = ConfigMap(**params)
    else:
        config_map = ConfigMap(**read_config_map(folder_key))

    if config_map.source_path == "" or not os.path.exists(config_map.source_path):
        logger.error(
            "Source Directory is not valid or doesn't exists!",
            source_directory=source_path,
        )
        raise Exception("Source Directory is not valid or doesn't exists!")

    logger.info(
        "Starting script",
        folder_key=config_map.folder_key,
        # source_path=config_map.source_path,
        # destination_path=config_map.destination_path,
        # move_folder=config_map.move_folders,
    )

    if config_map.destination_path == "":
        logger.warn("No destination specified! Using source path as destination")
        config_map.destination_path = config_map.source_path

    start_time = time.time()
    dir_file_map_list = get_directory_listing_with_mappings(config_map)
    if len(dir_file_map_list) != 0:
        organize_files(config_map, dir_file_map_list)
    else:
        logger.info("No files to organize!")

    logger.info(
        "Script Completed",
        elapsed_time_in_seconds=round(time.time() - start_time, 2),
    )


if __name__ == "__main__":
    app()


# TODO: Add option to copy instead of move organized files
