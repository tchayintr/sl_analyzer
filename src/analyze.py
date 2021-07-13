import argparse
from pathlib import Path
import re
import sys

import constants


def normalize_input_line(line):
    line = re.sub(' +', ' ', line).rstrip()
    return line


def load_data(data_path):
    data = []
    with open(data_path) as f:
        for line in f:
            line = normalize_input_line(line)
            if len(line) < 1:
                continue
            data.append(line)
    return data


def write_logs(logs, output_data_path):
    with open(output_data_path, 'w') as f:
        for log in logs:
            print('{}'.format(log), file=f)
    print('\n# Written log file: {}'.format(output_data_path))


def summarize(data, quiet=False):
    logs = []
    sents = data

    n_sents = len(sents)

    wl_sents = [len(sent) for sent in sents]
    cl_sents = [len(''.join(sent)) for sent in sents]
    words = [word for sent in sents for word in sent]

    n_words = sum(wl_sents)
    n_chars = sum(cl_sents)


    min_wps = min(wl_sents)
    min_cps = min(cl_sents)
    min_cpw = len(min(words, key=len))

    max_wps = max(wl_sents)
    max_cps = max(cl_sents)
    max_cpw = len(max(words, key=len))

    avg_wps = n_words / n_sents
    avg_cps = n_chars / n_sents
    avg_cpw = n_chars / n_words

    logs.append('### report')
    logs.append('# sent: {} ...'.format(n_sents))
    logs.append('# word: {} ...'.format(n_words))
    logs.append('# char: {} ...'.format(n_chars))

    logs.append('# words/sent: min={} max={} avg={}'.format(
        min_wps, max_wps, avg_wps))
    logs.append('# chars/sent: min={} max={} avg={}'.format(
        min_cps, max_cps, avg_cps))
    logs.append('# chars/word: min={} max={} avg={}'.format(
        min_cpw, max_cpw, avg_cpw))

    if not quiet:
        for log in logs:
            print('{}'.format(log))
    return logs


def digest(data):
    # data to sents with words
    sents = []
    for line in data:
        words = line.split(constants.SL_DATA_DELIM)
        sents.append(words)
    return sents


def run(args):
    input_data_path = args.input_data
    data = load_data(input_data_path)
    logs = summarize(data=digest(data), quiet=args.quiet)

    output_data_path = (args.log_prefix_path /
                        input_data_path.stem).with_suffix(
                            constants.LOG_DATA_FORMAT_EXT)
    write_logs(logs, output_data_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_data', type=Path, required=True)
    parser.add_argument('--log_prefix_path',
                        type=Path,
                        required=True,
                        default='logs')
    parser.add_argument('--quiet',
                        action='store_true',
                        help='Do not print logs')

    args = parser.parse_args()
    run(args)
