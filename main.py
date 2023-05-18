class Magaza: #Magaza sinifi olusturuldu
    def __init__(self, magaza_adi, satici_adi, satici_cinsi):
        # ozellikler tanimlaniyor
        self.__magaza_adi = magaza_adi
        self.__satis = {}
        self.__satici_adi = satici_adi
        self.__satici_cinsi = satici_cinsi
        self.satici_ekle(satici_adi, satici_cinsi) #her yeni magaza nesnesi olusturuldugunda ona satici eklemek icin metod cagirir

    def get_magaza_adi(self): #veriyi okumak icin get metodu
        return self.__magaza_adi

    def set_magaza_adi(self, magaza_adi): #deger atama yapabilmek icin set metodu
        self.__magaza_adi = magaza_adi

    def get_satici_adi(self): #veriyi okumak icin get metodu
        return self.__satici_adi

    def set_satici_adi(self, satici_adi): #deger atama yapabilmek icin set metodu
        self.__satici_adi = satici_adi

    def get_satici_cinsi(self): #veriyi okumak icin get metodu
        return self.__satici_cinsi

    def set_satici_cinsi(self, satici_cinsi): #deger atama yapabilmek icin set metodu
        self.__satici_cinsi = satici_cinsi

    def satici_ekle(self, satici_adi, satici_cinsi):
        # yeni bir satici eklemek icin satici_adi ve satici_cinsi parametre olarak alacak bir metod olusturuldu
        # satis isimli sozluk icinde bir ic sozluk olusturuldu
        # Bu ic sozluge saticinin adina bagli olacak sekilde satici_cinsi keyine sahip bir deger ve satislar keyine sahip bir liste yerlestirildi
        self.__satis[satici_adi] = {'satici_cinsi': satici_cinsi, 'satislar': []}

    def satis_ekle(self, satici_adi, miktar):
        # satis sozlugundeki saticinin satislarinin tutuldugu listeye o saticinin yeni satis miktarlarini ekler
        self.__satis[satici_adi]['satislar'].append(miktar)

    def get_satis(self): #sozlugu okumak icin get metodu
        return self.__satis

    @classmethod #magazadaki toplam satis ve saticilarin toplam satisini bulmak icin sinif metodu kullanilir
    def magaza_satis_tutar(cls, satislar):#satislar sozlugundeki satis miktarlarini toplamak icin yontem olusturuldu
        satici_listesi = [] #saticilari ve yaptiklari toplam satislari tutacak bir liste olusturuldu
        magaza_toplam = 0 #bir magazaki toplam satis fiyatlarini hesaplamak icin deger olusturuldu
        for magaza in satislar.values(): #satislar sozlugundeki her bir magaza icin for dongusu
            for satici, satislar in magaza.get_satis().items(): # magazanin sattigi her urun ve satis fiyatları icin for dongusu
                satici_toplam = sum(satislar['satislar']) #o saticinin sattigi urunlerin fiyati toplanir
                satici_bilgisi = satici + " : " + str(satici_toplam) #saticinin adi ve sattiklarinin fiyat toplami string olacak sekilde atanir
                satici_listesi.append(satici_bilgisi) #olusturulan string listeye eklenir
                magaza_toplam += satici_toplam #saticilarin satislarinin fiyatlari toplanıp magazanin yaptigi satis hesaplanir
            break  # yeni satıcılar eklenmeyeceği için burada donguden cikilir
        return satici_listesi, magaza_toplam

    def __str__(self): #magazalari, saticilari ve toplam satis tutarlarini ekrana yazdirmak icin metod olusturuldu
        satici, magaza = Magaza.magaza_satis_tutar({self.get_magaza_adi(): self}) #magaza_satis_tutar metodu cagrilip bulunan degerler ilgili degiskenlere atanir
        return (f"Magaza adi: {self.get_magaza_adi()}, Saticilar ve satis toplamlari : {satici}, Magaza toplami : {magaza}") #ekrana yazdirilir


def main(): #main metodu olusturulur
    satislar = {} #satislar sozlugu olusturulur
    while True: #kullanicidan ilgili degerler alinir, degerlerdeki bosluklar silinir.
       
        print("Lutfen giris yaparken Turkce harf KULLANMAYINIZ!")
        magaza_adi = input("Magaza Adi: ").strip()
        satici_adi = input("Satici Adi: ").strip()
        satici_cinsi = input("Satis Yapilan Urunun Cinsi: ").strip()
        tutar = float(input("Satis Tutari: "))

        if magaza_adi.strip() not in satislar: #magaza adi satislar sozlugunde yoksa yeni bir magaza olusturulur ve sozluge atanir
            satislar[magaza_adi] = Magaza(magaza_adi, satici_adi, satici_cinsi)
            satislar[magaza_adi].satis_ekle(satici_adi, tutar) #bu magazaya satici adi ve satilan urunun tutari kaydedilir
        else: #eger magaza satislar sozlugunde varsa
            if satici_adi not in satislar[magaza_adi].get_satis(): #satici adi o magazada var mı kontrol edilir
                satislar[magaza_adi].satici_ekle(satici_adi, satici_cinsi) #satici adi yoksa satici adi ve urun cinsi sozluge eklenir
            satislar[magaza_adi].satis_ekle(satici_adi, tutar) #satici adi ve tutar bilgisi sozluge eklenir

        devam = input("Yeni satis eklemek istiyor musunuz? (e/h): ") #kullaniciya yeni giris yapip yapmayacagi sorulur
        if devam.lower() == "h":
            break
        elif devam.lower() == "e":
            continue
        else:
            print("Gecersiz giris yaptiniz. Tekrar deneyiniz.")
            quit()
    for magaza in satislar.values(): #satislar listesindeki degerler __str__ metodu yardimiyla ekrana yazdirilir
        print(magaza)
main() #main cagrilir
