# By Vahema

import time as t, random, os

# Giris

t.sleep(1)

print("\n# Sayi Bulmaca #\n#    By Vahema #\n")

t.sleep(0.5)

# Atama

input_range = int(input("Maksimum Sayi : "))

t.sleep(0.5)

sayi_range = range(input_range)

random_sayi = random.choice(sayi_range)

input_deneme = 0

# Dongu

while True:
	input_kullanici = int(input(">>> "))

	input_deneme += 1

	t.sleep(0.2)

	if input_kullanici < random_sayi:
		print("\n[<] Kucuk\n")

	elif input_kullanici > random_sayi:
		print("\n[>] Buyuk\n")

	elif input_kullanici == random_sayi:
		print(f"\n[!] Tebrikler {input_deneme} Denemede Kazandiniz!\n")
		exit()
