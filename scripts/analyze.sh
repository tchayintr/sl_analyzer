set -e

INPUT_DATA=data/best2010.sample20.seg.sl
LOG_PREFIX=logs/

python3 src/analyze.py \
        --input_data $INPUT_DATA \
        --log_prefix_path $LOG_PREFIX
        # --quiet
