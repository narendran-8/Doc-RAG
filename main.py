from fastapi import FastAPI, UploadFile, File
from langchain.document_loaders import PyPDFLoader
from typing import List

from io import BytesIO
from PyPDF2 import PdfReader


from services import RAG_Service

app = FastAPI(title="FileUpload")

 


# xls and pdf files

@app.post("/read_files")
async def read_file(files: UploadFile = File(...)):
    content = await files.read()

    file_name = files.filename.lower()

    # if file_name.endswith(".txt"):
    if file_name.endswith(".txt") or file_name.endswith(".md"):
        text_content = content.decode("utf-8", errors="ignore")

        return {
            "type": "Text/Markdown",
            "file_name": files.filename,
            "content": text_content[:1000]  # Return first 1000 chars for brevity
        }

 
    elif file_name.endswith(".pdf"):
        pdf = PdfReader(BytesIO(content))
        # print(pdf.pages.extract_text())
        
        RAG_Service().process_file(content)
        first_page_text = pdf.pages[0].extract_text()


        return {
            "type": "PDF",
            "file_name": files.filename,
            "num_pages": len(pdf.pages),
            "first_page_text": first_page_text
        }

