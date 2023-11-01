from xlwt import Workbook 

# Class that creates a workbook and inserts data into it
class InsertIntoExcel:
    def __init__(self, filename):
        self.filename = filename
        self.wb = Workbook()
        self.sheet1 = self.wb.add_sheet('Sheet 1')
        self.row = 0
        
    def insert_data(self, col, data):
        self.sheet1.write(self.row, col, data)
    def insert_new_row(self):
        self.row += 1
    def save_workbook(self):
        self.wb.save(self.filename)

