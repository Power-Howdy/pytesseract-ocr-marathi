import fitz
from libs import Utils

def ConvertToImage(image_dir: str, inputPath: str, startPage: int, endPage: int) -> bool:
    try:
        pdffile = fitz.open(inputPath)
        doc = fitz.open(pdffile)
        zoom = 4
        mat = fitz.Matrix(zoom, zoom)
        count = 0
        for p in doc:
            count += 1
        for i in range(startPage - 1, min(endPage, count) if endPage != 0 else count):
            val = f"{image_dir}/image_{i + 1}.png"
            page = doc.load_page(i)
            pix = page.get_pixmap(matrix=mat)
            pix.save(val)
            Utils.show_progress("--> Converting Pages to Images: " + str(i + 1) + " / " + str(count) + " done.")
        doc.close()
        return True
    except Exception as e:
        print("Error:", str(e))
        return False


