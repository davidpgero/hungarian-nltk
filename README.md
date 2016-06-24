# Hungarian NLTK

Examples of Hungarian Sentence Analysis with NLTK

# Install
```bash
$ conda build .
```

# Examples

## AB grammar
![AB grammar](/images/ab.png?raw=true "AB grammar")

## Context free grammar
![Peter and Mari](/images/peter_mari.png?raw=true "Peter and Mari")

## FCFG
![FCFG](/images/fcfg.png?raw=true "FCFG")

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
$ python examples/unigramm_tagger.py
[('Péter', 'N'), ('Enikő', 'N'), ('szeret', 'V'), ('Marit', 'Nacc')]
```

## Work tokenizer
```bash
$ python examples/word_tokenizer.py
Szeretnék
kérni
tőled
egy
óriási
szívességet
.
```

## Semantic
A `True` sentence: `Egy asztal poros` ~> `a table is dusty`

```bash
The sentence: 'egy asztal poros'
The parsed tree: '(S[SEM=<exists x.(-elo(x) & -cselekvo(x))>]
  (NP[SEM=<\P.exists x.(-elo(x) & P(x))>]
    (Det[SEM=<\Q P.exists x.(Q(x) & P(x))>] egy)
    (N[SEM=<\x.-elo(x)>] asztal))
  (VP[SEM=<\x.-cselekvo(x)>] (V[SEM=<\x.-cselekvo(x)>] poros)))'
The semantic formula: 'exists x.(-elo(x) & -cselekvo(x))'
The semantic value: 'True'
```

A `False` sentence: `egy asztal fut` ~> `a table runs`

```bash
The sentence: 'egy asztal fut'
The parsed tree: '(S[SEM=<exists x.(-elo(x) & cselekvo(x))>]
  (NP[SEM=<\P.exists x.(-elo(x) & P(x))>]
    (Det[SEM=<\Q P.exists x.(Q(x) & P(x))>] egy)
    (N[SEM=<\x.-elo(x)>] asztal))
  (VP[SEM=<\x.cselekvo(x)>] (V[SEM=<\x.cselekvo(x)>] fut)))'
The semantic formula: 'exists x.(-elo(x) & cselekvo(x))'
The semantic value: 'False'
```