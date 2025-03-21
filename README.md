# vuln-ping-api
 Komut enjeksiyonuna açık basit bir Flask API uygulaması

🔓 Zafiyetli Flask Uygulaması: Command Injection
Bu projede, kullanıcıdan alınan bir IP adresiyle ping işlemi yapan basit bir Flask uygulaması bulunmaktadır. Ancak, kullanıcı girdisi doğrudan sistem komutuna eklendiği için uygulama komut enjeksiyonu (Command Injection) zafiyetine sahiptir.

⚠️ Zafiyet Bilgisi
Zafiyet Türü: Command Injection
OWASP Kategorisi: A03:2021 - Injection
Vector String (CVSS v3.1): AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
CVSS Skoru: 9.8 (Critical)
🐍 Kullanım
Gereksinim:

nginx
Kopyala
Düzenle
pip install flask
Zafiyetli uygulamayı çalıştırmak için:

nginx
Kopyala
Düzenle
python app_vuln.py
Tarayıcıda test etmek için:

arduino
Kopyala
Düzenle
http://127.0.0.1:5000/ping?ip=127.0.0.1
Zafiyeti tetiklemek için:

bash
Kopyala
Düzenle
http://127.0.0.1:5000/ping?ip=127.0.0.1&dir
Güvenli versiyon:

nginx
Kopyala
Düzenle
python app_fixed.py
Bu sürümde kullanıcı girdisi doğrudan sistem komutuna verilmediği için zafiyet ortadan kaldırılmıştır.

## 🎬 Demo Video

Aşağıda bu zafiyetin istismar edildiği demo videosunu izleyebilirsiniz:

📹 [Demo Videosunu İzle / İndir](demo.mp4)


https://github.com/user-attachments/assets/2e5c7a0e-f95f-424f-bfc8-cd9844705398



