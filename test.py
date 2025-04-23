from bpe_tokenizer.dataset import Dataset
from bpe_tokenizer.tokenizer import BPETokenizer

# Load a saved tokenizer
tokenizer = BPETokenizer()
tokenizer.load("data/tokenizer.json")

# Test encoding and decoding
test_text = "J'aime les avions"
encoded = tokenizer.encode(test_text)
decoded = tokenizer.decode(encoded)

print(f"Original: {test_text}")
print(f"Encoded: {encoded}")
print(f"Decoded: {decoded}")