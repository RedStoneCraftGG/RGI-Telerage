import requests
import time
import os
import argparse

try:
	parser = argparse.ArgumentParser(description='Contoh penggunaan aplikasi.')
	parser.add_argument('-id', '--chatid', help='ID obrolan')
	parser.add_argument('-t', '--token', help='Token bot')
	parser.add_argument('-m', '--message', help='Pesan yang akan dikirim')
	parser.add_argument('-i', '--image', help='URL gambar opsional')
	parser.add_argument('-d', '--delay', help='Jeda pengiriman dalam detik', type=int)
	args = parser.parse_args()

	if args.chatid:
		chat_id = args.chatid
	else:
		chat_id = input("Chat ID: ")

	if args.token:
		token = args.token
	else:
		token = input("Token Telegram: ")

	if args.message:
		message = args.message
	else:
		message = input("Pesan: ")

	image_url = None
	image_default = "https://redstone.my.id/bolep.jpeg" # JANGAN DIBUKA!

	if not args.image:
		if args.chatid and args.token and args.message and not args.delay:
			image_url = image_default
		elif args.chatid and args.token and args.message and args.delay:
			image_url = image_default
	elif args.image:
		if args.chatid and args.token and args.message and not args.delay:
			image_url = args.image
		elif args.chatid and args.token and args.message and args.delay:
			image_url = args.image
	else:
		image_url = input("Masukan URL gambar (Opsional): ")
		if not image_url:
			image_url = image_default

	if not image_url:
		image_url = input("Masukan URL gambar (Opsional): ")
		if not image_url:
			image_url = image_default



	if args.delay:
		cooldown = args.delay
	else:
		cooldown_input = input("Jeda pengiriman dalam detik (default: 10 detik): ")
		cooldown = float(cooldown_input) if cooldown_input else 10

	url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
	urlimg = f"https://api.telegram.org/bot{token}/sendPhoto?chat_id={chat_id}&photo={image_url}"


	def send():
		response1 = requests.get(url)
		response2 = requests.get(urlimg)

		if "result" in response1.json() and "message_id" in response1.json()["result"]:
			message_id1 = response1.json()["result"]["message_id"]
		else:
			message_id1 = "Error"

		if "result" in response2.json() and "message_id" in response2.json()["result"]:
			message_id2 = response2.json()["result"]["message_id"]
		else:
			message_id2 = "Error"


		if response1.status_code == 200:
			#print("[",message_id1,"] ","Pesan terkirim!")
			message1 = f"[{message_id1}] Pesan terkirim!"
		elif response1.status_code == 429:
			#print("[",message_id1,"] ","Aowaowowaowak API nya down")
			message1 = f"[{message_id1}] Aowaowowaowak API nya down"
		else:
			#print("[",message_id1,"] ","Pesan gagal terkirim")
			message1 = f"[{message_id1}] Pesan gagal terkirim"

		if response2.status_code == 200:
			#print("[",message_id2,"] ","Gambar terkirim!")
			message2 = f"[{message_id2}] Gambar terkirim!"
		elif response2.status_code == 429:
			#print("[",message_id2,"] ","Aowaowowaowak API nya down")
			message2 = f"[{message_id2}] Aowaowowaowak API nya down"
		else:
			#print("[",message_id2,"] ","Gambar gagal terkirim")
			message2 = f"[{message_id2}] Gambar gagal terkirim"

		#os.system('cls' if os.name == 'nt' else "printf '\033c'")
		print(message1 + "\n" + message2)


	while True:
		send()
		time.sleep(cooldown)


except KeyboardInterrupt:
	print("\nMenutup Program...")