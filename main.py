import os
from fastapi import FastAPI
from google import genai

# Vercel akan mengambil kunci ini dari pengaturan sistem
KUNCI_API_SAYA = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=KUNCI_API_SAYA)
app = FastAPI()

# Sisanya sama seperti kodemu sebelumnya...
@app.get("/")
def halaman_utama():
    return {"pesan": "Server AI Online!"}

@app.get("/tanya-ai")
def tanya(prompt: str):
    try:
        respon = client.models.generate_content(
            model='gemini-2.0-flash',
            contents=prompt,
        )
        return {"pertanyaan_kamu": prompt, "jawaban_ai": respon.text}
    except Exception as e:
        return {"status": "Gagal", "error": str(e)}