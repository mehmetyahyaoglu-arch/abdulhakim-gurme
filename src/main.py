import os
from fastapi import FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional

from src.db_manager import kayit_ekle, tum_basvurular
from src.telegram_notifier import telegram_bildirim_gonder

app = FastAPI(
    title="Abdülhakim Gurme - Web & Bayilik Otomasyonu",
    description="Çiğköfte, Baklava ve Kahve Lezzet Markası Bayilik Otomasyonu API",
    version="1.0.0"
)

# Static files (public/) dizini montajı
PUBLIC_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "public")
os.makedirs(PUBLIC_DIR, exist_ok=True)
app.mount("/static", StaticFiles(directory=PUBLIC_DIR), name="static")

class BayilikBasvuruModel(BaseModel):
    ad_soyad: str = Field(..., min_length=2, description="Başvuru sahibinin adı soyadı")
    telefon: str = Field(..., min_length=10, description="İletişim telefon numarası")
    sehir: str = Field(..., min_length=2, description="Bayilik kurulmak istenen il")
    ilce: Optional[str] = Field("", description="İlçe bilgisi")
    butce: str = Field(..., description="Yatırım bütçe aralığı")
    mesaj: Optional[str] = Field("", description="Ek not veya mesaj")

@app.get("/health")
async def health():
    return {"status": "ok", "service": "abdulhakim-gurme-web"}

@app.get("/", response_class=HTMLResponse)
async def home():
    index_path = os.path.join(PUBLIC_DIR, "index.html")
    if os.path.exists(index_path):
        with open(index_path, "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>Abdülhakim Gurme Web Sitesi Yükleniyor...</h1>"

@app.post("/api/bayilik-basvuru")
async def basvuru_yap(basvuru: BayilikBasvuruModel):
    try:
        data = basvuru.dict()
        kayitli_basvuru = kayit_ekle(data)
        
        # Telegram bildirimi gönderimi
        telegram_bildirim_gonder(kayitli_basvuru)
        
        return JSONResponse(
            status_code=200,
            content={
                "success": True,
                "message": "Bayilik başvurunuz başarıyla alındı! Ekibimiz en kısa sürede sizinle iletişime geçecektir.",
                "data_id": kayitli_basvuru.get("id")
            }
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Başvuru kaydedilirken hata oluştu: {str(e)}")

@app.get("/api/admin/basvurular")
async def basvurulari_listele():
    return {"success": True, "basvurular": tum_basvurular()}
