import cv2
import pytesseract

def ExtractText(imagePath) -> str:
  try:
    img = cv2.imread(imagePath)
    custom_config = r'--oem 3 --psm 6'
    str = pytesseract.image_to_string(img, config=custom_config, lang="mar+eng")
    str = str.strip()
    str = str.replace("\r\n", "\n")
    str = str.replace("\n\n", "\n")
    if str == "":
      return "Error"
    return str
  except Exception as e:
    print("Error in ExtractText", str(e))
    return "Error"
