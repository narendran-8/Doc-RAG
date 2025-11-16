from langchain.document_loaders import PyPDFLoader
import tempfile

class RAG_Service:
    def __init__(self):
        pass

    def process_file(self, file_bytes):
        # Save bytes to a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(file_bytes)
            tmp_path = tmp.name

        self.pdf_pages = PyPDFLoader(tmp_path).load()
        print(self.pdf_pages)


    