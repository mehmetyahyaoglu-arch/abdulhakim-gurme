# Abdülhakim Gurme — Web Sitesi ve Bayilik Otomasyonu

Karaman merkezli **Abdülhakim Gurme** markası için geliştirilmiş modern, koyu/altın lezzet temalı responsive kurumsal web sitesi ve otomatik bayilik başvuru yönetim sistemi.

---

## 🌟 Öne Çıkan Özellikler

- **Kurumsal İmalatçı Vurgusu:** Çiğköfte & Baklava bizzat imalatçı gücü, özel kahve menüsü sunumu.
- **Bayilik Başvuru Formu:** Potansiyel adaylardan isim, telefon, şehir, bütçe ve mesaj toplayan dinamik form.
- **Anlık Telegram Bildirimi:** Her başvuruda yöneticinin Telegram hesabına otomatik formatlı bildirim mesajı.
- **Gelişmiş JSON Veritabanı:** Gelen tüm başvuruların `data/basvurular.json` dosyasında tarih ve durum bilgisiyle arşivlenmesi.
- **Responsive Tasarım:** Mobil, tablet ve masaüstü cihazlarla %100 uyumlu lüks arayüz.

---

## 🚀 Çalıştırma Talimatları

### 1. Bağımlılıkları Yükleyin
```bash
pip install -r requirements.txt
```

### 2. Ortam Değişkenlerini Tanımlayın (İsteğe Bağlı - Telegram Bildirimleri İçin)
`.env` dosyası oluşturup aşağıdaki bilgileri ekleyin:
```env
TELEGRAM_BOT_TOKEN="BOT_TOKENINIZ"
TELEGRAM_CHAT_ID="CHAT_IDNIZ"
```

### 3. Sunucuyu Başlatın
```bash
python -m uvicorn src.main:app --reload --port 8000
```
Tarayıcınızda `http://localhost:8000` adresine giderek siteyi görüntüleyebilirsiniz.
