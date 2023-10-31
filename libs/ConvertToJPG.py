import fitz


def ConvertToImage(inputPath: str, startPage: int = 1, endPage: int = 0) -> bool:
    try:
        print("--> Converting pdf to images.")
        pdffile = fitz.open("pdfs/" + inputPath)
        doc = fitz.open(pdffile)
        zoom = 4
        mat = fitz.Matrix(zoom, zoom)
        count = 0
        for p in doc:
            count += 1
        for i in range(startPage - 1, min(endPage, count) if endPage != 0 else count):
            val = f"images/image_{i + 1}.png"
            page = doc.load_page(i)
            pix = page.get_pixmap(matrix=mat)
            pix.save(val)
            print("--> Convert Page " + str(i + 1) + " done.")
        doc.close()
        return True
    except Exception as e:
        print("Error:", str(e))
        return False


