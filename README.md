# ADIF Merger

## Overview

This Python application reads all `.adi` (ADIF) files from a specified directory, merges their content while preserving the header from the first file, and saves the combined file with a timestamped filename.

## Features

- Reads ADIF files from a specified directory.
- Extracts and preserves the header from the first file.
- Merges all records into a single ADIF file.
- Saves the output file with a timestamped name.

## Requirements

This application relies only on Python's standard library. No external dependencies are required.

## Usage

Run the script and provide the directory containing ADIF files when prompted:

```sh
python main.py <directory_path>
```
