# ATM System - Bankomat boshqaruv tizimi

## Loyiha haqida

ATM System foydalanuvchilarga quyidagilarni taqdim etadi:

- bank hisobini yaratish;
- karta raqami va PIN-kod orqali tizimga kirish;
- balansni tekshirish;
- hisobga pul kiritish va hisobdan pul yechish;
- tranzaksiyalar tarixini ko'rish;
- PIN-kodni o'zgartirish;
- tizimdan xavfsiz chiqish.

Dastur ma'lumotlarni **xotirada (RAM)** saqlaydi. Dastur yopilgach barcha hisoblar va tranzaksiyalar o'chadi.

---

## Loyiha maqsadi

Loyiha davomida quyidagi bilimlar amaliyotda mustahkamlanadi:

- Class va Object yaratish
- Constructor (`__init__`) bilan ishlash
- Instance attributes va methods
- **Encapsulation** (private attributelar va getter metodlar)
- Bir nechta class o'rtasida bog'lanish (Object Composition)
- List orqali obyektlar kolleksiyasini boshqarish
- Exception handling yordamida xatolarni boshqarish
- Business logikani class metodlari orqali tashkil qilish
- Modular dasturlash (har bir class alohida faylda)

---

## Imkoniyatlar

### 1. Account Management (hisob boshqaruvi)

- Yangi bank hisobini yaratish
- Hisob egasining ismini saqlash
- Har bir hisobga unikal ID berish
- Har bir hisobga unikal 16 xonali karta raqami yaratish
- 4 xonali PIN-kod o'rnatish

### 2. Authentication (autentifikatsiya)

- Karta raqami orqali hisobni aniqlash
- PIN-kod orqali tizimga kirish
- Noto'g'ri PIN uchun xabar va qolgan urinishlar sonini ko'rsatish
- Urinishlar sonini 3 ta bilan cheklash

### 3. Banking Operations (bank amallari)

- Balansni tekshirish
- Hisobga pul kiritish (Deposit)
- Hisobdan pul yechish (Withdraw)
- Yechishdan oldin mablag' yetarliligini tekshirish

### 4. Transaction History (tranzaksiyalar tarixi)

- Har bir Deposit va Withdraw avtomatik saqlanadi
- Tarixni 3 xil ko'rish mumkin: **hammasi**, **faqat Deposit**, **faqat Withdraw**
- Har bir tranzaksiyada ID, tur, summa va sana ko'rsatiladi

### 5. Security (xavfsizlik)

- PIN-kod tekshiruvi
- Noto'g'ri urinishlarni nazorat qilish
- 3 marta xato PIN kiritilsa, kartani vaqtincha bloklash
- Mablag' yetarli bo'lmasa yechishga ruxsat bermaslik
- PIN-kodni o'zgartirishda eski PIN-kodni so'rash
- Tizimdan chiqilganda sessiyani yakunlash

---

## Ishlatilgan texnologiyalar

| Texnologiya                   | Qayerda ishlatilgan                                     |
| ----------------------------- | ------------------------------------------------------- |
| Python 3                      | Butun loyiha                                            |
| Classes & Objects             | `Account`, `ATM`, `Transaction`                         |
| Constructor (`__init__`)      | Barcha classlarda                                       |
| Instance attributes / methods | Barcha classlarda                                       |
| Encapsulation                 | Private attributelar (`__balans`, `__pin` va boshqalar) |
| Lists                         | `hisoblar`, `tranzaksiyalar`                            |
| Conditional statements        | `if / elif / else`                                      |
| Loops                         | `while`, `for`                                          |
| Exception Handling            | `try / except ValueError`                               |
| `random` moduli               | Karta raqamini yaratish                                 |
| `datetime` moduli             | Tranzaksiya sanasi va karta bloklanish vaqti            |

---

## Loyiha tuzilishi

```
ATM_Project/
│
├── main.py          # Dasturni ishga tushirish va asosiy menu
├── account.py       # Bank hisobini boshqarish
├── atm.py           # Bankomat faoliyatini boshqarish
├── transaction.py   # Tranzaksiyalarni boshqarish
│
└── README.md        # Loyiha hujjati
```

| Fayl             | Vazifasi                                                                             |
| ---------------- | ------------------------------------------------------------------------------------ |
| `main.py`        | Dasturni ishga tushiradi, asosiy menyuni (Yangi hisob / Kirish / Chiqish) ko'rsatadi |
| `account.py`     | `Account` classi, PIN tekshirish funksiyasi va bloklash logikasi                     |
| `atm.py`         | `ATM` classi: hisob yaratish, autentifikatsiya, foydalanuvchi menyusi                |
| `transaction.py` | `Transaction` classi va tarixni chiqarish                                            |

---

