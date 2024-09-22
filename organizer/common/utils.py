from organizer.common.logger import logger
import yaml


def read_config_map(folder_key: str) -> dict[str, str]:

    config_map: dict[str, str] = {}
    try:
        with open("config_map.yaml", "r") as f:
            config_map_raw = yaml.safe_load(f)
    except Exception as e:
        raise e
    else:
        if folder_key not in config_map_raw.keys():
            logger.error("folder is not configured", folder_key=folder_key)
            raise KeyError(f"folder-key: '{folder_key}' is not configured")
        config_map = config_map_raw[folder_key]
        config_map["folder_key"] = folder_key
        return config_map
