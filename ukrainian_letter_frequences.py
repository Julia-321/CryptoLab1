FREQUENCIES = {'а': 0.074, 'б': 0.018, 'в': 0.054, 'г': 0.016, 'ґ': 0.001, 'д': 0.036, 'е': 0.017,
                                'є': 0.008, 'ж': 0.009, 'з': 0.024, 'и': 0.063,
                                'і': 0.059, 'ї': 0.006, 'й': 0.009, 'к': 0.036, 'л': 0.037, 'м': 0.032, 'н': 0.067,
                                'о': 0.097, 'п': 0.023, 'р': 0.049, 'с': 0.042,
                                'т': 0.057, 'у': 0.041, 'ф': 0.001, 'х': 0.012, 'ц': 0.006, 'ч': 0.019, 'ш': 0.012,
                                'щ': 0.001, 'ю': 0.004, 'я': 0.030, 'ь': 0.030}

ntoa = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
aton = dict(zip("абвгґдеєжзиіїйклмнопрстуфхцчшщьюя", range(33)))
ALPH_LEN = len(ntoa)

CI = sum([FREQUENCIES[l]**2 for l in FREQUENCIES.keys()])

print("Ukrainian CI: {}\nUniform CI: {}".format(CI, 1/33))
