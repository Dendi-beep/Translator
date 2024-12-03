import speech_recognition as sr
import webbrowser
import wikipedia
import pyttsx3
from gtts import gTTS
import os


wikipedia.set_lang("id")


engine = pyttsx3.init()
engine.setProperty("rate", 150)  
engine.setProperty("volume", 1.0)  


def ngomong(teks):
    try:
        #tts = gTTS(text=teks, lang='id')
        #tts.save("ngomong.mp3")
        #os.system("start ngomong.mp3")
       
        engine.say(teks)
        engine.runAndWait()
    except Exception as e:
        print("Kesalahan saat memproses teks menjadi suara:", e)


def user():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Silahkan bicarakan sesuatu...")
        ngomong("Silahkan bicarakan sesuatu...")
        recognizer.adjust_for_ambient_noise(source, duration=1) 
        try:
            suara = recognizer.listen(source, timeout=10, phrase_time_limit=20)
            hasil = recognizer.recognize_google(suara, language="id-ID")
            print("Anda mengatakan:", hasil)
            return hasil.lower()
        except sr.UnknownValueError:
            print("Maaf, saya tidak bisa memahami apa yang Anda katakan.")
            ngomong("Maaf, saya tidak bisa memahami apa yang Anda katakan.")
        except sr.RequestError as e:
            print("Kesalahan pada layanan pengenalan suara:", e)
            ngomong("Kesalahan pada layanan pengenalan suara.")
        except Exception as e:
            print("Kesalahan lain:", e)
            ngomong("Terjadi kesalahan.")
        return ""


def bukayoutube():
    url = "https://youtu.be/_vw2TkUfgNs?si=M2KWICQqKUTZlSkX"
    webbrowser.open(url)
    ngomong("Membuka YouTube untuk Anda...")


def cariwikipedia(topik):
    try:
        hasil = wikipedia.summary(topik, sentences=2)
        ngomong(f"Berikut penjelasan tentang {topik}: {hasil}")
        print(f"Berikut penjelasan tentang {topik}: {hasil}")
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"Topik tidak spesifik: {e}")
        ngomong(f"Topik tidak spesifik. Harap berikan informasi tambahan.")
    except wikipedia.exceptions.PageError:
        print(f"Topik {topik} tidak ditemukan.")
        ngomong(f"Topik {topik} tidak ditemukan.")
    except Exception as e:
        print(f"Kesalahan saat mencari di Wikipedia: {e}")
        ngomong(f"Kesalahan saat mencari di Wikipedia.")

def facebook():
    url = "https://web.facebook.com/Varukhpasterhitam?locale=id_ID"
    webbrowser.open(url)
    ngomong("Membuka Facebook untuk Anda...")


def Mulai():
    print("Selamat datang di asisten Irpan")
    ngomong("Selamat datang di asisten Irpan")
    while True:
        p = user()
        if p:
            if "youtube" in p:
                bukayoutube()
            elif "wikipedia" in p:
                topik = p.replace("wikipedia", "").strip()
                if topik:
                    cariwikipedia(topik)
                else:
                    ngomong("Silahkan sebutkan topik yang ingin dicari.")
            elif "keluar" in p:
                ngomong("Terima kasih sudah menggunakan asisten saya. Sampai jumpa!")
                break
            else:
                ngomong("Maaf, saya tidak mengerti perintah Anda.")

if __name__ == "__main__":
    Mulai()
