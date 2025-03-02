import datetime
import os


class AdifWriter:
    """
    A class used to write ADIF (Amateur Data Interchange Format) files.
    Methods
    -------
    save_file(directory, merged_content)
        Saves the merged ADIF content to a file in the specified directory with a timestamped filename.

        Parameters
        ----------
        directory : str
            The directory where the merged ADIF file will be saved.
        merged_content : str
            The content to be written to the ADIF file.
        Returns
        -------
        None
    """

    @staticmethod
    def save_file(directory, merged_content):
        """
        Saves the merged ADIF content to a file in the specified directory with a timestamped filename.
        Args:
            directory (str): The directory where the file will be saved.
            merged_content (str): The content to be written to the file.
        Returns:
            None
        """
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f"merged_{timestamp}.adi"
        output_path = os.path.join(directory, output_filename)

        with open(output_path, 'w', encoding='utf-8') as output_file:
            output_file.write(merged_content)

        print(f"Merged ADIF file saved as: {output_filename}")
