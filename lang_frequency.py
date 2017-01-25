import argparse
import re
from collections import Counter


def parser_config():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description='''\
            Read data from json file, set in first argument.
            Print it in pretty json format''')
    parser.add_argument('file_path', metavar='data.json', type=str,
                        help='path to the json file')
    return parser


def load_data(filepath):
    with open(filepath) as file:
        data = file.read()
    return data


def replace_symbols_to_space(text):
    unwelcome_symbols = [':', '.', '-', '(', ')', '+', '/', '"', '1', '2', '3',
                         '4', '5', '6', '7', '8', '9', '0', '@', '#', '$', '%',
                         '\t', '\n', ';', '~', '№', '%', '*', '[', ']', '=',
                         '“', '&', '\'', ',', '<', '>', '\\', '^', '|']
    for symbol in unwelcome_symbols:
        text = text.replace(symbol, ' ')
    return re.sub(r'\s+', ' ', text)


def get_most_frequent_words(text, count):
    text = replace_symbols_to_space(text)
    words = text.split()
    words_statistics = [[x, words.count(x)] for x in set(words)]
    words_statistics_sorted = sorted(words_statistics, key=lambda x: x[1],
                                     reverse=True)
    top_words = []
    for word_number in range(count):
        if word_number < len(words_statistics_sorted):
            top_words.append(words_statistics_sorted[wordNumber][0])
    return top_words


if __name__ == '__main__':
    text_to_analise = load_data(parser_config().parse_args().file_path)
    print('Top 10 words: ' + str(get_most_frequent_words(text_to_analise, 10)))
