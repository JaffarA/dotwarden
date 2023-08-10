from random import choice

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
