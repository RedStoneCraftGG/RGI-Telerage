import requests
import time
import os

try:
	chat_id = input("Chat ID Telegram: ")
	token = input("Token Telegram: ")
	message = input("Pesan: ")

	def get_image_url(image_default):
		image_url = input("Masukan URL gambar (Opsional): ")
		if not image_url:
			image_url = image_default
		return image_url

	cooldown_input = input("Jeda pengiriman dalam detik (default: 10 detik): ")
	if cooldown_input:
    		cooldown = float(cooldown_input)
	else:
    		cooldown = 10

	url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
	image_default = "https://redstone.my.id/bolep.jpeg" # JANGAN DIBUKA!!!
	image_url = get_image_url(image_default)
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