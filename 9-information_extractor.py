from IPython import display
from pydantic import BaseModel, Field
from rich import print
from docling.datamodel.base_models import InputFormat
from docling.document_extractor import DocumentExtractor
from typing import Optional

file_path = (
    "https://upload.wikimedia.org/wikipedia/commons/9/9f/Swiss_QR-Bill_example.jpg"
)

extractor = DocumentExtractor(allowed_formats=[InputFormat.IMAGE, InputFormat.PDF])

class Invoice(BaseModel):
    bill_no: str = Field(
        examples=["A123", "5414"]
    )  # provide some examples, but no default value
    total: float = Field(
        default=10, examples=[20]
    )  # provide some examples and a default value
    tax_id: Optional[str] = Field(default=None, examples=["1234567890"])
    
result = extractor.extract(
    source=file_path,
    template=Invoice,
)
print(result.pages)    