from .models import ATAcontent
from django.shortcuts import render
from dotenv import load_dotenv
import fitz, os
import google.generativeai as genai

load_dotenv()

genai.configure(api_key = os.getenv("API_KEY"))

def upload_pdf(request):
    if request.method == "POST" and request.FILES["pdf_file"]:
        pdf_file = request.FILES["pdf_file"]
        pdf_text = ""

        with fitz.open(stream=pdf_file.read(), filetype="pdf") as pdf:
            for page_num in range(pdf.page_count):
                page = pdf.load_page(page_num)
                pdf_text += page.get_text("text")
        
        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content("Retorne apenas o nome dos atendentes separados por vírgula: " + pdf_text)
        nomes_string = response.text
        nomes_lista = [nome.strip() for nome in nomes_string.split(",")]
        
        return render(request, 'atendentes.html', {'atendentes': nomes_lista})
    return render(request, "upload_pdf.html")
