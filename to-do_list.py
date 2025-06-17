toDoList = []
def dosyadan_oku():
    try:
        with open("gorevler.txt", "r", encoding="utf-8") as dosya:
            for satir in dosya:
                temiz = satir.strip()
                if temiz != "" and temiz not in toDoList:
                    toDoList.append(temiz)
    except FileNotFoundError:
        pass
def dosyaya_kaydet():
    try:
        with open("gorevler.txt", "w", encoding="utf-8") as dosya:
            for gorev in toDoList:
                dosya.write(gorev + "\n")
    except:
        print("Dosyada yazim hatasi olustu!")
def gorev_yukle():
    gorev = input("Yapilacak gorevi giriniz: ").strip()
    if gorev == "":
        print("Bu alan bos birakilamaz! ")
    elif gorev in toDoList:
        print("Bu gorev zaten listede mevcut! ")
    else:
        toDoList.append(gorev)
        print("Gorev basarili bir sekilde eklendi! ")
        dosyaya_kaydet()
def gorev_goster():
    if not toDoList:
        print("Henuz gorev bulunmuyor.")
    else:
        print("Yapilacak Gorevler:")
        for i in range(len(toDoList)):
            print(f"{i+1}. {toDoList[i]}")
def gorev_sil():
    gorev_goster()
    try:
        sira = int(input("Silmek istediginiz gorev numarasini giriniz: "))
        if 1 <= sira <= len(toDoList):
            silinen = toDoList.pop(sira - 1)
            print(f"'{silinen}' basariyla silindi.")
            dosyaya_kaydet()
        else:
            print("Gecersiz gorev numarasi.")
    except ValueError:
        print("Lutfen gecerli bir sayi giriniz.")
def gorev_duzenle():
    if not toDoList:
        print("Gorev listesi bos! ")
        return
    gorev_goster()
    try:
        sira = int(input("Duzenlemek istediginiz gorev numarasini giriniz: "))
        if 1 <= sira <= len(toDoList):
            yeni_gorev = input("Yeni gorev metnini giriniz: ").strip()
            if yeni_gorev == "":
                print("Bos gorev eklenemez.")
            else:
                toDoList[sira - 1] = yeni_gorev
                print("Gorev basariyla guncellendi!")
                dosyaya_kaydet()
        else:
            print("Gecersiz gorev numarasi girdiniz! ")
    except ValueError:
        print("Lutfen gecerli bir deger girin. ")
def menu():
    while True:
        print("\n--- Gorev Listeleme Uygulamasina Hos Geldiniz! ---")
        print("1 - Gorev Ekle")
        print("2 - Gorevleri Listele")
        print("3 - Gorev Sil")
        print("4 - Gorev Düzenle")
        print("5 - Uygulamadan Cikis Yap")
        try:
            secim = int(input("Lutfen seciminizi yapin (1-5): "))
            if secim == 1:
                gorev_yukle()
            elif secim == 2:
                gorev_goster()
            elif secim == 3:
                gorev_sil()
            elif secim == 4:
                gorev_duzenle()
            elif secim == 5:
                print("Uygulamadan cikiliyor...")
                break
            else:
                print("Gecersiz islem! Lutfen 1 ile 5 arasinda bir sayi girin.")
        except ValueError:
            print("Lutfen sadece sayi giriniz.")
dosyadan_oku()
menu()
