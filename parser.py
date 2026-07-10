import fitz


def extract_text(pdf_file):
    """
    Extract text from a PDF using PyMuPDF.

    Args:
        pdf_file: Uploaded PDF file from Streamlit.

    Returns:
        str: Extracted text.
    """

    pdf_bytes = pdf_file.read()
    pages = []

    try:
        with fitz.open(stream=pdf_bytes, filetype="pdf") as doc:

            for page in doc:

                page_text = page.get_text("text").strip()

                if page_text:
                    pages.append(page_text)

    except Exception as e:
        raise RuntimeError(f"Error reading PDF: {e}")

    return "\n\n".join(pages)