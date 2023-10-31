from xlwt import Workbook 

# Class that creates a workbook and inserts data into it
class WorkbookCreator:
    def __init__(self, filename):
        self.filename = filename
        self.wb = Workbook()
        self.sheet1 = self.wb.add_sheet('Sheet 1')
        
    def insert_data(self, row, col, data):
        self.sheet1.write(row, col, data)
        
    def save_workbook(self):
        self.wb.save(self.filename)

