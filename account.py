from datetime import datetime
from transaction import Transaction

BLOK_SONIYA = 60  # karta bloklanish muddati (soniya)


def pin_togrimi(pin):
    """PIN 4 xonali va faqat raqamlardan iborat bo'lishi kerak."""
    return len(pin) == 4 and pin.isdigit()


class Account:
    """Foydalanuvchining bank hisobi."""

    def __init__(self, id, egasi, karta_raqami, pin, balans=0):
        self.__id = id
        self.__egasi = egasi
        self.__karta_raqami = karta_raqami
        self.__pin = pin
        self.__balans = balans
        self.__tranzaksiyalar = []
        self.__bloklangan = False
        self.__blok_vaqti = None

    # ---------- getter metodlar ----------
    def get_id(self):
        return self.__id

    def get_egasi(self):
        return self.__egasi

    def get_karta_raqami(self):
        return self.__karta_raqami

    def get_tranzaksiyalar(self):
        return self.__tranzaksiyalar

    # ---------- bank amallari ----------
    def balansni_korish(self):
        return self.__balans

    def pul_qoshish(self, summa):
        if summa <= 0:
            raise ValueError("Kiritiladigan summa musbat bo'lishi kerak!")
        self.__balans += summa
        self.__tranzaksiyalar.append(Transaction("Deposit", summa))

    def pul_yechish(self, summa):
        if summa <= 0:
            raise ValueError("Yechiladigan summa musbat bo'lishi kerak!")
        if summa > self.__balans:
            raise ValueError("Hisobda mablag' yetarli emas!")
        self.__balans -= summa
        self.__tranzaksiyalar.append(Transaction("Withdraw", summa))

    # ---------- PIN bilan ishlash ----------
    def pin_tekshirish(self, pin):
        return self.__pin == pin

    def pin_ozgartirish(self, eski_pin, yangi_pin):
        if not self.pin_tekshirish(eski_pin):
            raise ValueError("Eski PIN-kod noto'g'ri!")
        if not pin_togrimi(yangi_pin):
            raise ValueError("PIN-kod 4 xonali raqam bo'lishi kerak!")
        self.__pin = yangi_pin

    # ---------- bloklash ----------
    def bloklash(self):
        self.__bloklangan = True
        self.__blok_vaqti = datetime.now()

    def bloklanganmi(self):
        if self.__bloklangan:
            otgan = (datetime.now() - self.__blok_vaqti).total_seconds()
            if otgan >= BLOK_SONIYA:
                # Blok muddati tugadi
                self.__bloklangan = False
                self.__blok_vaqti = None
        return self.__bloklangan

    def qolgan_soniya(self):
        if self.__blok_vaqti is None:
            return 0
        otgan = (datetime.now() - self.__blok_vaqti).total_seconds()
        return int(BLOK_SONIYA - otgan) + 1
