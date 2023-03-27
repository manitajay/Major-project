import openpyxl

def attend(scholar_no,subject_code):
    file=subject_code+'.xlsx'
    df=openpyxl.load_workbook(file)
    lf=df.active
    ss1='B'+str(scholar_no+1)
    cl=lf[ss1]
    ss2='B'+str(410)
    cl2=lf[ss2]
    print(cl.value)
    val1=cl.value+1
    print(val1)
    lf[ss1]=str(val1)
    val2=cl2.value+1
    lf[ss2]=str(val2)
    df.save(filename=file)

attend(83,"EC431")
    