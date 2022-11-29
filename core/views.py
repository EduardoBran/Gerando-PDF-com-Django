import io

from django.http import FileResponse
from django.views.generic import View
from reportlab.pdfgen import canvas


class IndexView(View):
    
    def get(self, request, *args, **kwargs):
        
        # Cria um arquivo para receber os dados e gerar o PDF
        buffer = io.BytesIO() # cria arquivo temporário no disco
        
        # Cria o arquivo pdf
        pdf = canvas.Canvas(buffer)
        
        # Insere 'coisas' no PDF
        pdf.drawString(100, 100, "Geek University")
        
        # Após inserir no PDF
        pdf.showPage()
        pdf.save()
        
        # Para finalizar retornamos o buffer para o início do arquivo
        buffer.seek(0)
        
        # Faz o download direto do arquivo PDF
        # return FileResponse(buffer, as_attachment=True, filename='relatorio1.pdf')
        
        # Abre o PDF direto no navegador
        return FileResponse(buffer, filename='relatorio1.pdf')