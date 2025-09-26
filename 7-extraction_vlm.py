from docling.datamodel import vlm_model_specs
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import (
    VlmPipelineOptions,
)
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.pipeline.vlm_pipeline import VlmPipeline

source = "A-sample-prescription-image-in-grayscale-version.png"

# ###### USING SIMPLE DEFAULT VALUES
# # - GraniteDocling model
# # - Using the transformers framework

# converter = DocumentConverter(
#     format_options={
#         InputFormat.PDF: PdfFormatOption(
#             pipeline_cls=VlmPipeline,
#         ),
#     }
# )

# doc = converter.convert(source=source).document

# print(doc.export_to_markdown())


# ###### USING MACOS MPS ACCELERATOR
# # For more options see the compare_vlm_models.py example.

pipeline_options = VlmPipelineOptions(
    vlm_options=vlm_model_specs.SMOLDOCLING_TRANSFORMERS,
)

converter = DocumentConverter(
    format_options={
        InputFormat.PDF: PdfFormatOption(
            pipeline_cls=VlmPipeline,
            pipeline_options=pipeline_options,
        ),
    }
)

doc = converter.convert(source=source).document

print(doc.export_to_markdown())
