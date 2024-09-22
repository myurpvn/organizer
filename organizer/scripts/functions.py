import mimetypes
import shutil
from pathlib import Path
from collections import defaultdict

from organizer.models.config_map import ConfigMap
from organizer.common.logger import logger


def get_directory_listing_with_mappings(config_map: ConfigMap) -> dict[str, list[str]]:

    types_to_ignore: list[str] = [
        "UnknownType",
        "folder",
    ]

    source_root_dir: str = config_map.source_path
    logger.info("Finding files", directory_to_organize=source_root_dir)

    path = Path(source_root_dir)
    file_type_to_file_name_map: dict[str, list[str]] = defaultdict(list)

    for file in path.glob("*"):

        file_type = (
            "folder"
            if file.is_dir() and not file.name.startswith("_")
            else mimetypes.guess_type(file.as_uri())[0] or "UnknownType"
        )
        if file_type in types_to_ignore:
            continue

        file_type_split: list[str] = file_type.split("/")
        file_type: str = (
            file_type_split[1]
            if file_type_split[0] == "application"
            else file_type_split[0]
        )

        file_type_to_file_name_map[file_type].append(file.name)

    # logger.info(
    #     "Files mapped",
    #     file_type_to_file_name_map=file_type_to_file_name_map.items(),
    # )

    return file_type_to_file_name_map


def organize_files(
    config_map: ConfigMap,
    file_map_list: dict[str, list[str]],
) -> None:

    logger.info("Organizing files", number_of_files=len(file_map_list))

    source_root_dir = config_map.source_path
    destination_root_dir = config_map.destination_path

    logger.info(
        "Moving files to destination",
        destination_directory=destination_root_dir,
    )

    for file_type, file_name_list in file_map_list.items():

        destination_folder_path: str = (
            destination_root_dir + f"/_{file_type}"
            if config_map.move_folders
            else destination_root_dir + f"/{file_type}"
        )

        for file_name in file_name_list:

            destination_path: str = destination_folder_path + f"/{file_name}"
            source_path: str = source_root_dir + f"/{file_name}"

            if file_type != "folders":
                Path(destination_folder_path).mkdir(
                    parents=True,
                    exist_ok=True,
                )

            shutil.move(
                source_path,
                destination_path,
            )

    logger.info("Folder Organized")
