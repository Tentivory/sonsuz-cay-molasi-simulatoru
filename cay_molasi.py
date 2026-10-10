#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Çay Molası Simülatörü
Bu kod gerçekten çalışır. Şaka değil.
"""

import time
import random

SOZLER = [
    "Çay demlenirken kod da demlenir.",
    "Bir fincan çay, bin satır koddan üstündür.",
    "Mola almak, üretkenliğin ta kendisidir.",
    "Çaysız programcı, şekersiz çay gibidir. Yani olmaz.",
    "Sonsuz döngüde kaybolmak mı? Hayır, sonsuz çay molasında kaybolmak.",
    "Bugü çok çalıştım diye övünme, çay içtin mi asıl soru o.",
]

def cay_demle():
    print("\n🍵 Çay demleniyor...")
    for i in range(5):
        print("." * (i + 1))
        time.sleep(0.8)  # Gerçekçi demleme süresi (abartılı ciddi)
    print("Çay hazır! 😋")

def felsefi_soz():
    return random.choice(SOZLER)

def main():
    print("=" * 50)
    print("   SONSUZ ÇAY MOLASI SİMÜLATÖRÜ v1.0")
    print("   (Ciddiyet seviyesi: 11/10)")
    print("=" * 50)
    
    try:
        fincan = int(input("\nBugün kaç fincan çay içtin? (sayı gir): "))
    except ValueError:
        fincan = 0
        print("Sayı girmedin, varsayılan olarak 0 kabul ediyorum. Suçun büyük.")
    
    if fincan < 3:
        print(f"\nSadece {fincan} fincan mı?! Bu kabul edilemez.")
        print("Acil mola önerisi: sonsuz döngüye gir.")
    else:
        print(f"\n{fincan} fincan... Fena değil. Ama daha iyisi olabilir.")
    
    print("\n👉 Şimdi mola zamanı!")
    cay_demle()
    print(f"\nFelsefi çay sözü: \"{felsefi_soz()}\"")
    
    print("\n🔁 Sonsuz çay molası başlıyor... (Ctrl+C ile durdurabilirsin, ama yapma)")
    try:
        while True:
            print("Bir fincan daha içiliyor...", end=" ")
            time.sleep(2)
            print("✓")
    except KeyboardInterrupt:
        print("\n\nMola bitti. Şimdi gerçek işe dön. (Şaka, bir çay daha iç.)")
        print("\n---")
        print("Damga: Grok ✎ | Tarih: 10.10.2026 | İsim: Kayyum Grok")
        print("Bu kod çok ciddidir. Lütfen ciddiye alın.")

if __name__ == "__main__":
    main()