## Classlar tavsifi

### 1. `Transaction` class (`transaction.py`)

**Vazifasi:** hisobda bajarilgan bitta operatsiyani (Deposit yoki Withdraw) saqlash.

**Attributes:**

| Attribute | Type     | Tavsif                             |
| --------- | -------- | ---------------------------------- |
| `__id`    | int      | Unikal tranzaksiya ID raqami       |
| `__turi`  | str      | `"Deposit"` yoki `"Withdraw"`      |
| `__summa` | float    | Tranzaksiya summasi                |
| `__sana`  | datetime | Tranzaksiya amalga oshirilgan vaqt |

**Class-level attribute:**

| Nomi         | Tavsif                                                                                                                 |
| ------------ | ---------------------------------------------------------------------------------------------------------------------- |
| `keyingi_id` | Barcha tranzaksiyalar uchun umumiy hisoblagich. Har yangi tranzaksiyada 1 ga oshadi, shu sababli ID lar takrorlanmaydi |

**Methods:**

| Method                                                | Tavsif                                                                                                                                                                                 |
| ----------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `get_id()`, `get_turi()`, `get_summa()`, `get_sana()` | Private attributelarni o'qish uchun getterlar                                                                                                                                          |
| `malumot()`                                           | Tranzaksiya haqida bitta qatorli matn qaytaradi. Masalan: `#1 \| Deposit \| 50000.0 so'm \| 2025-01-15 14:30:05`                                                                       |
| `tranzaksiya_tarixi(royxat, turi=None)`               | Berilgan tranzaksiyalar ro'yxatini chiqaradi. `turi=None` bo'lsa hammasi, `"Deposit"` yoki `"Withdraw"` bo'lsa faqat shu tur. Hech narsa topilmasa "Tranzaksiyalar topilmadi." chiqadi |

---

### 2. `Account` class (`account.py`)

**Vazifasi:** foydalanuvchining bank hisobi ma'lumotlarini saqlash va bank amallarini bajarish.

**Attributes:**

| Attribute          | Type            | Tavsif                                     |
| ------------------ | --------------- | ------------------------------------------ |
| `__id`             | int             | Hisob ID raqami                            |
| `__egasi`          | str             | Hisob egasining ismi                       |
| `__karta_raqami`   | str             | 16 xonali karta raqami                     |
| `__pin`            | str             | 4 xonali PIN-kod                           |
| `__balans`         | float           | Hisobdagi mablag' (boshlang'ich qiymati 0) |
| `__tranzaksiyalar` | list            | `Transaction` obyektlari ro'yxati          |
| `__bloklangan`     | bool            | Karta bloklangan yoki yo'qligi             |
| `__blok_vaqti`     | datetime / None | Karta bloklangan vaqt                      |

**Fayl darajasidagi elementlar:**

| Nomi               | Tavsif                                                                     |
| ------------------ | -------------------------------------------------------------------------- |
| `BLOK_SONIYA = 60` | Karta bloklanish muddati (soniyada). Xohlasangiz shu qiymatni o'zgartiring |
| `pin_togrimi(pin)` | PIN 4 xonali va faqat raqamlardan iborat bo'lsa `True` qaytaradi           |

**Methods:**

| Method                                                                  | Tavsif                                                                                                                        |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `get_id()`, `get_egasi()`, `get_karta_raqami()`, `get_tranzaksiyalar()` | Getterlar                                                                                                                     |
| `balansni_korish()`                                                     | Hisobdagi mablag'ni qaytaradi                                                                                                 |
| `pul_qoshish(summa)`                                                    | Summa musbat bo'lsa balansga qo'shadi va `Deposit` tranzaksiyasini yozadi. Aks holda `ValueError`                             |
| `pul_yechish(summa)`                                                    | Summa musbat va balansdan oshmasa balansdan ayiradi va `Withdraw` tranzaksiyasini yozadi. Aks holda `ValueError`              |
| `pin_tekshirish(pin)`                                                   | Kiritilgan PIN to'g'ri bo'lsa `True` qaytaradi                                                                                |
| `pin_ozgartirish(eski_pin, yangi_pin)`                                  | Eski PIN to'g'ri va yangi PIN 4 xonali bo'lsa PIN ni almashtiradi. Aks holda `ValueError`                                     |
| `bloklash()`                                                            | Kartani bloklaydi va bloklangan vaqtni eslab qoladi                                                                           |
| `bloklanganmi()`                                                        | Karta hozir bloklanganmi yoki yo'qligini qaytaradi. Agar blok muddati (`BLOK_SONIYA`) o'tgan bo'lsa, kartani avtomatik ochadi |
| `qolgan_soniya()`                                                       | Blok tugashiga necha soniya qolganini                                                                                         |
