import requests
import time
import os
import argparse

try:
	parser = argparse.ArgumentParser(description='Contoh penggunaan aplikasi.')
	parser.add_argument('-id', '--chatid', help='ID chat')
	parser.add_argument('-t', '--token', help='Token bot')
	parser.add_argument('-m', '--message', help='Pesan yang akan dikirim')
	parser.add_argument('-i', '--image', help='URL gambar. opsional')
	parser.add_argument('-d', '--delay', help='Jeda pengiriman dalam detik', type=int)
	parser.add_argument('-v', '--verbose', help='Menampilkan pesan verbose', action='store_true')
	args = parser.parse_args()

	if args.chatid:
		chat_id = args.chatid
	else:
		chat_id = input("Chat ID Telegram: ")

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

	print("\n")

	url = f"https://api.telegram.org/bot{token}/sendMessage?parse_mode=markdown&chat_id={chat_id}&text={message}"
	urlimg = f"https://api.telegram.org/bot{token}/sendPhoto?chat_id={chat_id}&photo={image_url}"

	def send(verbose=False):
		response1 = requests.get(url)
		response2 = requests.get(urlimg)

		if "result" in response1.json() and "message_id" in response1.json()["result"]:
			message_id1 = response1.json()["result"]["message_id"]

			#Verbose
			message_text = response1.json()["result"]["text"]
			bot_name = response1.json()["result"]["from"]["first_name"]
			bot_nickname = response1.json()["result"]["from"]["username"]
			bot_id = response1.json()["result"]["from"]["id"]
			chat_id = response1.json()["result"]["chat"]["id"]
			chat_type = response1.json()["result"]["chat"]["type"]

			receiver_name = "Unknown"
			if "first_name" in response1.json()["result"]["chat"]:
				receiver_name = response1.json()["result"]["chat"]["first_name"]

			chat_title = "Unknown"
			if "title" in response1.json()["result"]["chat"]:
				chat_title = response1.json()["result"]["chat"]["title"]

		else:
			message_id1 = "Error"

		if "result" in response2.json() and "message_id" in response2.json()["result"]:
			message_id2 = response2.json()["result"]["message_id"]

			#Verbose
			if "photo" in response2.json()["result"]:
				for photo in response2.json()["result"]["photo"]:
					width = photo['width']
					height = photo['height']
					file_size = photo['file_size']
		else:
			message_id2 = "Error"


		if response1.status_code == 200:
			#print("[",message_id1,"] ","Pesan terkirim!")
			message1 = f"[{message_id1}] Pesan terkirim!"
			if args.verbose == True:
				message1 = f"[{message_id1}] Pesan terkirim!\nMessage: '{message_text}'\nBot Name: '{bot_name}'\nBot Nickname: '{bot_nickname}'\nBot ID: {bot_id}\nReceiver: '{receiver_name}'\nChat Title: '{chat_title}'\nChat ID: {chat_id}\nChat Type: {chat_type}\n"
		elif response1.status_code == 429:
			#print("[",message_id1,"] ","Aowaowowaowak API nya down")
			message1 = f"[{message_id1}] Aowaowowaowak API nya down"
		else:
			#print("[",message_id1,"] ","Pesan gagal terkirim")
			message1 = f"[{message_id1}] Pesan gagal terkirim"

		if response2.status_code == 200:
			#print("[",message_id2,"] ","Gambar terkirim!")
			message2 = f"[{message_id2}] Gambar terkirim!"
			if args.verbose == True:
				message2 = f"[{message_id2}] Gambar terkirim!\nSize: {round(file_size / 1024, 2)} Kb\nResolution: {width}x{height}\n"
		elif response2.status_code == 429:
			#print("[",message_id2,"] ","Aowaowowaowak API nya down")
			message2 = f"[{message_id2}] Aowaowowaowak API nya down"
		else:
			#print("[",message_id2,"] ","Gambar gagal terkirim")
			message2 = f"[{message_id2}] Gambar gagal terkirim"

		#os.system('cls' if os.name == 'nt' else "printf '\033c'")
		print(message1 + "\n" + message2)

		#print(requests.get(url).json())
		#print(requests.get(urlimg).json())

	while True:
		send()
		time.sleep(cooldown)


except KeyboardInterrupt:
	print("\nMenutup Program...")