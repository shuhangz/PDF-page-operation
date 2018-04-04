from PyPDF2 import PdfFileReader, PdfFileWriter
import os
def split_pdf(infn, outfn):
    pdf_output = PdfFileWriter()
    pdf_input = PdfFileReader(open(infn, 'rb'))
    # 获取 pdf 共用多少页
    page_count = pdf_input.getNumPages()
    print(page_count)
    # 将 pdf 第五页之后的页面，输出到一个新的文件
    for i in range(5, page_count):
        pdf_output.addPage(pdf_input.getPage(i))
    pdf_output.write(open(outfn, 'wb'))
def merge_pdf(infnList, outfn):
    pdf_output = PdfFileWriter()
    for infn in infnList:
        pdf_input = PdfFileReader(open(infn, 'rb'))
        # 获取 pdf 共用多少页
        page_count = pdf_input.getNumPages()
        print(page_count)
        for i in range(page_count):
            pdf_output.addPage(pdf_input.getPage(i))
    pdf_output.write(open(outfn, 'wb'))

def first_last_page(file_dir, filename):
    pdf_output = PdfFileWriter()
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            filename_pdf = os.path.join(root,file)
            pdf_input = PdfFileReader(open(filename_pdf,'rb'),strict=False)
            print(filename_pdf)
            page_count = pdf_input.getNumPages()
            pdf_output.addPage(pdf_input.getPage(0))
            # pdf_output.addPage(pdf_input.getPage(page_count-1))
    pdf_output.write(open(filename, 'wb'))

if __name__ == '__main__':
    file_dir = r"C:\Users\zsh\Desktop\报奖论文\7_论文\3_国际会议"
    first_last_page(file_dir,'output.pdf')

