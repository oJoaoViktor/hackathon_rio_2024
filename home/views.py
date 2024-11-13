from django.shortcuts import render
from read_audio.views import transpose_audio_for_text
from read_ata.views import upload_pdf


def post_form(request):
    if request.method == "POST":
        if request.FILES["audio"] and request.FILES["pdf_file"]:
            ata_file = request.FILES["pdf_file"]
            audio_file = request.FILES["audio"]
            
            audio_transcription = transpose_audio_for_text(audio_file)
            
            list_names = upload_pdf(ata_file)

    return render(request, 'atendentes.html', {'atendentes': list_names})