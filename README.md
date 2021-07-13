# SL (sentence line) Analyzer
#### _sl_analyzer_

A tool for analyzing segmented sentences in sl format.

#### Data formats
- **sl**: sentence line

#### Usage
```
usage: analyze.py [-h] --input_data INPUT_DATA --log_prefix_path LOG_PREFIX_PATH [--quiet]

optional arguments:
  -h, --help            show this help message and exit
  --input_data INPUT_DATA
  --log_prefix_path LOG_PREFIX_PATH
  --quiet               Do not print logs
```

#### Example outputs
```
### report
# sent: 20 ...
# word: 656 ...
# char: 2531 ...
# words/sent: min=1 max=76 avg=32.8
# chars/sent: min=2 max=332 avg=126.55
# chars/word: min=1 max=22 avg=3.8582317073170733
```
