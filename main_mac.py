from PIL import Image
import platform_
import os
from pypdf import PdfMerger

sistema = platform.system()

cartella = 'cartella'

# Ottieni la lista dei file PDF nella cartella
jpeg_files = []
jpeg_files_jpg = [file for file in os.listdir(cartella) if file.endswith('.jpg')]

jpeg_files_jpeg = [file for file in os.listdir(cartella) if file.endswith('.jpeg')]
jpeg_files.extend(jpeg_files_jpg)
jpeg_files.extend(jpeg_files_jpeg)
# Ordina i file in modo da unirli nell'ordine corretto
jpeg_files.sort()
merger = PdfMerger()
count = 0
if sistema == "Darwin":
    for file in jpeg_files:
        image_1 = Image.open(r''+cartella+'/'+file+'')
        im_1 = image_1.convert('RGB')
        im_1.save(r''+cartella+'/nome'+str(count)+'.pdf')
        count+=1

        pdf_files = [file for file in os.listdir(cartella) if file.endswith('.pdf')]

        pdf_files.sort()

        for pdf in pdf_files:
            merger.append(cartella+'/'+pdf)
            os.remove(cartella+'/'+pdf)
else:
     for file in jpeg_files:
        image_1 = Image.open(r''+cartella+'\\'+file+'')
        im_1 = image_1.convert('RGB')
        im_1.save(r''+cartella+'//nome'+str(count)+'.pdf')
        count+=1

        pdf_files = [file for file in os.listdir(cartella) if file.endswith('.pdf')]

        pdf_files.sort()

        for pdf in pdf_files:
            merger.append(cartella+'\\'+pdf)
            os.remove(cartella+'\\'+pdf)


merger.write("unito.pdf")
merger.close()
