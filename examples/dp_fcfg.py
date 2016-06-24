# hun_dp_fcfg.py
from nltk import load_parser
from nltk.draw import draw_trees


if __name__ == '__main__':
    parser = load_parser('file:data/hun_dp.fcfg')

    sentences = [
            ['ember'],
            ['kutya'],
            ['egy', 'kutya'],
            ['egy', 'ember'],
            ['az', 'ember'],
            ['a', 'kutya']
            ]
    trees = []
    for sentence in sentences:
        for tree in parser.parse(sentence):
            trees.append(tree)

    draw_trees(*trees)
