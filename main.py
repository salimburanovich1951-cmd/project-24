
# 1. Davlatlar ro'yxati
def davlatlar():
    davlat = ["Uzbekistan", "Rossiya", "AQSH", "Angliya", "Turkiya"]
    print(davlat)
# 2. Ro'yxat uzunligi
    print("Uzunligi:", len(davlat))
# 3. Alifbo bo'yicha
    print("Tartiblangan:", sorted(davlat))
# 4. Teskari alifbo bo'yicha
    print("Teskari tartib:", sorted(davlat, reverse=True))
# 5. Asl ro'yxat
    print("Asl ro'yxat:", davlat)
# 6. Ro'yxatni orqadan chiqarish
    davlat.reverse()
    print("Orqadan:", davlat)
# 7. Sort metodi
    davlat.sort()
    print("Alifbo:", davlat)
    davlat.sort(reverse=True)
    print("Teskari alifbo:", davlat)
# 8. 120 dan 1200 gacha juft sonlar
def juft_sonlar():
    sonlar = list(range(120, 1201, 2))
    print(sonlar)
# 9. Sonlar yig'indisi
    print("Yig'indi:", sum(sonlar))
# 10. Eng katta va kichik son ayirmasi
    print("Ayirma:", max(sonlar) - min(sonlar))
# 11. Elementlar soni
    print("Elementlar soni:", len(sonlar))
# 12. Boshidan, o'rtasidan va oxiridan 20 ta
    print("Boshidan:", sonlar[:20])
    orta = len(sonlar) // 2
    print("O'rtasidan:", sonlar[orta-10:orta+10])
    print("Oxiridan:", sonlar[-20:])
# 13. Taomlar ro'yxati
def taomlar():
    taomlar = ["Osh", "Manti", "Lag'mon", "Somsa", "Shashlik"]
# 14. Nonushta ro'yxatidan nusxa olish
    nonushta = taomlar.copy()
# 15. Faqat nonushtaga mos taomlar
    nonushta.clear()
    nonushta.extend(["Tuxum", "Non", "Pishloq"])
    nonushta.extend(["Sut", "Bo'tqa"])
# 16. Ikkala ro'yxatni chiqarish
    print("Taomlar:", taomlar)
    print("Nonushta:", nonushta)
davlatlar()
juft_sonlar()
taomlar()
