#  猜數字遊戲
import random
def guess_number_game():
    # 產生一個1到100之間的隨機數字
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("歡迎來到猜數字遊戲！我已經選好了一個1到100之間的數字。")
    while True:
        try:
            # 提示玩家輸入猜測的數字
            guess = int(input("請輸入你的猜測（1-100）："))
            attempts += 1
            if guess < 1 or guess > 100:
                print("請輸入一個介於1到100之間的數字。")
                continue
            if guess < number_to_guess:
                print("太小了！再試一次。")
            elif guess > number_to_guess:
                print("太大了！再試一次。")
            else:
                print(f"恭喜你！你猜對了，答案就是 {number_to_guess}。你總共猜了 {attempts} 次。")
                break
        except ValueError:
            print("請輸入一個有效的數字。")
if __name__ == "__main__":
    guess_number_game()