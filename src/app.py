from frontend import ExcelValidadorUI
from backend import process_excel

def main():
    
    ui = ExcelValidadorUI()
    ui.display_header()
    uploaded_file = ui.upload_file()

    if uploaded_file: 
        result, errors =  process_excel(uploaded_file)
        ui.display_results(errors)

if __name__ == '__main__': 
    main()