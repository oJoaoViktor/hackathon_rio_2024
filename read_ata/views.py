from .models import ATAcontent
from django.shortcuts import render
from dotenv import load_dotenv
import fitz, openai, os
import google.generativeai as genai

load_dotenv()

genai.configure(api_key = os.getenv("API_KEY"))

def upload_pdf(request):
    pdf_path = "C:\\Users\\TRJ1JVL\\Documents\\GitHub\\Hackathon\\dia 1 - resumo.pdf"
    pdf_text = ""

    with fitz.open(pdf_path) as pdf:
        for page_num in range(pdf.page_count):
            page = pdf.load_page(page_num)
            pdf_text += page.get_text("text")
    
    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content("Retorne apenas o nome dos atendentes separados por vírgula: "+pdf_text)
    nomes_string = response.text
    nomes_lista = [nome.strip() for nome in nomes_string.split(",")]
    atendentes = {f"atendente_{i+1}": nome for i, nome in enumerate(nomes_lista)}
    
    return render(request, 'atendentes.html', {'atendentes': atendentes})
