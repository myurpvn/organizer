# Organizer - *Directory organizing tool*

## Introduction

A python CLI tool to organize a folder based on their file type

## Table of contents

- [Organizer - *Directory organizing tool*](#organizer---directory-organizing-tool)
  - [Introduction](#introduction)
  - [Table of contents](#table-of-contents)
  - [Getting Started](#getting-started)
    - [Organizer folder structure](#organizer-folder-structure)
    - [Running the Organizer](#running-the-organizer)

## Getting Started

- Prerequisite
  - `poetry` - [install here!](https://python-poetry.org/docs/#installation)
- Install dependencies

    ```bash
    poetry install
    ```

- create a `yaml` file and name it as `config_map.yaml`

    ```bash
    touch config_map.yaml
    ```

- Follow the below structure to populate the `config_map.yaml`

    ```yaml
    folder-key: # this will be used in the CLI input arguement as --folder/-f (case-sensitive)
        move_folders: # boolean value
            # True: will move any folders inside the source_path to a "folder" named folder
            # False: ignore any folders in source_path
        source_path: # path to the folder to be organized
        destination_path: # destination path to move/copy the organized files

- You can have multiple folders configured here in `config_map.yaml`

    ```yaml
    # sample contents of config_map.yaml
    
    # ignore any folders and organize file in the same directory
    Downloads:
        move_folders: False
        source_path: "/Users/johndoe/Downloads"
        destination_path: "/Users/johndoe/Downloads"

    # move folders and move the organized files to a new destination
    Documents:
        move_folders: True
        source_path: "/Users/johndoe/Documents"
        destination_path: "/Users/johndoe/organized/Documents"

    # folder key is case-sensitive so can help match case-sensitive folder names
    documents:
        move_folders: False
        source_path: "/Users/johndoe/documents"
        destination_path: "/Users/johndoe/documents"
    ```

### Organizer folder structure

- Before running `Organizer`

    ```bash
    .
    ├── IMG_5961.HEIC
    ├── IMG_5961.png
    ├── Screenshot.jpg
    ├── The-Starter-Guide-in-Modern-Data.pdf
    ├── big-enderman-face.png
    ├── big-wither-face.png
    ├── processing-4.3-macos-aarch64.zip
    ├── random_name_generator_copy
    │   ├── female_first_names.txt
    │   ├── first_names.txt
    │   ├── last_names.txt
    │   ├── main.py
    │   ├── male_first_names.txt
    │   └── middle_names.txt
    ├── sign.png
    └── structured-streaming.py
    ```

- After running `Organizer` - *with move_folder set to* `False`

    ```bash
    .
    ├── image
    │   ├── IMG_5961.HEIC
    │   ├── IMG_5961.png
    │   ├── Screenshot.jpg
    │   ├── big-enderman-face.png
    │   ├── big-wither-face.png
    │   └── sign.png
    ├── pdf
    │   └── The-Starter-Guide-in-Modern-Data.pdf
    ├── random_name_generator_copy
    │   ├── female_first_names.txt
    │   ├── first_names.txt
    │   ├── last_names.txt
    │   ├── main.py
    │   ├── male_first_names.txt
    │   └── middle_names.txt
    ├── text
    │   └── structured-streaming.py
    └── zip
        └── processing-4.3-macos-aarch64.zip
    ```

### Running the Organizer

- Running the organizer

    ```bash
    # folder-key is passed in folder arg
    poetry run app --folder Downloads
    ```

- Running the organizer without any configurations in `config_map.yaml`

    ```bash
    # example args
    poetry run app --input /Users/johndoe/pictures --output /Users/johndoe/pictures/organized
    ```
