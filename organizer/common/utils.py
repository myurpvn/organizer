from organizer.common.logger import logger
import yaml


def read_config_map(folder: str) -> dict[str, str]:

    config_map: dict[str, str] = {}
    try:
        with open("../config_map.yaml", "r") as f:
            config_map_raw = yaml.safe_load(f)
        config_map = config_map_raw[folder]
        config_map["folder"] = folder
        return config_map

    except KeyError:
        logger.exception("Config not found for given folder", folder=folder)
        raise (KeyError)
    except Exception as e:
        logger.exception("Error when reading config file", error=e)
        raise e
