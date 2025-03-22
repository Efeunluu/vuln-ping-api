# 🔓 Zafiyetli Flask API – Command Injection

Bu projede, kullanıcıdan alınan IP adresini ping’leyen basit bir Flask API uygulaması bulunmaktadır. Uygulamanın zafiyetli versiyonu, kullanıcı girdisini doğrudan sistem komutuna verdiği için **Command Injection** (komut enjeksiyonu) zafiyetine sahiptir.

---

## ⚠️ Zafiyet Bilgisi

- **Zafiyet Türü:** Command Injection  
- **OWASP Kategorisi:** A03:2021 - Injection  
- **Vector String (CVSS v3.1):** `AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`  
- **CVSS Skoru:** **9.8 / 10** (Critical)

---

## 🐍 Gereksinimler

```bash
pip install flask
🚨 Zafiyetli Uygulama: app_vuln.py
bash
Kopyala
Düzenle
python app_vuln.py
Tarayıcıda çalıştırmak için:

arduino
Kopyala
Düzenle
http://127.0.0.1:5000/ping?ip=127.0.0.1
Zafiyeti tetiklemek için (örnek payload):

bash
Kopyala
Düzenle
http://127.0.0.1:5000/ping?ip=127.0.0.1&dir
✅ Güvenli Versiyon: app_secure.py
Bu sürümde kullanıcıdan alınan IP adresi filtrelenmekte ve komut, doğrudan parametrelerle çalıştırılmaktadır. Böylece komut enjeksiyonu zafiyeti engellenmiştir.

bash
Kopyala
Düzenle
python app_secure.py


📁 Dosyalar
app_vuln.py → Zafiyetli versiyon
app_secure.py → Güvenli versiyon (fix uygulanmış)
demo.mp4 → İstismar videosu

## 🎬 Demo Video

Aşağıda bu zafiyetin istismar edildiği demo videosunu izleyebilirsiniz:




https://github.com/user-attachments/assets/ee31117c-d74a-4ded-be7d-e4bfa53688dc




