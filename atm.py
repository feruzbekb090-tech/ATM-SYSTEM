from account import Account, pin_togrimi, karta_togrimi
from transaction import Transaction


class ATM:
    """Bankomatning asosiy faoliyati."""

    def __init__(self, nomi):
        self.__nomi = nomi
        self.__hisoblar = []
        self.__joriy_hisob = None
        self.__urinishlar = 0

    def get_nomi(self):
        return self.__nomi

    def __summa_kiritish(self, matn):
        """Foydalanuvchidan son oladi, noto'g'ri bo'lsa xatolik ko'taradi."""
        try:
            return float(input(matn))
        except ValueError:
            raise ValueError("Summa faqat son bo'lishi kerak!")

    # ---------- asosiy metodlar ----------
    def hisobni_topish(self, karta_raqami):
        for hisob in self.__hisoblar:
            if hisob.get_karta_raqami() == karta_raqami:
                return hisob
        return None

    def hisob_yaratish(self):
        print("\n--- Yangi hisob yaratish ---")
        egasi = input("Ism familiyangiz: ").strip()
        if egasi == "":
            print("Xatolik: ism bo'sh bo'lishi mumkin emas!")
            return

        karta = input("16 xonali karta raqamingiz: ").strip().replace(" ", "")
        if not karta_togrimi(karta):
            print("Xatolik: karta raqami 16 xonali raqam bo'lishi kerak!")
            return
        if self.hisobni_topish(karta) is not None:
            print("Xatolik: bu karta raqami allaqachon ro'yxatdan o'tgan!")
            return

        pin = input("4 xonali PIN-kod o'rnating: ").strip()
        if not pin_togrimi(pin):
            print("Xatolik: PIN-kod 4 xonali raqam bo'lishi kerak!")
            return

        hisob_id = len(self.__hisoblar) + 1
        self.__hisoblar.append(Account(hisob_id, egasi, karta, pin))

        print("Hisob muvaffaqiyatli yaratildi!")
        print("Hisob ID:", hisob_id)
        print("Karta raqami:", karta)

    def tizimga_kirish(self):
        print("\n--- Tizimga kirish ---")
        karta = input("Karta raqami: ").strip()
        hisob = self.hisobni_topish(karta)
        if hisob is None:
            print("Xatolik: bunday karta raqami topilmadi!")
            return False

        if hisob.bloklanganmi():
            print(
                "Karta vaqtincha bloklangan. Yana",
                hisob.qolgan_soniya(),
                "soniyadan keyin urinib ko'ring.",
            )
            return False

        self.__urinishlar = 0
        while self.__urinishlar < 3:
            pin = input("PIN-kod: ").strip()
            if hisob.pin_tekshirish(pin):
                self.__joriy_hisob = hisob
                self.__urinishlar = 0
                print("Xush kelibsiz,", hisob.get_egasi() + "!")
                return True
            self.__urinishlar += 1
            qolgan = 3 - self.__urinishlar
            if qolgan > 0:
                print("Noto'g'ri PIN-kod! Qolgan urinishlar:", qolgan)

        hisob.bloklash()
        self.__urinishlar = 0
        print("3 marta noto'g'ri PIN kiritildi. Karta vaqtincha bloklandi!")
        return False

    def tizimdan_chiqish(self):
        self.__joriy_hisob = None
        print("Tizimdan xavfsiz chiqildi.")

    def menu(self):
        """Foydalanuvchi menyusi (tizimga kirgandan keyin)."""
        while self.__joriy_hisob is not None:
            print("\n=== User Menu ===")
            print("1. Balansni tekshirish")
            print("2. Pul kiritish (Deposit)")
            print("3. Pul yechish (Withdraw)")
            print("4. Tranzaksiyalar tarixini ko'rish")
            print("5. PIN-kodni o'zgartirish")
            print("6. Tizimdan chiqish")
            tanlov = input("Tanlang: ").strip()

            try:
                if tanlov == "1":
                    print("Balans:", self.__joriy_hisob.balansni_korish(), "so'm")

                elif tanlov == "2":
                    summa = self.__summa_kiritish("Kiritiladigan summa: ")
                    self.__joriy_hisob.pul_qoshish(summa)
                    print("Pul muvaffaqiyatli kiritildi.")

                elif tanlov == "3":
                    summa = self.__summa_kiritish("Yechiladigan summa: ")
                    self.__joriy_hisob.pul_yechish(summa)
                    print("Pul muvaffaqiyatli yechildi.")

                elif tanlov == "4":
                    self.__tarixni_korsatish()

                elif tanlov == "5":
                    eski = input("Eski PIN-kod: ").strip()
                    yangi = input("Yangi PIN-kod (4 xonali): ").strip()
                    self.__joriy_hisob.pin_ozgartirish(eski, yangi)
                    print("PIN-kod muvaffaqiyatli o'zgartirildi.")

                elif tanlov == "6":
                    self.tizimdan_chiqish()

                else:
                    print("Xatolik: 1 dan 6 gacha son kiriting!")
            except ValueError as xato:
                print("Xatolik:", xato)

    def __tarixni_korsatish(self):
        print("\n1. Barcha tranzaksiyalar")
        print("2. Faqat Deposit")
        print("3. Faqat Withdraw")
        tanlov = input("Tanlang: ").strip()
        royxat = self.__joriy_hisob.get_tranzaksiyalar()
        # tranzaksiya_tarixi() metodini chaqirish uchun vaqtinchalik obyekt
        # ishlatmaymiz, shuning uchun royxat bo'sh bo'lmasa birinchi elementdan foydalanamiz
        if len(royxat) == 0:
            print("Tranzaksiyalar topilmadi.")
            return
        t = royxat[0]
        if tanlov == "1":
            t.tranzaksiya_tarixi(royxat)
        elif tanlov == "2":
            t.tranzaksiya_tarixi(royxat, "Deposit")
        elif tanlov == "3":
            t.tranzaksiya_tarixi(royxat, "Withdraw")
        else:
            print("Xatolik: 1 dan 3 gacha son kiriting!")
