#/home/vahema! v1.0 Taş-Kağıt-Makas

import random, time as t

print("\nTaş Kağıt Makas\nBy Vahema\n")

oyuncu_adi = input("Kullanıcı Adı : ")

hareketler = ["Taş", "Kağıt", "Makas"]

oyuncu_skor = 0
npc_skor = 0

# print("\n{0}|{1}:{2}|NCP\n".format(oyuncu_adi, oyuncu_skor, npc_skor))

while True:
	npc = random.choice(hareketler)

	oyuncu_el = str(input("El : "))

	if oyuncu_el == "Taş":
		if npc == "Taş":
			print("Berabere")

		elif npc == "Kağıt":
			print("NPC +1")
			npc_skor += 1
			print("\n{0}|{1}:{2}|NCP\n".format(oyuncu_adi, oyuncu_skor, npc_skor))

		elif npc == "Makas":
			print(f"{oyuncu_adi} +1")
			oyuncu_skor += 1
			print("\n{0}|{1}:{2}|NCP\n".format(oyuncu_adi, oyuncu_skor, npc_skor))

	if oyuncu_el == "Kağıt":
		if npc == "Taş":
			print(f"{oyuncu_adi} +1")
			oyuncu_skor	+= 1
			print("\n{0}|{1}:{2}|NCP\n".format(oyuncu_adi, oyuncu_skor, npc_skor))

		if npc == "Kağıt":
			print("Berabere")

		if npc == "Makas":
			print("NPC +1")
			npc_skor += 1
			print("\n{0}|{1}:{2}|NCP\n".format(oyuncu_adi, oyuncu_skor, npc_skor))

	if oyuncu_el == "Makas":
		if npc == "Taş":
			print("NPC +1")
			npc_skor += 1
			print("\n{0}|{1}:{2}|NCP\n".format(oyuncu_adi, oyuncu_skor, npc_skor))

		if npc == "Kağıt":
			print(f"{oyuncu_adi} +1")
			oyuncu_skor += 1
			print("\n{0}|{1}:{2}|NCP\n".format(oyuncu_adi, oyuncu_skor, npc_skor))

		if npc == "Makas":
			print("Berabere")
