from datetime import datetime


class Transaction:
    """Bitta tranzaksiya (Deposit yoki Withdraw)."""

    # Barcha tranzaksiyalar uchun umumiy hisoblagich (ID unikal bo'lishi uchun)
    keyingi_id = 1

    def __init__(self, turi, summa):
        self.__id = Transaction.keyingi_id
        Transaction.keyingi_id += 1
        self.__turi = turi
        self.__summa = summa
        self.__sana = datetime.now()

    def get_id(self):
        return self.__id

    def get_turi(self):
        return self.__turi

    def get_summa(self):
        return self.__summa

    def get_sana(self):
        return self.__sana

    def malumot(self):
        sana = self.__sana.strftime("%Y-%m-%d %H:%M:%S")
        return (
            "#"
            + str(self.__id)
            + " | "
            + self.__turi
            + " | "
            + str(self.__summa)
            + " so'm | "
            + sana
        )

    def tranzaksiya_tarixi(self, royxat, turi=None):
        """Berilgan tranzaksiyalar ro'yxatini chiqaradi.
        turi = None bo'lsa hammasi, 'Deposit' yoki 'Withdraw' bo'lsa faqat shu tur."""
        topildi = False
        for t in royxat:
            if turi is None or t.get_turi() == turi:
                print(t.malumot())
                topildi = True
        if not topildi:
            print("Tranzaksiyalar topilmadi.")
