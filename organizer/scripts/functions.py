import mimetypes
import shutil
from pathlib import Path

from organizer.models.config_map import ConfigMap
from organizer.common.logger import logger


def get_directory_listing(config_map: ConfigMap) -> list[dict[str, str]]:

    source_root_dir: str = config_map.source_path
    logger.info("Finding files", directory=source_root_dir)

    file_map_list: list[dict[str, str]] = []
    path = Path(source_root_dir)

    for file in path.glob("*"):

        file_map: dict[str, str] = {}
        file_type = (
            "folders"
            if (file.is_dir() and config_map.move_folders)
            and not file.name.startswith("_")
            else mimetypes.guess_type(file.as_uri())[0] or "UnknownType"
        )
        if file_type in ["UnknownType", "folders"]:
            continue

        file_type_split: list[str] = file_type.split("/")
        file_map["file_type"] = (
            file_type_split[0]
            if file_type_split[0] != "application"
            else file_type_split[1]
        )
        file_map["file_name"] = file.name

        logger.info("file found", file_name=file.name, mime_file_type=file_type)

        file_map_list.append(file_map)

    return file_map_list


def organize_files(
    config_map: ConfigMap,
    file_map_list: list[dict[str, str]],
) -> None:

    logger.info("Organizing files", files_to_move=len(file_map_list))

    source_root_dir = config_map.source_path
    destination_root_dir = config_map.destination_path

    for file_map in file_map_list:
        file_name: str = file_map["file_name"]
        file_type: str = file_map["file_type"]

        destination_folder_path: str = (
            destination_root_dir + f"/_{file_type}"
            if config_map.move_folders
            else destination_root_dir + f"/{file_type}"
        )
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
