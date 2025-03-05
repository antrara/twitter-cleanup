import tweepy
import os
from dotenv import load_dotenv
from datetime import datetime

def save_api_keys():
    api_key = input("Masukkan API Key: ")
    api_secret = input("Masukkan API Secret: ")
    access_token = input("Masukkan Access Token: ")
    access_secret = input("Masukkan Access Secret: ")
    
    with open(".env", "w") as f:
        f.write(f"API_KEY={api_key}\n")
        f.write(f"API_SECRET={api_secret}\n")
        f.write(f"ACCESS_TOKEN={access_token}\n")
        f.write(f"ACCESS_SECRET={access_secret}\n")
    print("✅ API Key berhasil disimpan!")

def logout():
    if os.path.exists(".env"):
        os.remove(".env")
    print("\n🔒 Anda telah logout. Jalankan ulang skrip untuk login kembali.")
    exit()

load_dotenv()
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")

def main():
    if not API_KEY or not API_SECRET or not ACCESS_TOKEN or not ACCESS_SECRET:
        print("🚀 Selamat datang! Anda perlu memasukkan API Key terlebih dahulu.")
        save_api_keys()
        load_dotenv()
    
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)
    
    def unfollow_users(api, jumlah):
        friends = api.get_friends(count=jumlah)
        for user in friends:
            api.destroy_friendship(user.id)
            print(f"✅ Unfollowed: {user.screen_name}")

    def unlike_all(api):
        liked_tweets = api.get_favorites(count=200)
        for tweet in liked_tweets:
            api.destroy_favorite(tweet.id)
            print(f"❌ Unliked: {tweet.id}")

    def unrepost_all(api):
        tweets = api.user_timeline(count=200)
        for tweet in tweets:
            if tweet.retweeted:
                api.unretweet(tweet.id)
                print(f"🔄 Unretweeted: {tweet.id}")

    def delete_comments(api):
        tweets = api.user_timeline(count=200)
        for tweet in tweets:
            if tweet.in_reply_to_status_id:
                api.destroy_status(tweet.id)
                print(f"🗑️ Deleted comment: {tweet.id}")

    def delete_tweets_since(api, start_date):
        tweets = api.user_timeline(count=200)
        for tweet in tweets:
            tweet_date = tweet.created_at
            if tweet_date >= start_date:
                api.destroy_status(tweet.id)
                print(f"🗑️ Deleted tweet from {tweet_date}: {tweet.id}")

    def delete_account_instructions():
        print("\n⚠️  Twitter tidak menyediakan API untuk menghapus akun secara otomatis.")
        print("Silakan hapus akun Anda secara manual di: https://twitter.com/settings/deactivate")
    
    while True:
        print("\n===== MENU =====")
        print("1. Unfollow Akun")
        print("2. Unlike Semua Tweet")
        print("3. Unretweet Semua")
        print("4. Hapus Komentar")
        print("5. Hapus Tweet sejak Tanggal")
        print("6. Logout")
        print("7. Keluar")
        pilihan = input("Pilih menu (1-7): ")
        
        if pilihan == "1":
            jumlah = int(input("Masukkan jumlah akun yang ingin di-unfollow: "))
            unfollow_users(api, jumlah)
        elif pilihan == "2":
            unlike_all(api)
        elif pilihan == "3":
            unrepost_all(api)
        elif pilihan == "4":
            delete_comments(api)
        elif pilihan == "5":
            tanggal_input = input("Masukkan tanggal (YYYY-MM-DD): ")
            start_date = datetime.strptime(tanggal_input, "%Y-%m-%d")
            delete_tweets_since(api, start_date)
        elif pilihan == "6":
            logout()
        elif pilihan == "7":
            print("🚀 Keluar dari program.")
            break
        else:
            print("❌ Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()
