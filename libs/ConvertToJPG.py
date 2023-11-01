import fitz
from libs import Utils
from tqdm import tqdm

def ConvertToImage(image_dir: str, inputPath: str, startPage: int, endPage: int) -> bool:
    try:
        pdffile = fitz.open(inputPath)
        doc = fitz.open(pdffile)
        zoom = 4
        mat = fitz.Matrix(zoom, zoom)
        count = 0
        for p in doc:
            count += 1
        counter = count
        if endPage != 0:
            counter = min(endPage, count) - startPage
        else:
            counter = count - startPage
        progress_bar = tqdm(total=counter, unit='iteration', ncols=80)
        for i in range(startPage - 1, min(endPage, count) if endPage != 0 else count):
            val = f"{image_dir}/image_{i + 1}.png"
            page = doc.load_page(i)
            pix = page.get_pixmap(matrix=mat)
            pix.save(val)
            # Utils.show_progress("--> Converting Pages to Images: " + str(i + 1) + " / " + str(count) + " done.")
            progress_bar.update(1)
        doc.close()
        return True
    except Exception as e:
        print("Error:", str(e))
        return False


