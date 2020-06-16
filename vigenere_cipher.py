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
    print(encrypt("Містер і місіс Дурслі, що жили в будинку номер чотири на вуличці Прівіт-драйв, пишалися тим, що були, слава Богу, абсолютно нормальними. Кого-кого, але тільки не їх можна було б запідозрити, що вони пов'язані з таємницями чи дивами, бо такими дурницями вони не цікавилися.",
                  "ключ"))
    print(decrypt("ьччжпчьишисаєяйпявааьяч", 'зима'))
