This repository is hands-on on various features available in Docling Python Library. 
https://docling-project.github.io/docling/

Features
🗂️ Parsing of multiple document formats incl. PDF, DOCX, PPTX, XLSX, HTML, WAV, MP3, VTT, images (PNG, TIFF, JPEG, ...), and more
📑 Advanced PDF understanding incl. page layout, reading order, table structure, code, formulas, image classification, and more
🧬 Unified, expressive DoclingDocument representation format
↪️ Various export formats and options, including Markdown, HTML, DocTags and lossless JSON
🔒 Local execution capabilities for sensitive data and air-gapped environments
🤖 Plug-and-play integrations incl. LangChain, LlamaIndex, Crew AI & Haystack for agentic AI
🔍 Extensive OCR support for scanned PDFs and images
👓 Support of several Visual Language Models (GraniteDocling)
🎙️ Support for Audio with Automatic Speech Recognition (ASR) models
🔌 Connect to any agent using the Docling MCP server
💻 Simple and convenient CLI

Tested Almost all the features available in Docling 

1) Extracting text from PDF including table structures, annotating images , generating picture descriptions using default models provided by Docling and also using OpenAI Api, and also extracting text from any of the
  images using ocr_options.
2) Extracting text from CSV files by Default Docling options
3) Extracting text from Images using different OCR engines and VLM models provided by docling. (Hugging Face models, SMOL DOCLING, GRANITE DOCLING).
      -- Tesseract OCR Engine : Little Noisy data
      -- RapidOCR Engine:(with accelerator options): All the data was extracted without any mistakes.
      -- Checked with Passport and Aadhar card
      -- SMOL DOCLING: A small open source hugging face model , worked well in extracting complete handwritten text from medical prescription
      -- GRANITE DOCLING: Just released on September 17, 2025-- is still not stable -- code given in the model card itself failed even when used float16 dType
4)Hybrid Chunker : Worked but chunks with contextulize had some incomplete words
5)OpenAI tokenizer: Worked extremely well with all the chunks carrying context
6)Output format of the Docling Document:
       -- Markdown with table and image enrichments is good
       -- DocTags format is useful in some scenarios
       -- Extracting some pieces of data example bill no from invoice etc is working well with docling.extractor but its still in beta version. We can extract data in pydantic model and can be directly for downstram worflows, can extract even string and dict formats as below
   [
    ExtractedPageData(
        page_no=1,
        extracted_data={'bill_no': '3139', 'total': 3949.75, 'tax_id': None},
        raw_text='{"bill_no": "3139", "total": 3949.75, "tax_id": null}',
        errors=[]
    )
]
