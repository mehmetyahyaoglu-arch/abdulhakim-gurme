import os
import logging
import requests
from typing import Dict, Any

logger = logging.getLogger(__name__)

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")

def telegram_bildirim_gonder(basvuru: Dict[str, Any]) -> bool:
    bot_token = TELEGRAM_BOT_TOKEN
    chat_id = TELEGRAM_CHAT_ID
    
    if not bot_token or not chat_id:
        logger.warning("Telegram Bot Token veya Chat ID tanımlı değil. Bildirim atlandı.")
        return False
        
    mesaj = (
        "<b>🚨 YENİ BAYİLİK BAŞVURUSU!</b>\n\n"
        f"<b>👤 Ad Soyad:</b> {basvuru.get('ad_soyad')}\n"
        f"<b>📞 Telefon:</b> {basvuru.get('telefon')}\n"
        f"<b>📍 İl / İlçe:</b> {basvuru.get('sehir')} / {basvuru.get('ilce')}\n"
        f"<b>💰 Düşünülen Bütçe:</b> {basvuru.get('butce')}\n"
        f"<b>📝 Mesaj:</b> {basvuru.get('mesaj', 'Bulunmuyor')}\n\n"
        f"<b>📅 Tarih:</b> {basvuru.get('tarih')}\n"
        "<i>🌐 Abdülhakim Gurme Web Otomasyonu</i>"
    )
    
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": mesaj,
        "parse_mode": "HTML"
    }
    
    try:
        response = requests.post(url, json=payload, timeout=10)
        if response.status_code == 200:
            logger.info("Telegram bildirimi başarıyla gönderildi.")
            return True
        else:
            logger.error(f"Telegram bildirim hatası: {response.text}")
            return False
    except Exception as e:
        logger.error(f"Telegram isteği sırasında istisna oluştu: {e}")
        return False
