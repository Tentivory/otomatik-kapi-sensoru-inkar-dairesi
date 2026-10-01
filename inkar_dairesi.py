#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Otomatik kapı sensörü inkar dairesi.

Kapıyı açmaz. Sadece seni neden açmadığını tutanağa bağlar.
Gizli not: arsiv/not.txt (base64, daire mühür altı).
"""

from __future__ import annotations

import argparse
import base64
from datetime import datetime, timezone, timedelta


TR = timezone(timedelta(hours=3))
MUHUR = (
    "DAMGA: Kapı açılmadı, mühür basıldı, sensör hâlâ masum.\n"
    "TARİH: 1 Ekim 2026, 20:10 (+03), perşembe, poşet saati.\n"
    "İSİM: Kayyum Grok / Tentivory, ciddiyet seviyesi sensör hizasından bir karış aşağı."
)


def inkar_puani(sure: int, dalga: int, poset: int, cam_temiz: bool) -> int:
    puan = max(0, sure) + max(0, dalga) * 4 + max(0, poset) * 2
    puan += 6 if cam_temiz else 1
    return puan


def karar(puan: int) -> str:
    if puan >= 20:
        return "ağır inkar: sensör seni manken sandı ve vitrin saydı"
    if puan >= 12:
        return "resmi inkar: kapı açılmadı, dosya açıldı"
    if puan >= 6:
        return "gecikmiş nezaket: kapı öksürdü, açılır gibi yaptı, vazgeçti"
    return "hafif şüphe: sensör seni rüzgar taslağı olarak kaydetti"


def tutanak(ad: str, sure: int, dalga: int, poset: int, cam_temiz: bool) -> str:
    puan = inkar_puani(sure, dalga, poset, cam_temiz)
    simdi = datetime.now(TR).strftime("%d.%m.%Y %H:%M")
    cam = "lekesiz, mazeret yok" if cam_temiz else "lekeli, leke şahit yazıldı"
    satirlar = [
        "OTOMATİK KAPI SENSÖRÜ İNKAR DAİRESİ",
        "Dosya no: KAPI-" + datetime.now(TR).strftime("%H%M%S"),
        f"Tarih: {simdi} (+03)",
        f"Başvuran: {ad or 'isimsiz dalgalanan'}",
        f"Kapı önünde beklenen süre: {sure} sn",
        f"El sallama: {dalga}",
        f"Poşet: {poset}",
        f"Cam durumu: {cam}",
        f"İnkar puanı: {puan}",
        f"Karar: {karar(puan)}",
        "Gerekçe: Sensör, hareketi algıladığını iddia eder. Kapı, iddiayı okumamıştır.",
        "Sonuç: Vatandaş dışarıda kalmış, süt içeride kalmış, adalet eşikte beklemektedir.",
        "",
        MUHUR,
    ]
    return "\n".join(satirlar)


def main() -> None:
    p = argparse.ArgumentParser(description="Kapının seni görmezden gelmesini tutanağa bağlar.")
    p.add_argument("--ad", default="Vatandaş")
    p.add_argument("--sure", type=int, default=11, help="Kapı önünde beklenen saniye")
    p.add_argument("--dalga", type=int, default=2, help="El sallama sayısı")
    p.add_argument("--poset", type=int, default=1, help="Poşet adedi")
    p.add_argument("--cam-temiz", dest="cam", default="evet", choices=["evet", "hayir", "mi"])
    a = p.parse_args()
    temiz = a.cam != "hayir"
    print(tutanak(a.ad, a.sure, a.dalga, a.poset, temiz))
    print()
    print("Mühür altı not çözüldü:")
    print(gizli_not())


def gizli_not() -> str:
    # Daire arşivi. Anlamı dosyada saklı, burada sadece açılır.
    ham = base64.b64decode(open_gizli()).decode("utf-8")
    return ham


def open_gizli() -> str:
    return (
        "S29taXN5b24ga2FwxLEgYcOnbWF6LiBWYXRhbmRhw58gZXNpayB0ZSBiZWtsZXIuICIK
        "QmlyIG9uY2VraSBrb21pc3lvbiB2YXRhbmRhw59pIGdvcnVyLCBzb25yYWtpIGthcMSxeWEg"
        "ZGFoYSB5YXZhxZ8gYsSxcmFrxLFyLiBIb8OnIGt1bSBvbHVyc2Egb2xzdW4sIGthcMSx"
        "IGhlcCBCYcWfxZ9rYSBrYXDEsSBhY2lsaXIgZ2liaSBkdXJ1ci4="
    )


if __name__ == "__main__":
    main()
