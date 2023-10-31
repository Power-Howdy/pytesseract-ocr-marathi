import fitz

# Create a function that gets inputPath as a string, pdfFilePath, startPage default 1 and endPage default 0, if startpage is not 1, then only extract from startpage, for endpage, if endpage is not 0, then extract from startpage to the given endpage
def ConvertToImage(inputPath, startPage=1, endPage=0):
    print("--> Converting pdf to images.")
    pdffile = fitz.open("pdfs/"+inputPath)
    doc = fitz.open(pdffile)
    zoom = 4
    mat = fitz.Matrix(zoom, zoom)
    count = 0
    # Count variable is to get the number of pages in the pdf
    for p in doc:
        count += 1
    # add if endPage is not 0 then min(endPage, count) will be used, otherwise range(count) will be used
    for i in range(startPage-1, min(endPage, count) if endPage != 0 else count):
        val = f"images/image_{i+1}.png"
        page = doc.load_page(i)
        pix = page.get_pixmap(matrix=mat)
        pix.save(val)
        print("--> Convert Page " + str(i + 1) + " done.")
    doc.close()

ConvertToImage("test.pdf", 1, 10)
