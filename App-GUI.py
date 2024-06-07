from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from pathlib import Path
from io import BytesIO
import requests
import threading
import time
import os
import re

# pillow, requests

def print_selection():
    if var1.get() == 1:
        url_image.config(state='normal')
        b_img.config(state='normal')
    else:
        url_image.config(state='disabled')
        b_img.config(state='disabled')

def strstp():
    if loop_running.get():
         start_button.config(state='disabled')
         stop_button.config(state='normal')
         url_image.config(state='disabled')
         b_img.config(state='disabled')
         ci.config(state='disabled')
    else:
         start_button.config(state='normal')
         stop_button.config(state='disabled')
         url_image.config(state='normal')
         b_img.config(state='normal')
         ci.config(state='normal')

def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
    if file_path:
        url_image.delete(0, 'end')
        img = Image.open(file_path)
        url_image.insert(0, file_path)

def start_program():
    loop_running.set(True)
    strstp()
    print("Loop dimulai!")
    while loop_running.get():
        cooldown_value, image_value, message_value, token_value, id_value = get_value()
        url = f"https://api.telegram.org/bot{token_value}/sendMessage?chat_id={id_value}&text={message_value}"

        if var1.get() == 1:
            path = url_image.get()
            if is_url(path):
                urlimg = f"https://api.telegram.org/bot{token_value}/sendPhoto?chat_id={id_value}&photo={image_value}"
                print(requests.get(urlimg).json())
            else:
                file_path = Path(image_value)
                urlimg = f'https://api.telegram.org/bot{token_value}/sendPhoto?chat_id={id_value}'
                if image_value and not is_url(path):
                    try:
                        with file_path.open('rb') as file:
                            response = requests.post(urlimg, files={'photo': file})
                            print(response.json())
                    except FileNotFoundError:
                        print(f"File not found")
                    except Exception as e:
                        print(f"Error: {e}")
        else:
            urlimg = ""

        print(requests.get(url).json())

        if var1.get() == 0:
            print("image disabled")

        time.sleep(int(cooldown_value))

def stop_program():
    loop_running.set(False)
    strstp()
    print("Loop dihentikan!")

def start_loop_in_thread():
    thread = threading.Thread(target=start_program)
    thread.start()

def is_url(path):
    url_pattern = re.compile(r'^(http|https|ftp):\/\/')
    return re.match(url_pattern, path) is not None

################################################

def get_value():
    cooldown_value = cooldown_input.get()

    if not cooldown_value:
        cooldown_value = 0

    image_value = url_image.get()
    message_value = message_input.get()
    token_value = token_input.get()
    id_value = chatid_input.get()

    default_image = "https://redstone.my.id/bolep.jpeg" # JANGAN DIBUKA!!!

    if var1.get() == 1:
        if image_value:
            image_value = image_value
        else:
            print("image path empty")
    else:
        image_value = default_image

    return cooldown_value, image_value, message_value, token_value, id_value

################################################

root = Tk()
root.geometry("500x380")
root.title('RGI Telerage')

loop_running = BooleanVar(value=True)

chatid = Label(root, text="ID Chat Telegram")
chatid.pack(anchor='w', padx=10, pady=2)
chatid_input = Entry(root)
chatid_input.pack(anchor='w', padx=10, fill="both")

token_l = Label(root, text="Token Bot Telegram")
token_l.pack(anchor='w', padx=10, pady=2)
token_input = Entry(root)
token_input.pack(anchor='w', padx=10, fill="both")

message = Label(root, text="Pesan")
message.pack(anchor='w', padx=10, pady=2)
message_input = Entry(root)
message_input.pack(anchor='w', padx=10, fill="both")

var1 = IntVar()

ci = Checkbutton(root, text='Kirim dengan gambar', variable=var1, onvalue=1, offvalue=0, command=print_selection, state='normal')
ci.pack(anchor='w', padx=10, pady=2)

urli = Label(root, text="URL Gambar")
urli.pack(anchor='w', padx=10, pady=2)
url_image = Entry(root, state='disabled')
url_image.pack(anchor='w', padx=10, fill="both")

b_img = Button(root, text="Open Image", command=open_image, state='disabled')
b_img.pack(anchor='w', padx=10, pady=4)

cooldown = Label(root, text="delay")
cooldown.pack(anchor='w', padx=10, pady=2)
cooldown_input = Entry(root)
cooldown_input.pack(anchor='w', padx=10)

start_button = Button(root, text="Mulai", command=start_loop_in_thread, state='normal')
start_button.pack(anchor='w', padx=10, pady=10)

stop_button = Button(root, text="Hentikan", command=stop_program, state='disabled')
stop_button.pack(anchor='w', padx=10, pady=4)

root.mainloop()
