# Docling Python Library - Hands-On Examples

This repository demonstrates hands-on usage of various features available in the [Docling Python Library](https://docling-project.github.io/docling/).

## Features

- 🗂️ **Multi-format Document Parsing**  
  Supports PDF, DOCX, PPTX, XLSX, HTML, WAV, MP3, VTT, images (PNG, TIFF, JPEG, …) and more.

- 📑 **Advanced PDF Understanding**  
  Includes page layout, reading order, table structures, code, formulas, image classification, and more.

- 🧬 **Unified DoclingDocument Representation**  
  Expressive and consistent format for all document types.

- ↪️ **Various Export Formats**  
  Markdown, HTML, DocTags, and lossless JSON.

- 🔒 **Local Execution**  
  Works with sensitive data and air-gapped environments.

- 🤖 **Integrations**  
  Plug-and-play integrations with LangChain, LlamaIndex, Crew AI, and Haystack for agentic AI workflows.

- 🔍 **Extensive OCR Support**  
  For scanned PDFs and images.

- 👓 **Visual Language Models (VLMs)**  
  Supports multiple models including GraniteDocling.

- 🎙️ **Audio Support**  
  Automatic Speech Recognition (ASR) models supported.

- 🔌 **Docling MCP Server**  
  Connect to any agent using the server.

- 💻 **Convenient CLI**  
  Simple command-line interface for all features.

---

## Hands-On Examples Tested

### 1️⃣ Text Extraction from PDF
- Extracted text including **table structures**.  
- Annotated images and generated **image descriptions** using default Docling models and OpenAI API.  
- Extracted text from images using **OCR options**.

### 2️⃣ CSV Extraction
- Extracted text from CSV files using default Docling options.

### 3️⃣ Image Extraction Using Different OCR & VLM Models
- **Tesseract OCR Engine**: Minor noisy data.  
- **RapidOCR Engine**: Accurate extraction with accelerator options.  
- **SMOL DOCLING**: Small Hugging Face model, effective for handwritten text (e.g., medical prescriptions).  
- **GRANITE DOCLING**: Recently released (Sep 17, 2025). Still unstable; model card code failed with float16 dtype.

> Tested examples include **passport** and **Aadhar card** images.

### 4️⃣ Hybrid Chunker
- Worked with context-aware chunks.  
- Some chunks had incomplete words in certain cases.

### 5️⃣ OpenAI Tokenizer
- Performed extremely well.  
- All chunks retained context properly.

### 6️⃣ Docling Document Output Formats
- **Markdown**: Good table and image enrichment.  
- **DocTags**: Useful in specific scenarios.  
- **Extractor** (Beta):
  - Extract data into Pydantic models, strings, or dictionaries.  
  - Example:
  ```python
  [
      ExtractedPageData(
          page_no=1,
          extracted_data={'bill_no': '3139', 'total': 3949.75, 'tax_id': None},
          raw_text='{"bill_no": "3139", "total": 3949.75, "tax_id": null}',
          errors=[]
      )
  ]
