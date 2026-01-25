#!/bin/bash

BASE_DIR="$HOME/Documents/Programming/Python/SMTP/send_new_english_words"
LOG_DIR="$BASE_DIR/bash/logs"
LOG_ARQ="$LOG_DIR/logs_email_monitoring.txt"
DATE=$(date +"%Y-%m-%d %H:%M:%S")

mkdir -p "$LOG_DIR"
touch "$LOG_ARQ"

python3 "$BASE_DIR/send_email.py"
STATUS=$?

if [ $STATUS -eq 0 ]; then
    echo "[$DATE] INFO: Processo executado com sucesso" >> "$LOG_ARQ"
else
    echo "[$DATE] ERROR: Falha ao executar o processo (API fora ou erro interno)" >> "$LOG_ARQ"
fi
