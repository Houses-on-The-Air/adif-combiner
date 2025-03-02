class AdifReader:
    """
    AdifReader is a class that provides functionality to read ADIF (Amateur Data Interchange Format) files.
    Methods:
        read_file(file_path: str) -> str:
            Reads the content of an ADIF file specified by the file_path.
            Args:
                file_path (str): The path to the ADIF file to be read.
            Returns:
                str: The content of the ADIF file as a string.
    """
    @staticmethod
    def read_file(file_path):
        """
        Reads the content of a file and returns it as a string.
        Args:
            file_path (str): The path to the file to be read.
        Returns:
            str: The content of the file.
        """

        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
