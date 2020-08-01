"""
Program menghitung luas segitiga
l = a*t / 2
"""

print("Menghitung luas segitiga dengan fungsi luas_sgt")
print("="*20)


def luas_sgt(alas, tinggi):
    luas = alas * tinggi / 2
    return luas


try:
    a = int(input("Masukkan alas: "))
    t = int(input("Masukkan tinggi: "))
    print(f"luas segitiga dengan alas {a} dan tinggi {t} adalah {luas_sgt(a, t)}")
except ValueError:
    print("Harap masukkan angka!")
