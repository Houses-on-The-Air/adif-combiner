
from AdifMerger import AdifMerger
from AdifWriter import AdifWriter
import sys

def main():
    """
    Main function to merge ADIF files in a specified directory.
    Prompts the user to enter the directory containing ADIF files,
    creates an AdifMerger instance with the provided directory path,
    merges the ADIF files, and saves the merged content if available.
    Raises:
        IOError: If there is an issue reading or writing files.
    """
    if len(sys.argv) != 2:
        print("Usage: python main.py <directory_path>")
        sys.exit(1)

    dir_path = sys.argv[1].strip()
    merger = AdifMerger(dir_path)
    merged_content = merger.merge_files()
    if merged_content:
        AdifWriter.save_file(dir_path, merged_content)

if __name__ == "__main__":
    main()
