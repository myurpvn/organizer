# Organizer - *Directory organizing tool*

## Introduction

A python CLI tool to organize a folder based on their file type

## Table of contents

- [Organizer - *Directory organizing tool*](#organizer---directory-organizing-tool)
  - [Introduction](#introduction)
  - [Table of contents](#table-of-contents)
  - [Getting Started](#getting-started)
    - [Using Poetry - recommended](#using-poetry---recommended)
    - [Using pip](#using-pip)
    - [Create Configuration file](#create-configuration-file)
    - [Running the App](#running-the-app)
  - [Organizer folder structure](#organizer-folder-structure)
  - [Notes](#notes)

## Getting Started

### Using Poetry - recommended

- Install Poetry
  - `poetry` - [follow steps here!](https://python-poetry.org/docs/#installation)

- Install dependencies

    ```bash
    poetry install
    ```

### Using pip

- Create a virtual environment and activate - [follow steps here!](https://docs.python.org/3/tutorial/venv.html)
  - Unix or MacOS

    ```bash
    python -m venv <venv_name>
    source <venv_name>/bin/activate
    ```

  - Windows

    ```powershell
    python -m venv <venv_name>
    <venv_name>\Scripts\activate
    ```

- Install dependencies

    ```bash
    pip install -r requirement.txt
    ```

### Create Configuration file

- create a `yaml` file and name it as `config_map.yaml`

    ```bash
    touch config_map.yaml
    ```

- Follow the below structure to populate the `config_map.yaml`

    ```yaml
    folder-key: # (Required) [case-sensitive]
        source_path: # (Required) path of the folder to be organized
        destination_path: # (Optional) [Default: source_path]

- You can have multiple folders configured here in `config_map.yaml`

    ```yaml
    # sample contents of config_map.yaml
    
    # writes in the same directory as "source_path"
    Downloads:
        source_path: "/Users/johndoe/Downloads"

    # writes to a "destination_path"
    Documents:
        source_path: "/Users/johndoe/Documents"
        destination_path: "/Users/johndoe/organized/Documents"

    # folder key is case-sensitive
    documents:
        source_path: "/Users/johndoe/documents"
    Documents:
        source_path: "/Users/johndoe/Documents"
    ```

### Running the App

- Using poetry - *for poetry installation method*

    ```bash
    # using -fkey
    poetry run app -fkey <folder_key>
    ```

    ```bash
    # using -s and -d
    poetry run app -s <source_path> -d <destination_path>
    ```

- Using python - *for pip installation method*

    ```bash
    # using -fkey
    python -m organizer -fkey <folder_key>
    ```

    ```bash
    # using -s and -d
    python -m organizer -s <source_path> -d <destination_path>
    ```

## Organizer folder structure

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

- After running `Organizer`

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

## Notes

- `Organizer` ignores any folders inside the source folder
