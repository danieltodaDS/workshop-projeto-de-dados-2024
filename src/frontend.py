import streamlit as st

class ExcelValidadorUI: 

    def __init__ (self): 
        self.set_page_config()

    def set_page_config(self): 
        st.set_page_config(
            page_title = 'Validador de schema excel'
        )

    def display_header(self): 
        st.title('Validador de schema excel')

    def display_results (self, errors): 
        if errors: 
               st.error(f"Erro na validacao: {errors}") 
            # else:    
            #     for error in errors: 
            #         st.error(f"Erro na validacao: {error}")
        else: 
            st.success("O schema do arquivo excel esta correto")

    def upload_file(self): 
        return st.file_uploader('Carregue seu arquivo excel aqui', type=['xlsx'])