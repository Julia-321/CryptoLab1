import vigenere_cipher as vc
from ukrainian_letter_frequences import *
import matplotlib.pyplot as plt
import numpy as np

K = 40

# alphabet = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
# alphabet = "abcdefghijklmnopqrstuvwxyz"


# def coincidence_index(text1, text2):
#     if len(text1) != len(text2):
#         raise ValueError("texts have different length")
#     cnt = 0
#     for i in range(len(text1)):
#         if text1[i]==text2[i]:
#             cnt+=1
#     return cnt/len(text1)*ALPH_LEN


def coincidence_index(text):
    sum = 0
    for l in ntoa:
        cnt = text.count(l)
        sum += cnt*(cnt-1)
    return sum/len(text)/(len(text)-1)


def analyze_key_length(text):
    ci = [0 for i in range(K+1)]
    for i in range(1, K):
        ci[i] = coincidence_index(text, text[i:]+text[:i])
        print(i, ci[i])



    fig = plt.figure()
    ax = fig.gca()
    ax.set_xticks(np.arange(0, K+1, 1))
    ax.set_yticks(np.arange(0, 0, 1))
    plt.plot(ci, '.')
    plt.grid()
    plt.show()

def analyze_encrypted_text(text):
    # analyze_key_length(text)
    text = text.lower()
    text = [l for l in text if l in ntoa]
    aci = [0 for i in range(K+1)]
    for i in range(2, 40):
        s = 0
        for j in range(i):
            s += coincidence_index(text[::i])
        aci[i] = s/i
        print(i, s/i)

    fig = plt.figure()
    ax = fig.gca()
    ax.set_xticks(np.arange(0, K + 1, 1))
    ax.set_yticks(np.arange(0, 0, 1))
    plt.plot(aci, '.')
    plt.grid()
    plt.show()

    return proposed

with open("plain.txt", 'r') as f:
    text = f.read()

analyze_encrypted_text(vc.encrypt(text, "ключавс"))