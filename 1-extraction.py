from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.pipeline_options import PdfPipelineOptions, RapidOcrOptions,TesseractOcrOptions
from docling.datamodel.base_models import InputFormat

pipeline_options = PdfPipelineOptions()
# pipeline_options.do_formula_enrichment = True
pipeline_options.do_table_structure=True
# pipeline_options.do_picture_description = True
pipeline_options.do_ocr = True
pipeline_options.ocr_options= RapidOcrOptions(backend="onnxruntime")

converter = DocumentConverter(format_options={
    InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
})

result = converter.convert("./Purnima_passportscan.pdf")
doc = result.document
print(doc.export_to_markdown())

