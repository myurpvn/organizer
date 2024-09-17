import time

import typer
from typing_extensions import Annotated

from organizer.models.config_map import ConfigMap
from organizer.common.logger import logger
from organizer.common.utils import read_config_map
from organizer.scripts.downloads import get_file_map_list, organize_files

app = typer.Typer()


@app.command()
def main(
    folder: Annotated[
        str,
        typer.Option("--folder", "-f"),
    ]
) -> None:

    logger.info("Starting script", folder=folder)

    start_time = time.time()
    config_map = ConfigMap(**read_config_map(folder))
    file_map_list = get_file_map_list(config_map)

    (
        logger.info("No files to move")
        if len(file_map_list) == 0
        else organize_files(config_map, file_map_list)
    )

    logger.info("Script Completed", elapsed_seconds=round(time.time() - start_time, 2))


if __name__ == "__main__":
    app()
