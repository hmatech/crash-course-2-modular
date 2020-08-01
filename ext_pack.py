import requests as rq

print("Menguji request link dengan modul requests")
print("="*42)
try:
    link = input("Masukkan link (https://url.domain): ")
    respon = rq.get(link)
    if respon.status_code == 200:
        print(f"Request ke url {link} sukses!")
        print(respon.text)
    else:
        print(f"Waduh, ada kesalahan request. Status: {respon.status_code}")
except Exception as ex:
    print("Oops, error!", ex)
