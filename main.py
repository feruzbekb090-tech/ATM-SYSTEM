from atm import ATM


def main():
    atm = ATM("Bank ATM")

    while True:
        print("\n=== ATM System ===")
        print("1. Yangi hisob yaratish")
        print("2. Tizimga kirish")
        print("3. Dasturni yakunlash")
        tanlov = input("Tanlang: ").strip()

        if tanlov == "1":
            atm.hisob_yaratish()
        elif tanlov == "2":
            if atm.tizimga_kirish():
                atm.menu()
        elif tanlov == "3":
            print("Xayr! Yana kutamiz.")
            break
        else:
            print("Xatolik: 1 dan 3 gacha son kiriting!")


main()
