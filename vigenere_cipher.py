from ukrainian_letter_frequences import *


def encrypt(text, key):
    text = text.lower()
    text = [l for l in text if l in ntoa]
    encrypted = ""
    for i, l in enumerate(text):
        encrypted += ntoa[(aton[l]+aton[key[i % len(key)]]) % ALPH_LEN]
    return encrypted


def decrypt(text, key):
    decrypted = ""
    for i, l in enumerate(text):
        decrypted += ntoa[(ALPH_LEN + aton[l] - aton[key[i % len(key)]]) % ALPH_LEN]
    return decrypted


if __name__ == '__main__':
    with open("plain_ukr.txt", 'r') as f:
        text = f.read()

    print(encrypt("весна красна колись прийде", "зима"))
    print(decrypt("ьччжпчьишисаєяйпявааьяч", "зима"))
