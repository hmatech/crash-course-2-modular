from bangun_datar.lingkaran import luas_lingk
from bangun_datar.persegi import luas_psg
from bangun_datar.persegipanjang import luas_psgp

sisi = 20
print(f"Luas persegi dengan sisi {sisi} adalah {luas_psg(sisi)}")

panjang = 20
lebar = 35
print(f"Luas persegi panjang dengan panjang {panjang} dan lebar {lebar} adalah {luas_psgp(panjang, lebar)}")

ruas = 10
print(f"Luas lingkaran dengan ruas {ruas} adalah {luas_lingk(ruas)}")
