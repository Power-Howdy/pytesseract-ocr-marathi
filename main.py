from libs import Utils
from libs.ConvertToJPG import ConvertToImage
from libs.CleanDir import CleanDir
from libs.ExtractInfoFromString import extract_information
from libs.ExtractTextFromImage import  ExtractText
from libs.InsertIntoExcel import InsertIntoExcel
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
result_dir = "result"
result_filename = "result"
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
      result = CleanDir(image_dir)
      if result == True:          
        # if start_page is 1 and end_page is 0, don't pass these params
        result = ConvertToImage(image_dir, pdf_file_name, int(start_page), int(end_page))
        if result == True:
            Utils.msg_info("\n--> Successfully converted to JPG")
            result_filename = Utils.optional_input("Enter the file name to save result(optional, default is 'test.xls'): ")
            if result_filename == "":
               result_filename = "test.xls"
            else:
               result_filename += ".xls"
            # Get the list of filenames in the folder
            filenames = os.listdir(image_dir)
            excelWriter = InsertIntoExcel(result_dir + "/" + result_filename)
            excelWriter.insert_data(0, 'No')
            excelWriter.insert_data(1, 'Name')
            excelWriter.insert_data(2, 'Father\'s name')
            excelWriter.insert_data(3, 'House no')
            excelWriter.insert_data(4, 'Age')
            excelWriter.insert_data(5, 'Gender')
            excelWriter.insert_data(6, 'ID')
            excelWriter.insert_new_row()
            for k in range(len(filenames)):
                str =  ExtractText(image_dir + "/" + filenames[k])
                if str != "Error":
                    info = extract_information(str)
                    if len(info) == 0:
                       Utils.msg_warning("--> Error Occured while extracting information from string: " + filenames[k])
                       continue
                    else:
                       for i in  range(len(info)):
                          excelWriter.insert_data(0, info[i]['no'])
                          excelWriter.insert_data(1, info[i]['name'])
                          excelWriter.insert_data(2, info[i]['fname'])
                          excelWriter.insert_data(3, info[i]['hno'])
                          excelWriter.insert_data(4, info[i]['age'])
                          excelWriter.insert_data(5, info[i]['gender'])
                          excelWriter.insert_data(6, info[i]['ID'])
                          excelWriter.insert_new_row()
                       Utils.show_progress("--> Inserted records for " + filenames[k])
                else:
                  Utils.msg_warning("\n--> Error Occured while OCR: " + filenames[k])
                  continue
            excelWriter.save_workbook()
Utils.msg_success("\n--------------------------------")
Utils.msg_success("      >>>>> Finished <<<<<")
Utils.msg_success("--------------------------------")
