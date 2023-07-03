import itertools
from pathlib import Path

nombre_combinaisons = int(input('Entrer le nombre de combinaison que vous voulez : '))  # flemme de gerer les bugs


def password_generator(nombre_combinaisons):
    caracteres = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    longueur = 8
    combinaisons = itertools.islice(itertools.product(caracteres, repeat=longueur), nombre_combinaisons)

    ROOT_FILE = Path(__file__).cwd()
    WORDLIST = ROOT_FILE / "password.txt"

    WORDLIST.touch() if not Path.exists(WORDLIST) else ''

    with open(WORDLIST, 'w') as f:
        for combinaison in combinaisons:
            mot_de_passe = ''.join(combinaison)
            print(mot_de_passe)
            f.write(f'{mot_de_passe}\n')


password_generator(nombre_combinaisons)