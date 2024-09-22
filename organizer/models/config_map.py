class ConfigMap:

    folder_key: str = "N/A"
    move_folders: bool = False
    source_path: str = ""
    destination_path: str = ""

    def __init__(self, **kwargs) -> None:
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return str(self.__dict__)
