from docling.document_converter import DocumentConverter
from docling.chunking import HybridChunker
import tiktoken
from docling_core.transforms.chunker.tokenizer.openai import OpenAITokenizer

doc = DocumentConverter().convert("https://arxiv.org/pdf/2408.09869").document

tokenizer = OpenAITokenizer(
    tokenizer=tiktoken.encoding_for_model("gpt-4o"),
    max_tokens=128 * 1024,  # context window length required for OpenAI tokenizers
)
chunker = HybridChunker(
    tokenizer=tokenizer,
    merge_peers=True,  # optional, defaults to True
)
chunk_iter = chunker.chunk(dl_doc=doc)
chunks = list(chunk_iter)




for i, chunk in enumerate(chunks):
    print(f"=== {i} ===")
    txt_tokens = tokenizer.count_tokens(chunk.text)
    print(f"chunk.text ({txt_tokens} tokens):\n{chunk.text!r}")

    ser_txt = chunker.contextualize(chunk=chunk)
    ser_tokens = tokenizer.count_tokens(ser_txt)
    print(f"chunker.contextualize(chunk) ({ser_tokens} tokens):\n{ser_txt!r}")

    print()