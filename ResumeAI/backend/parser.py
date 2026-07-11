import fitz


def extract_text(pdf_file) -> str:
    """
    Extract text from a PDF using PyMuPDF.

    Args:
        pdf_file: A file-like object containing PDF data.

    Returns:
        The extracted text from all pages.

    Raises:
        ValueError: If no readable text is found.
        RuntimeError: If the PDF cannot be processed.
    """

    pages = []

    try:
        pdf_bytes = pdf_file.read()

        with fitz.open(stream=pdf_bytes, filetype="pdf") as document:

            for page in document:

                page_text = page.get_text("text").strip()

                if page_text:
                    pages.append(page_text)

        if not pages:
            raise ValueError("No readable text found in the uploaded PDF.")

        return "\n\n".join(pages)

    except RuntimeError:
        raise

    except Exception as exc:
        raise RuntimeError("Failed to extract text from the uploaded PDF.") from exc