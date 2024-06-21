# Text-to-Speech:

This Python script showcases a variety of natural language processing (NLP) tasks using the NLTK (Natural Language Toolkit) library and integrates text-to-speech functionality with `pyttsx3` and `gTTS`. Here's how it works:

The script begins by installing necessary dependencies (`nltk`, `gTTS`, `pyttsx3`) if they are not already installed. It then imports these libraries for further use in the script.

### NLTK Tasks:
1. **Tokenization**: 
   - It demonstrates both word and sentence tokenization using `word_tokenize()` and `sent_tokenize()` functions from NLTK. Tokenization breaks text into smaller units, either words or sentences, which facilitates further analysis.
   
2. **N-grams**:
   - It calculates bi-grams, tri-grams, and 5-grams using NLTK's `bigrams()`, `trigrams()`, and `ngrams()` functions. N-grams are sequences of `n` contiguous items from a given sample of text, useful for analyzing word sequences and predicting next words.
   
3. **Stemming**:
   - It uses the Porter Stemmer (`PorterStemmer`) from NLTK to find the root or base form of words. Stemming reduces words to their linguistic roots, which helps in tasks like text classification and information retrieval.
   
4. **Part-of-Speech Tagging**:
   - Demonstrates part-of-speech tagging (`pos_tag()`) using NLTK, which assigns grammatical tags to words in a sentence. These tags denote whether a word is a noun, verb, adjective, etc., aiding in syntactic analysis.
   
5. **Named Entity Recognition (NER)**:
   - Utilizes NLTK's `ne_chunk()` function for named entity recognition. It identifies named entities such as names, organizations, and locations in a sentence, enhancing understanding of the content.

### Text-to-Speech:
- **gTTS (Google Text-to-Speech)**:
  - Imports `gTTS` to convert text input into speech. It generates an audio file (`1.wav`) from the input text and plays it using `Audio()` from IPython.display, enabling text-to-speech functionality.

- **pyttsx3**:
  - Implements `pyttsx3` for text-to-speech conversion with different settings:
    - Adjusts voice rate (`rate`) and volume (`volume`) using `engine.setProperty()`.
    - Changes the voice type between male and female by setting `engine.setProperty('voice', voices[0].id)` or `engine.setProperty('voice', voices[1].id)`.
    - Demonstrates text-to-speech conversion with custom voice settings and outputs.
  
The script concludes with a demonstration of event handling during speech synthesis using `pyttsx3`. It connects to events (`started-utterance`, `started-word`, `finished-utterance`) to monitor speech synthesis progress and completion.

This script serves as a comprehensive introduction to NLP tasks and text-to-speech capabilities in Python, showcasing practical applications across various linguistic analyses and speech synthesis scenarios.
