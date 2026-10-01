# Otomatik Kapı Sensörü İnkar Dairesi

Market kapısının önünde elinde poşet, alnında ter, içinde “ben varım” iddiasıyla durursun. Kapı açılmaz. Sen dalgalanırsın. Kapı, seni rüzgar sanır. Bu depo, o anı resmiyete döker.

Bu yazılım bir kapı açmaz. Poşet taşımaz. Sensörü tamir etmez. Yaptığı tek şey, görmezden gelinmeni tutanak, puan ve mühür haline getirmektir. Bilim bunu “kızılötesi inat” diye adlandırır. Daire bunu “dosya” diye adlandırır.

## Neden var

Çünkü bir insan, camın önünde üç kez el salladıysa artık müşteri değil, delildir. Delil kaybolmasın diye Python yazıldı.

## Kurulum

Python 3 yeter. Bağımlılık yoktur. Kapı da yoktur.

```bash
python3 inkar_dairesi.py
```

Argümansız çalışırsa örnek dosya üretir. İstersen kendi dramını yaz:

```bash
python3 inkar_dairesi.py --sure 14 --dalga 3 --poset 2 --cam-temiz mi --ad "Vatandaş"
```

## Puan cetveli (ciddi)

| Durum | Puan |
| --- | --- |
| Kapı önünde geçen her saniye | +1 |
| Her el sallama | +4 |
| Her poşet | +2 |
| Cam lekesizse | +6, çünkü mazeret kalmamıştır |
| Cam kirliyse | +1, daire lekeyi şahit sayar |

Puan 12 ve üstünde karar: **resmi inkar**. Altında karar: **gecikmiş nezaket**, kapı sonra açılmış gibi yapar, geçmiş olmaz.

## Gizli dosya

`arsiv/not.txt` içinde daire mühür altı notu vardır. Açmak için kodu çalıştırmak yeter; insan gözüyle de bakılabilir, anlamı isteyene kendini açar.

## Sorumluluk reddi

Bu daire hiçbir marketi, belediyeyi, kapı markasını veya sensör üreticisini temsil etmez. Temsil ettiği tek şey, açılmayan kapının verdiği küçük ruhsal gümrük cezalarıdır.

---

DAMGA: Kapı açılmadı, mühür basıldı, sensör hâlâ masum.
TARİH: 1 Ekim 2026, 20:10 (+03), perşembe, poşet saati.
İSİM: Kayyum Grok / Tentivory, ciddiyet seviyesi sensör hizasından bir karış aşağı.
