while True:
    try:
        özellik= (input("özellik nedir:"))
        Sayısa_özellik=int(input("sayısal/yaşı özellik nedir:"))
        if(Sayısa_özellik==1554)or(özellik=="yazılımcı")or(özellik=="sakalı var")or (Sayısa_özellik==15)or (özellik=="  "):
            print("Tahmin ediliyor...")
            print("Bekleyin...")
            print("Tahmin edilen kisi ERAY ÇETİN mi?")
            print("Doğruysa (D),Yanlıssa (Y) basın")
            cevap=input()
            if(cevap=="D"):
                print("==============OYUN BİYMİŞTİR=============")
            elif(cevap=="Y"):
                continue
            elif(cevap=="Y"):
                print("Tahmin edemedim",("devam etmek için 'enter' tusuna basınız"))
                a=input()
                if(a=='enter'):
                    print("oyuna devma ediliyor")
                elif(özellik=="sarı saçlı")or(Sayısa_özellik==1533)or(özellik=="bisiklet sprou yapıyr")or(özellik=="listenin yedinci  sırasında yer alıyor"):
                    print("Tahmin ediliyor")
                    print("biraz zorlandım ama")
                    print("tahmin ettiğim kisi FERHAT ALTEKİN mi? evetse E hayırsa H tusuna basınız")
                    Cevap=input()
                    if (cevap=="E"):
                        print("Biraz zorladın beni")
                        print("Ama iyi oyundu bu...")
                        print("=============OYUN BİTMİŞTİR==============")
                    elif (cevap=="Y"):
                        print("çok zor sourlar bunlar ama","Devam etmek için'enter'tusuna basınız.")
                        lakap=input("karakterin lakabı varmı varsa nedir:")
                        cevapp=input()
                        if(cevapp==özellik=="uzun boylu") or (Sayısa_özellik==15) or (cevapp==özellik=="lakbı sümük"):
                            print("Tahmin ettiğim kisi BURAK ULUPINAR mı?","Evetse E Hayırsa H tusuna bas")
                            ceVap = input()
                            if (cevap=="E"):
                                print("==============OYUN BİYMİŞTİR===========")
                            elif (cevap=="H"):
                                print("oyuna devam etmek için'enter' tusuna basınız")
                                print("==============OYUN BİYMİŞTİR===========")#şimdilik ders çalısyotum oyüzden kapattım merak ettme devamı gelcek...
                                soru=input("tahmn ettiğiniz kişi listenin 18 in üstündem, yoksa altıda mı?","Altında ise A değilse Ü",sep="-")
                                Ccevap=input()
                                if(Ccevap=="A"):
                                    print()#SINIF LİSTESİNİN 18 SEKİZ ALTINI AL DİYE KOD YAZ
                                elif (Ccevap=="Ü"):
                                    print()#SINIF LİSTESİNİN ALTINDAKİLERİ AL DİYE ÖRN"""
        elif (özellik == "sarı saçlı") or (Sayısa_özellik == 1533) or (özellik == "bisiklet sprou yapıyr") or (özellik == "listenin yedinci  sırasında yer alıyot"):
            print("tahmin edilen kisi Ferhat altekin mi?\n","Evetse E tusuna basın,Hyırsa H tusna bas")
            ceevap=input()
            if(ceevap=="E"):
                print("==================OYUN BİTMİŞTİR===================")
                break
            elif(ceevap=="Y"):
                print("oyuna devam etmek ister misiniz? 'enter' tusuna basın")
        else:
            print("Aradığımız özellik yok...")
    except  ValueError or TypeError:
        print("sayısal yere sözel girme...")
        print("Tekrar dene lütfen...")
