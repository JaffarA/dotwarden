import pickle
from base64 import a85decode, a85encode
from os import getcwd, listdir, mkdir, remove

from .word_bank import generate_random_dot_name


class Dotwarden:
    PICKLE_FILE = ".warden"
    PICKLE_PROTOCOL = 4
    PICKLE_STORE = ".warden"
    BYTE_ENCODING = "ASCII"

    def __init__(self):
        self.__warden_dir__ = (
            Dotwarden.pickle_read()
            if Dotwarden.pickle_exists()
            else Dotwarden.encode(generate_random_dot_name())
        )

        if not Dotwarden.pickle_exists():
            Dotwarden.pickle_write(self.__warden_dir__)

        if self.warden_dir not in listdir(getcwd()):
            mkdir(self.warden_dir)

    @property
    def warden_dir(self):
        return Dotwarden.decode(self.__warden_dir__)

    def destroy(self) -> bool:
        try:
            remove(Dotwarden.PICKLE_FILE)
            self.existing_pickle = False
            return True
        except Exception as err:
            print(f"Error occured: {err}")
            return False

    @staticmethod
    def encode(string_value):
        return a85encode(
            b=bytes(string_value, encoding=Dotwarden.BYTE_ENCODING),
            foldspaces=False,
            pad=False,
            adobe=False,
        )

    @staticmethod
    def decode(encoded_value):
        return str(
            a85decode(b=encoded_value, foldspaces=False, adobe=False),
            encoding=Dotwarden.BYTE_ENCODING,
        )

    @staticmethod
    def pickle_exists(pickle_file=PICKLE_FILE, dir=getcwd()) -> bool:
        return True if pickle_file in listdir(dir) else False

    @staticmethod
    def pickle_write(value, pickle_file=PICKLE_FILE) -> None:
        with open(pickle_file, "wb") as write_file:
            pickle.dump(obj=value, file=write_file, protocol=Dotwarden.PICKLE_PROTOCOL)

    @staticmethod
    def pickle_read(pickle_file=PICKLE_FILE) -> str:
        with open(pickle_file, "rb") as read_file:
            return pickle.load(read_file)
