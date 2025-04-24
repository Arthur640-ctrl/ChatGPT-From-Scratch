# Welcome to the Chat-GPT-From-Scratch documentation !

Chat-GPT-From-Scratch is a new homemade AI. The goal is for it to resemble ChatGPT, with a budget of 0€ and just one person working on the project. This project was made possible by this GitHub [project](https://github.com/ThePixelCrafted/chatgpt_de_zero).

## Table of contents
- [Introduction](#introduction)
- [Features](#features)

## Introduction
This project was made possible by this GitHub [project](https://github.com/ThePixelCrafted/chatgpt_de_zero).

Currently, it includes:

- Tokenizer (BPE: Byte Pair Encoding)

Coming soon:

- CHAT GPT architecture"

## Features
All features :
- [BPETokenizer](#---bpetokenizer---)
- [Features](#features)
  
### -- BPETokenizer --
For the tokenizer to work, it needs vocabulary. There are two options: either you train your tokenizer from a large text, which will create a vocabulary, or you have already trained it or downloaded the vocabulary, and you just need to load it.

#### <u>🧠 - Training your tokenizer</u> 
For your tokenizer to have vocabulary, you need to train it with a large amount of data. The more data it has, the larger its vocabulary will be, and the more powerful it will become.

```python
from bpe_tokenizer.dataset import Dataset
from bpe_tokenizer.tokenizer import BPETokenizer

dataset = Dataset()
dataset.preprocess()

tokenizer = BPETokenizer()
tokenizer.train(dataset)

tokenizer.save("data/tokenizer.json")
```

Let's break it down :
```python
dataset = Dataset()
```
This line loads a file of French conversations from Reddit; it's a huge text file.

```python
dataset.preprocess()
```
This line will process the file to remove unnecessary elements and perform other small manipulations.
```python
tokenizer = BPETokenizer()
```
This line will initialize the tokenizer.

**⚠️ NOTE : By default, the number of elements your tokenizer will learn is limited to 10,000. To increase this number, put 'vocab_size=maximum number of elements' inside the parentheses.**

Once that's done, all that's left is to train it with this line :

```python
tokenizer.train(dataset)
```

To avoid retraining every time, you can save the vocabulary :

```python
tokenizer.save("Chemin")
```

#### <u>⏩ - Charger un vocabulaire existant</u>

There’s nothing simpler ! In just two lines, everything is ready :

```python
from bpe_tokenizer.dataset import Dataset
from bpe_tokenizer.tokenizer import BPETokenizer

tokenizer = BPETokenizer()
tokenizer.load("Chemin du vocab")
```

#### <u>🔥 - Tester le tokenizer</u>

To test, you need to initialize the tokenizer and the vocabulary :

```python
from bpe_tokenizer.dataset import Dataset
from bpe_tokenizer.tokenizer import BPETokenizer

tokenizer = BPETokenizer()
tokenizer.load("Chemin du vocab")
```

Then, we add :

```python
encoded = tokenizer.encode("J'aime les avions")
```
If we print it, we get a sequence of numbers : *[11, 12, 866, 2, 97, 2, 5515]*

*👁️ NOTE : The numbers vary for each person; everyone will have different ones !*

To decode a text in this form : *[11, 12, 866, 2, 97, 2, 5515]*, we use the .decode(Text to decode) function :
```python
decoded = tokenizer.decode(encode)
```
If we print it, we get : *j'aime les avions*

🔰- Complete example of .encode() and .decode() :

With this code :
```python
from bpe_tokenizer.dataset import Dataset
from bpe_tokenizer.tokenizer import BPETokenizer

tokenizer = BPETokenizer()
tokenizer.load("data/tokenizer.json")

test_text = "J'aime les avions"
encoded = tokenizer.encode(test_text)
decoded = tokenizer.decode(encoded)

print(f"Original: {test_text}")
print(f"Encoded: {encoded}")
print(f"Decoded: {decoded}")
```
We get :
```text
Original: J'aime les avions
Encoded: [11, 12, 866, 2, 97, 2, 5515]
Decoded: j'aime les avions
```

Tanks

