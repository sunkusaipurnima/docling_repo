import urllib.request
from io import BytesIO
from docling.backend.html_backend import HTMLDocumentBackend
from docling.datamodel.base_models import InputFormat
from docling.datamodel.document import InputDocument

url = "https://en.wikipedia.org/wiki/Duck"

# Add headers to mimic a browser
req = urllib.request.Request(
    url,
    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"}
)

# Fetch HTML with headers
response = urllib.request.urlopen(req)
html_bytes = response.read()

# Pass to Docling
in_doc = InputDocument(
    path_or_stream=BytesIO(html_bytes),
    format=InputFormat.HTML,
    backend=HTMLDocumentBackend,
    filename="duck.html",
)
backend = HTMLDocumentBackend(in_doc=in_doc, path_or_stream=BytesIO(html_bytes))
dl_doc = backend.convert()

print(dl_doc.export_to_markdown())
