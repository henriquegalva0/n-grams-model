# N-Gram Model
## Definition
An n-gram model uses sequences of 'n' words or characters (n-grams) to create a probabilistic language model, predicting the next word based on a short history of preceding words. It functions by counting occurrences of these sequences in a large corpus of text to establish probabilities, enabling applications like predictive text, speech recognition, and machine translation. The "n" in n-gram can be any number, with common examples being unigrams (single words), bigrams (two-word sequences), and trigrams (three-word sequences).

## Mission
The mission of this repository is to build a functional minimal gram model where the user can inform the "N" and it complete sentences based on one single word without using extremely sofisticated and efficient frameworks.
### Structure
I'm only using python and its common frameworks. There is no specific AI frameworks for tokenization, lemmatization or pre-trained models.
The data being used is the portuguese version of the book [Metamorfose by Kafka](ua00106a.pdf). It was taken from a [public book repository](http://www.dominiopublico.gov.br/pesquisa/PesquisaObraForm.jsp) developed by government institutions.
