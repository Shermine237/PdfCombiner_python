# Utilisation de la bibliotheque PyPDF2 pour travailler sur les PDF
# Combiner des fichiers PDF

from PyPDF2 import PdfFileWriter, PdfFileReader

# on ouvre les fichiers a combiner :
fichierPDF1 = open("presentation.pdf", "rb")
fichierPDF2 = open("recap.pdf", "rb")

# on lit les contenu des PDF en les stockant dans des objets:
reader_fichier1 = PdfFileReader(fichierPDF1)
reader_fichier2 = PdfFileReader(fichierPDF2)

# on assemble les objects contenant des information dans un nouveau objet qui est vide
fichier_combine = PdfFileWriter()

for page in range(reader_fichier1.getNumPages()): # ajout des pages du fichierPDF1
    fichier_combine.addPage(reader_fichier1.getPage(page))
for page in range(reader_fichier2.getNumPages()): # ajout des pages du fichierPDF2
    fichier_combine.addPage(reader_fichier2.getPage(page))

# on enregistre le nouveau fichier pdf
fichier_final = open("fichierPDF_final.pdf", "wb")
fichier_combine.write(fichier_final)

# on ferme les fichiers
fichierPDF1.close()
fichierPDF2.close()
fichier_final.close()
