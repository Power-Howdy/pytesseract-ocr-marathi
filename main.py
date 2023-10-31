from libs import ConvertToJPG, ExtractInfoFromString, ExtractTextFromImage, InsertIntoExcel, CleanDir, Utils
import os.path

'''
Prompt user to enter pdf file name and start and end page numbers, and output Excel name
start and end page numers are optional. 
Convert the pages of the pdf into images, this returns True or False(when error)
When completed successfully, there will be images extracted in images folder name in the format of image_pageNumber.png
Now Process images one by one.
Extract text from the image using ExtractTextFromImage, this returns string when successful, 'Error' when error
Extract info(array) from string, this returns array when successful, [] when error
Finally insert this information into excel file using InsertIntoExcel
'''

pdf_dir = "pdfs"
image_dir = "images"
pdf_file_name = ""
start_page = "1"
end_page = "0"

# Start work from here
inputStr = Utils.essential_input("Enter pdf file name: ")
if inputStr == "":
    Utils.msg_error("Pdf file name is required")
else:
  pdf_file_name = pdf_dir + "/" + inputStr
  if not os.path.exists(pdf_file_name):
      Utils.msg_error("Error: File does not exist.")
  else:
      pdf_file_name = pdf_file_name    
      start_page = Utils.optional_input("Enter start page number(optional): ")
      if start_page == "":
          start_page = "1"          
      end_page = Utils.optional_input("Enter end page number(optional): ")
      if end_page == "":
          end_page = "0"
      result = CleanDir.CleanDir(image_dir)
      if result == True:          
        # if start_page is 1 and end_page is 0, don't pass these params
        result = ConvertToJPG.ConvertToImage(image_dir, pdf_file_name, int(start_page), int(end_page)) if start_page != "1" or end_page != "0" else ConvertToJPG.ConvertToImage(image_dir, pdf_file_name)
        if result == True:
            Utils.msg_info("--> Successfully converted to JPG")
            # Get the list of filenames in the folder
            filenames = os.listdir(image_dir)
            excelWriter = InsertIntoExcel("test.xls")
            for filename in filenames:
                str =  ExtractTextFromImage.ExtractText(image_dir + "/" + filename)
                if str != "Error":
                    info = ExtractInfoFromString.extract_information(str)
                    if len(info) == 0:
                       continue
                    else:
                       for rec in  info:
                          excelWriter.insert_record(rec)
                          Utils.msg_info("--> Inserted a record for " + filename)
                else:
                  Utils.msg_warning("--> Error Occured: " + filename)
                  continue
            excelWriter.save_workbook()
            Utils.msg_success(" >>>>> Finished <<<<<")
