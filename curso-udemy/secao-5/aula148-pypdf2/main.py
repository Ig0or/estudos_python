import PyPDF2

caminho_dos_pdfs = r"C:\Users\office\Desktop\estudos_python\curso-udemy\secao-5\aula148-pypdf2\pdf"

# Unir PDFS

# novo_pdf = PyPDF2.PdfFileMerger()
#
# for root, dirs, files in os.walk(caminho_dos_pdfs):
#     for file in files:
#         caminho_completo_arquivo = os.path.join(root, file)
#
#         arquivo_pdf = open(caminho_completo_arquivo, 'rb')
#         novo_pdf.append(arquivo_pdf)
#
# with open(f'{caminho_dos_pdfs}/novo_arquivo.pdf', 'wb') as meu_novo_pdf:
#     novo_pdf.write(meu_novo_pdf)


# Dividir PDFS

caminho_original = 'pdf/python-documentation.pdf'

with open(caminho_original, 'rb') as arquivo_pdf:
    leitor = PyPDF2.PdfFileReader(arquivo_pdf)
    num_paginas = leitor.getNumPages()

    for num_pagina in range(num_paginas):
        escritor = PyPDF2.PdfFileWriter()
        pagina_atual = leitor.getPage(num_pagina)
        escritor.addPage(pagina_atual)

        with open(f'novos_pdfs/{num_pagina}.pdf', 'wb') as novo_pdf:
            escritor.write(novo_pdf)
