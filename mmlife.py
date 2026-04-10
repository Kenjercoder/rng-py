import random
import time

money = 0

def kerja():
    global money
    soal = random.randint(1, 10)
    soal2 = random.randint(1, 10)
    tanda = random.choice(["+", "-", "*"])

    if tanda == "+":
        hasil = soal + soal2
    elif tanda == "-":
        hasil = soal - soal2
    else:
        hasil = soal * soal2

    print(f"berapa hasil dari {soal} {tanda} {soal2}?")
    jawaban = input("jawaban: ")

    if jawaban == str(hasil):
        print("benar!")
        money += 10
        time.sleep(1)
        print("kamu mendapatkan 10 money!")
    else:
        print("salah!")
        money -= 5
        time.sleep(1)
        print("kamu kehilangan 5 money!")

def mesin_slot():
    global money
    bet = int(input("Masukkan jumlah taruhan : "))
    if money < bet:
        print("Maaf, uang tidak cukup!")
        return
    money -= bet
    symbols = ["🍒", "🍋", "🍊", "🍉", "⭐"]
    result = [random.choice(symbols) for _ in range(3)]

    print("Hasil mesin slot:", " ".join(result))

    if result[0] == result[1] == result[2]:
        print(f"Selamat! Kamu mendapatkan {bet * 10} money!")
        money += bet * 10
    else:
        print("Maaf, kamu kalah!")

def coin_flip():
    global money

    try:
        bet = int(input("pilih jumlah taruhan: "))
    except:
        print("Input harus angka!")
        return

    if bet > money:
        print("Uang tidak cukup!")
        return

    try:
        bit = int(input("pilih sisi (1=Heads, 2=Tails): "))
    except:
        print("Input harus angka!")
        return

    if bit not in [1, 2]:
        print("Pilihan tidak valid!")
        return

    bit_rng = random.randint(1, 2)

    if bit_rng == 1:
        hasil = "Heads"
    else:
        hasil = "Tails"

    print("Mengocok koin...")
    time.sleep(1)
    print("Hasil:", hasil)

    if bit == bit_rng:
        print(f"Menang! +{bet}")
        money += bet
    else:
        print(f"Kalah! -{bet}")
        money -= bet

def putar_roda():
    while True:
        print("\n1. mesin slot")
        print("2. coin flip")
        print("3. keluar")

        pilihan = input("Pilih: ")

        if pilihan == "1":
            mesin_slot()
        elif pilihan == "2":
            coin_flip()
        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak valid!")

def main2():
    global money
    while True:
        print(f"Money kamu: {money}")
        print("1. Kerja")
        print("2. akhiri permainan")

        pilihan = input("Pilih: ")

        if pilihan == "1":
            kerja()
        elif pilihan == "2":
            print("Terima kasih sudah bermain!")
            break
        else:
            print("Pilihan tidak valid!")

def main():
    global money
    money = 0

    print("Welcome to yolo life!")
    time.sleep(1)

    while True:
        print(f"\nMoney kamu: {money}")
        print("1. Kerja")
        print("2. akhiri permainan")
        print("3. Putar Roda")
        print("4. next")

        pilihan = input("Pilih: ")

        if pilihan == "1":
            kerja()
        elif pilihan == "2":
            print("Terima kasih sudah bermain!")
            break
        elif pilihan == "3":
            putar_roda()
        elif pilihan == "4":
            main2()
        else:
            print("Pilihan tidak valid!")
main()