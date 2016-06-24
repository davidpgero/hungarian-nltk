# hungarian-nltk

Examples of Hungarian Sentence Analysis with NLTK

# Install
```bash
conda build .
```

# Examples

## AB grammar
![AB grammar](/images/ab.png?raw=true "AB grammar")

## Context free grammar
![Peter and Mari](/images/peter_mari.png?raw=true "Peter and Mari")

## Regexp stemmer
| word,stem      |
|----------------|
| Péter,Péter    |
| szereti,szeret |
| Enikőt,Enikő   |
| és,és          |
| Marit,Mari     |

## Snowball stemmer
| word,stem      |
|----------------|
| Péter,péter    |
| szereti,szeret |
| Enikőt,enikő   |
| és,és          |
| Marit,mar      |

## Unigramm Tagger
```bash
python examples/unigramm_tagger.py
[('Péter', 'N'), ('Enikő', 'N'), ('szeret', 'V'), ('Marit', 'Nacc')]
```

## Work tokenizer
```bash
python examples/word_tokenizer_example.py
Szeretnék
kérni
tőled
egy
óriási
szívességet
.
```
