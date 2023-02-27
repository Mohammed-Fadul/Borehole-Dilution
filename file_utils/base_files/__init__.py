import os
from pathlib import Path
# Authoured by Geovanna
#class to check whether required data files exist
class BaseFile:
    """
    :CLASS BaseFile:

    :arg            filepath    (str)   points to a valid or invalid filepath

    :properties
        filepath                (str)   pointing to the whole path within the system
        filename                (str)   indicates the file name with extension
        parent                  (pathlib.Path.parent)   indicates parent
        extension               (str)   indicates the extension of a BaseFile

    """

    def __init__(self, filepath: str, **kwargs):
        self.__set_filepath(filepath)
        self.__set_filename()
        self.__set_parent()
        self.__set_extension()

    def __set_filepath(self, filepath):
        if not os.path.exists(filepath):
            raise FileExistsError("BaseFileERROR: Specified Basefile does not exist!")
        self.__filepath_obj = Path(filepath)
        self.filepath = str(self.__filepath_obj)

    def __set_filename(self):
        self.filename = self.__filepath_obj.name

    def __set_parent(self):
        self.parent = self.__filepath_obj.parent

    def __set_extension(self):
        self.extension = self.__filepath_obj.suffix
