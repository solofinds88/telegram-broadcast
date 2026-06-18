import requests

TOKEN = "8571405082:AAHmlj7LhGKb20GnuUYIV31G81pWz_a969Q"
CHAT_ID = "-5330139068"

caption = """
*KUE GUNTING MEDAN*
*⭐ Hanya 1 di KPS!! ⭐*
Renyah, Gurih, dan Rasanya Mantap!

*Cemilan Legendaris dengan Rasa yang Tak Terlupakan*
✅ Dibuat dari bahan pilihan
✅ Tanpa pengawet
✅ Rasa khas Medan autentik

Sekali Gigit, Langsung Ketagihan!

✂️MENU KUE GUNTING✂️

Jenis kue : Hepia, Uyen, Pokpia Goreng/Kukus, Bakwan, (Kue Lobak/Chai Thao Kue Ready 1 Minggu Sekali)

✂️Mix Tanpa Hepia & Kue Lobak/Chai Thao Kue 12.000
✂️Mix/Full Hepia 14.000
✂️Mix/Full Kue Lobak/Chai Thao Kue 14.000
✂️Mix dengan Hepia & Kue Lobak/Chai Thao Kue 15.000
✂️Kue Gunting Yummy Special 18.000👍🏻

Untuk menu lengkapnya bisa join GRUP RESTO kami ✨

Tele Admin : @restoyummykps
Link Grup : https://t.me/restoYummy

🕚Open 11.00 Siang - 22.30 Malam (last order)"""

photo_url = "https://i.postimg.cc/1tMq8hff/C420036D-A055-4C2C-B6E6-49D2A73DD1EC.jpg"

requests.post(
    f"https://api.telegram.org/bot{TOKEN}/sendPhoto",
    data={
        "chat_id": CHAT_ID,
        "photo": photo_url,
        "caption": caption
    }
)
