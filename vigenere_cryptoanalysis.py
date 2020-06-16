import codecs

import vigenere_cipher as vc
from ukrainian_letter_frequences import *
import matplotlib.pyplot as plt
import numpy as np

K = 40
INF = 1e9

def coincidence_index(text):
    sum = 0
    for l in ntoa:
        cnt = text.count(l)
        sum += cnt*(cnt-1)
    return sum/len(text)/(len(text)-1)

def get_max_inds(l, k=3):
    l = l.copy()
    ans = [0 for i in range(k)]
    for i in range(k):
        ans[i] = l.index(max(l))
        l[ans[i]] = -INF
    return ans


def analyze_key_length(text):
    aci = [0 for i in range(K + 1)]
    for i in range(2, 40):
        s = 0
        for j in range(i):
            s += coincidence_index(text[::i])
        aci[i] = s / i
        # print(i, s / i)

    # fig = plt.figure()
    # ax = fig.gca()
    # ax.set_xticks(np.arange(0, K+1, 1))
    # ax.set_yticks(np.arange(0, 0, 1))
    # plt.plot(ci, '.')
    # plt.grid()
    # plt.show()


    # print(get_max_inds(aci))
    return np.gcd.reduce(get_max_inds(aci))

def chi_squared(text, shift=0):
    sum = 0
    for i in range(ALPH_LEN):
        letter = ntoa[(i+ALPH_LEN*10-shift)%ALPH_LEN]
        p = FREQUENCIES[letter]
        sum += (text.count(ntoa[i]) - len(text)*p)**2/(len(text)*p)
    return sum

def analyze_encrypted_text(text):
    text = text.lower()
    text = [l for l in text if l in ntoa]

    key_length = analyze_key_length(text)
    # print("Key length: {}".format(key_length))

    key = [0 for i in range(key_length)]
    for i in range(key_length):
        chunk = text[i::key_length]
        chsq = [INF for j in range(ALPH_LEN)]
        for shift in range(ALPH_LEN):
            chsq[shift] = chi_squared(chunk, shift)
        key[i] = ntoa[chsq.index(min(chsq))]
    # print("Key: {}".format("".join(key)))
    proposed = vc.decrypt(text, ''.join(key))
    return proposed


if __name__== "__main__":
    with codecs.open("plain_ukr.txt", encoding="utf-8") as f:
        text = f.read()

    print(analyze_encrypted_text(vc.encrypt(text, "поттер")))