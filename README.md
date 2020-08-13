# Hungarian NLTK

Examples of Hungarian Sentence Analysis with [NLTK](http://www.nltk.org/ "NLTK") `~> 3.2.1`

> Gerő Dávid Péter (2014) Egyszerű magyar mondatok kezelése NLTK környezetben. BA/BSc, Szegedi Tudományegyetem. [http://diploma.bibl.u-szeged.hu/51272/]

# Install
## Prerequisite

* I recommend to use [Anaconda](https://www.continuum.io/downloads "Anaconda 3")
* Python `~> 3.5` (It includes in Anaconda 3)

## Install with Conda
```bash
conda build .
```

## Install without Anaconda
```bash
easy_install install nltk
```

# Examples

## AB grammar
![AB grammar](/images/ab.png?raw=true "AB grammar")

## Context free grammar
![Peter and Mari](/images/peter_mari.png?raw=true "Peter and Mari")

## FCFG
![FCFG](/images/fcfg.png?raw=true "FCFG")

## Regexp stemmer
Word | Stem
--- | ---
Péter | Péter
szereti | szeret
Enikőt | Enikő
és | és
Marit | Mari

## Snowball stemmer
Word | Stem
--- | ---
Péter| péter
szereti | szeret
Enikőt | enikő
és | és
Marit | mar

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
The parsed tree: '(S[SEM=<exists x.(-alive(x) & -agent(x))>]
  (NP[SEM=<\P.exists x.(-alive(x) & P(x))>]
    (Det[SEM=<\Q P.exists x.(Q(x) & P(x))>] egy)
    (N[SEM=<\x.-alive(x)>] asztal))
  (VP[SEM=<\x.-agent(x)>] (V[SEM=<\x.-agent(x)>] poros)))'
The semantic formula: 'exists x.(-alive(x) & -agent(x))'
The semantic value: 'True'
```

A `False` sentence: `egy asztal fut` ~> `a table runs`

```bash
The sentence: 'egy asztal fut'
The parsed tree: '(S[SEM=<exists x.(-alive(x) & agent(x))>]
  (NP[SEM=<\P.exists x.(-alive(x) & P(x))>]
    (Det[SEM=<\Q P.exists x.(Q(x) & P(x))>] egy)
    (N[SEM=<\x.-alive(x)>] asztal))
  (VP[SEM=<\x.agent(x)>] (V[SEM=<\x.agent(x)>] fut)))'
The semantic formula: 'exists x.(-alive(x) & agent(x))'
The semantic value: 'False'
```
