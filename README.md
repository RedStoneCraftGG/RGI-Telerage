# RGI-Telerage
Alat untuk membanjiri pesan bot telegram penipu dari apk undangan atau website tarif bank

# Instalasi
Download file yang ingin anda gunakan atau clone/download repository ini. Jangan lupa untuk menginstall Python3 jika belum punya

Pastikan anda menginstall Requests di python dengan cara menuliskan kode dibawah ini:

**Untuk Windows:**
```
py -m pip install requests
py -m pip install pillow
```

**Untuk Linux:**
```
pip install requests
pip install pillow
```

# Cara menggunakan aplikasi
Saat menjalankan aplikasinya, terdapat input text yang harus diisi seperti ID chat, Token, Pesan, dan lainnya seperti gambar dibawah ini

![image](https://github.com/RedStoneCraftGG/RGI-Scammer-Revenge/assets/66346080/535ff7ec-99c7-4590-97cc-999d66a57f67)

setelah memasukan informasi yang dibutuhkan, maka aplikasi akan berjalan dan mulai membanjiri pesan bot telegram si penipu. Jalankan sebanyak-banyaknya untuk membanjiri lebih banyak lagi!

Selain mengisi dengan user input, Aplikasi ini bisa dijalankan dengan 1 command line saja. Contohnya seperti dibawah ini:

```
py app.py -id 1234567890 -t 1234567890:abcdefghijklmnopqrstuvwxyz -m "Mampus Lu" -i https://example.com/image.png -d 1
```
Atau
```
python3 app.py -id 1234567890 -t 1234567890:abcdefghijklmnopqrstuvwxyz -m "Mampus Lu" -i https://example.com/image.png -d 1
```
Dengan keterangan:

-id --chatid (Chat ID Telegram)

-t --token (Token bot Telegram)

-m --message (Pesan)

-i --image (Gambar url. Kosongkan untuk menupload gambar bawaan)

-d --delay (Jeda mengirim pesan. Kosongkan untuk mengatur secara default: 10 detik)

-v --verbose (tampilkan verbose dan info)



**Selalu Waspada dan Gunakan Aplikasi Ini Dengan Penuh Tanggung Jawab!**
