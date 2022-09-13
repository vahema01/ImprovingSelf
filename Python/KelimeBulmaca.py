#!bin/bash/python
# made by vahema

import time as t, random, os

point = 0

def tr():
	global point
	print("[+] True!")
	point += 1

while True:
	os.system("clear")
	kelimeler = ["abandon", "abolish", "absorb", "abundant", "abuse", "accompany", "account", "adapt", "administration", "adverse", "affection", "affection", "amazing", "amusement", "anxiety", "application", "appointment", "apprentice", "approve", "approximate", "arise", "arrest", "arrogant", "artificial", "ashamed", "attach", "attend", "audience", "average", "avord", "award", "ban", "bankruptoy", "bargain", "bench", "beneficial", "betreyol", "bias", "bite", "bitte", "blame", "boil", "border", "borrow", "bottom", "broadcast", "bunch", "burn", "bush", "burn", "bush", "candidate", "capture"]
	kelime = random.choice(kelimeler)

	print("\n$ point : {0}\n\n### {1} ###\n".format(point, kelime.upper()))
	u = input(">>> ")

	if kelime == "abandon":
		if u == "terk etmek":
			tr()
	elif kelime == "abolish":
		if u == "kaldırmak":
			tr()
	elif kelime == "absorb":
		if u == "emmek":
			tr()
	elif kelime == "abundant":
		if u == "bol miktarda":
			tr()
	elif kelime == "abuse":
		if u == "kötüye kullanmak":
			tr()
	elif kelime == "accompany":
		if u == "eşlik etmek":
			tr()
	elif kelime == "account":
		if u == "hesap":
			tr()
	elif kelime == "adapt":
		if u == "uyum sağlamak":
			tr()
	elif kelime == "administration":
		if u == "yönetici":
			tr()
	elif kelime == "adverse":
		if u == "olumsuz":
			tr()
	elif kelime == "affection":
		if u == "sevgi":
			tr()
	elif kelime == "amazing":
		if u == "şaşırtıcı":
			tr()
	elif kelime == "amusement":
		if u == "eğlence":
			tr()
	elif kelime == "anxiety":
		if u == "endişe":
			tr()
	elif kelime == "application":
		if u == "uygulama":
			tr()
	elif kelime == "appointment":
		if u == "atama":
			tr()
	elif kelime == "apprentice":
		if u == "çırak":
			tr()
	elif kelime == "approve":
		if u == "onaylamak":
			tr()
	elif kelime == "aprroximate":
		if u == "yaklaşık":
			tr()
	elif kelime == "arise":
		if u == "meydana gelmek":
			tr()
	elif kelime == "arrest":
		if u == "tutuklamak":
			tr()
	elif kelime == "arrogant":
		if u == "kaba":
			tr()
	elif kelime == "artificial":
		if u == "suni":
			tr()
	elif kelime == "ashamed":
		if u == "utanmış":
			tr()
	elif kelime == "attach":
		if u == "iliştirmek":
			tr()
	elif kelime == "attend":
		if u == "katılmak":
			tr()
	elif kelime == "audience":
		if u == "seyirci":
			tr()
	elif kelime == "average":
		if u == "ortalama":
			tr()
	elif kelime == "avord":
		if u == "kaçınmak":
			tr()
	elif kelime == "award":
		if u == "ödül":
			tr()
	elif kelime == "ban":
		if u == "yasaklamak":
			tr()
	elif kelime == "bankruptoy":
		if u == "iflas":
			tr()
	elif kelime == "bargain":
		if u == "pazarlık":
			tr()
	elif kelime == "bench":
		if u == "bank":
			tr()
	elif kelime == "beneficial":
		if u == "yararlı":
			tr()
	elif kelime == "betreyol":
		if u == "ihanet":
			tr()
	elif kelime == "bias":
		if u == "ön yargı":
			tr()
	elif kelime == "bite":
		if u == "ısırmak":
			tr()
	elif kelime == "bitte":
		if u == "acı":
			tr()
	elif kelime == "blame":
		if u == "suçlamak":
			tr()
	elif kelime == "boil":
		if u == "kaynatmak":
			tr()
	elif kelime == "border":
		if u == "sınır":
			tr()
	elif kelime == "borrow":
		if u == "ödünç almak":
			tr()
	elif kelime == "bottom":
		if u == "taban":
			tr()
	elif kelime == "broadcast":
		if u == "yayınlamak":
			tr()
	elif kelime == "bunch":
		if u == "demet":
			tr()
	elif kelime == "burn":
		if u == "yanmak":
			tr()
	elif kelime == "bush":
		if u == "çalı":
			tr()
	elif kelime == "candidate":
		if u == "aday":
			tr()
	elif kelime == "capture":
		if u == "esir almak":
			tr()

	else:
		print("Error!")

# the end