from base64 import a85encode
from base64 import a85decode
from random import choice
from os import listdir
from os import remove
from os import getcwd
from os import mkdir
import pickle


E_WORD_LEN = 3
E_WORD_BANK = [
    "fjor",
    "darling",
    "cavern",
    "alpha",
    "gamma",
    "novice",
    "adept",
    "slime",
    "tyr",
    "ragnor",
    "henrik",
]


def generate_random_dot_name(name_len=E_WORD_LEN, name_bank=E_WORD_BANK) -> str:
    names = []
    while len(names) < name_len:
        c = choice(name_bank)
        if c not in names:
            names.append(c)
    return f".{'-'.join(names)}"


class Dotwarden:

    PICKLE_FILE = ".fwarden_STORE"
    PICKLE_PROTOCOL = 4
    PICKLE_STORE = "warden_STORE"
    BYTE_ENCODING = "ASCII"

    def __init__(self):

        self.__warden_dir__ = (
            Warden.pickle_read()
            if Warden.pickle_exists()
            else Warden.encode(generate_random_dot_name())
        )

        if not Warden.pickle_exists():
            Warden.pickle_write(self.__warden_dir__)

        if self.warden_dir not in listdir(getcwd()):
            mkdir(self.warden_dir)

    @property
    def warden_dir(self):
        return Warden.decode(self.__warden_dir__)

    def destroy(self) -> bool:
        try:
            remove(Warden.PICKLE_FILE)
            self.existing_pickle = False
            return True
        except Exception as err:
            print(f"Error occured: {err}")
            return False

    @staticmethod
    def encode(string_value):
        return a85encode(
            b=bytes(string_value, encoding=Warden.BYTE_ENCODING),
            foldspaces=False,
            pad=False,
            adobe=False,
        )

    @staticmethod
    def decode(encoded_value):
        return str(
            a85decode(b=encoded_value, foldspaces=False, adobe=False),
            encoding=Warden.BYTE_ENCODING,
        )

    @staticmethod
    def pickle_exists(pickle_file=PICKLE_FILE, dir=getcwd()) -> bool:
        return True if pickle_file in listdir(dir) else False

    @staticmethod
    def pickle_write(value, pickle_file=PICKLE_FILE) -> None:
        with open(pickle_file, "wb") as write_file:
            pickle.dump(obj=value, file=write_file, protocol=Warden.PICKLE_PROTOCOL)

    @staticmethod
    def pickle_read(pickle_file=PICKLE_FILE) -> str:
        with open(pickle_file, "rb") as read_file:
            return pickle.load(read_file)
