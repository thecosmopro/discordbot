import random

def sifre_olusturucu(parola_uzunlugu ):
    karakterler = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    parola = ""
    for _ in range(parola_uzunlugu):
        rastgele_karakter = random.choice(karakterler)
        parola += rastgele_karakter

    return parola

def double_letter (str):
    result = ''
    for letter in str:
        result += letter * 2
    return result

def sayi_tahmin():
    x = random.randint(1,10)
