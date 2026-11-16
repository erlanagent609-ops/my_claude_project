#!/bin/bash

# Nama sesi tmux
SESSION_NAME="agen_ecosystem"

# Cek apakah sesi sudah ada. Jika belum, buat baru.
tmux has-session -t $SESSION_NAME 2>/dev/null

if [ $0 != 0 ]; then
    # 1. Buat sesi baru dan jalankan Translator Agent di panel pertama (kiri/atas)
    tmux new-session -d -s $SESSION_NAME -n "Multi-Agent"
    tmux send-keys -t $SESSION_NAME:0.0 'cd ~/my_agent_home && echo "=== [ PANEL 1: TRANSLATOR AGENT ] ===" && python3 scripts/translator_wrapper.py "Ecosystem is starting up automatically."' C-m

    # 2. Belah layar secara vertikal (kanan) dan jalankan Weather / Debug Agent
    tmux split-window -h -t $SESSION_NAME:0.0
    tmux send-keys -t $SESSION_NAME:0.1 'cd ~/my_agent_home && echo "=== [ PANEL 2: WEATHER MONITOR ] ===" && python3 scripts/weather_fetcher.py Manado' C-m

    # 3. Fokus kembali ke panel pertama
    tmux select-pane -t $SESSION_NAME:0.0
fi

# Masuk/lampirkan ke sesi tmux tersebut
tmux attach-session -t $SESSION_NAME
