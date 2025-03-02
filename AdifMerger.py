from AdifReader import AdifReader


import glob
import os


class AdifMerger:
    """
    AdifMerger is a class that handles the merging of ADIF (Amateur Data Interchange Format) files in a specified directory.

    Attributes:
        directory (str): The directory containing ADIF files to be merged.
        adif_files (list): A list of paths to ADIF files in the specified directory.

    Methods:
        __init__(directory):
            Initializes the AdifMerger with the specified directory and finds all ADIF files in that directory.

        merge_files():
            Merges the contents of all ADIF files in the directory. If no ADIF files are found, it prints a message and returns None.
            Returns a single string containing the merged contents of all ADIF files, with headers and records properly combined.
    """
    def __init__(self, directory):
        """
        Initializes the AdifMerger with the specified directory.
        Args:
            directory (str): The path to the directory containing ADIF files.
        Attributes:
            directory (str): The path to the directory containing ADIF files.
            adif_files (list): A list of paths to ADIF files in the specified directory.
        """

        self.directory = directory
        self.adif_files = glob.glob(os.path.join(directory, "*.adi")) + glob.glob(os.path.join(directory, "*.adif"))

    def merge_files(self):
        """
        Merges multiple ADIF (Amateur Data Interchange Format) files into a single ADIF content string.
        This method reads ADIF files from the `self.adif_files` list, extracts their headers and records,
        and combines them into a single ADIF content string. If no ADIF files are found, it prints a message
        and returns None.
        Returns:
            str: The merged ADIF content string, including the header and all records, or None if no ADIF files are found.
        """

        if not self.adif_files:
            print("No ADIF files found in the directory.")
            return None

        header = ""
        records = []

        for file in self.adif_files:
            content = AdifReader.read_file(file)
            if "<eoh>" in content.lower():
                parts = content.split("<eoh>", 1)
                if not header:
                    header = parts[0] + "<eoh>\n"
                records.append(parts[1].strip())
            else:
                records.append(content.strip())

        return header + "\n" + "\n".join(records) + "\n"
