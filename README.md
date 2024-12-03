Voice Assistant in Python

Voice Assistant ini adalah program Python yang dapat menerima perintah suara dari pengguna untuk melakukan beberapa tugas, seperti membuka YouTube atau mencari informasi di Wikipedia. Program ini menggunakan pustaka `speech_recognition`, `webbrowser`, `wikipedia`, dan `pyttsx3`.

---

Fitur

1. Mendengarkan Perintah Suara: 
   - Asisten mendengarkan input suara pengguna hingga 20 detik.
2. Perintah Tersedia:
   - Membuka YouTube: Dengan mengatakan "buka YouTube".
   - Mencari di Wikipedia: Dengan mengatakan "cari di Wikipedia [topik]".
3. Text-to-Speech (TTS):
   - Asisten akan memberikan respons suara menggunakan pustaka `pyttsx3`.
4. Penanganan Kesalahan:
   - Menangani kesalahan jika input suara tidak dikenali atau topik Wikipedia tidak ditemukan.

---

Prasyarat

Pastikan Python sudah terinstal di sistem Anda. Gunakan versi Python 3.6 atau lebih baru.

 Instalasi Pustaka yang Dibutuhkan
Jalankan perintah berikut untuk menginstal pustaka yang diperlukan:
```bash
pip install SpeechRecognition, wikipedia, pyttsx3.
