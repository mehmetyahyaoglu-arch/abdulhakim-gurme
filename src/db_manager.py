import json
import os
from datetime import datetime
from typing import List, Dict, Any

DATA_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "basvurular.json")

def init_db():
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=2)

def kayit_ekle(basvuru_data: Dict[str, Any]) -> Dict[str, Any]:
    init_db()
    
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        try:
            basvurular = json.load(f)
        except json.JSONDecodeError:
            basvurular = []
            
    basvuru_data["id"] = len(basvurular) + 1
    basvuru_data["tarih"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    basvuru_data["durum"] = "Yeni"
    
    basvurular.append(basvuru_data)
    
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(basvurular, f, ensure_ascii=False, indent=2)
        
    return basvuru_data

def tum_basvurular() -> List[Dict[str, Any]]:
    init_db()
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []
