import xlwt
import codecs

def Txt_to_Excel(inputTxt,sheetName,start_row,start_col,outputExcel):
 fr = codecs.open(inputTxt,'r')
 wb = xlwt.Workbook(encoding = 'utf-8')
 ws = wb.add_sheet(sheetName)

 line_number = 0
 row_excel = start_row
 try:
  for line in fr :
   line_number +=1
   row_excel +=1
   line = line.strip()
   line = line.split(' ')
   len_line = len(line)
   col_excel = start_col
   for j in range(len_line):
    print (line[j])
    ws.write(row_excel,col_excel,line[j])
    col_excel +=1
    wb.save(outputExcel)
 except:
  print ('')


if __name__=='__main__':
 sheetName = 'pdf'
 start_row = 1
 start_col = 1
 inputfile = '666.txt'
 outputExcel = 'lunyu.xls'
 Txt_to_Excel(inputfile,sheetName,start_row,start_col,outputExcel)