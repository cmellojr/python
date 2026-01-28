#!/usr/bin/env python3

import mmap, time

MB = 50000
PAGE = 4096

size = MB * 1024 * 1024

try:
    mm = mmap.mmap(-1, size, access=mmap.ACCESS_WRITE)
    mv = memoryview(mm)
    for i in range(0, size, PAGE):
        mv[i] = (mv[i] + 1) % 256

    while True:
        time.sleep(3000)
except MemoryError:
    raise SystemExit(1)

# Antes de rodar, aumentar swap

# sudo fallocate -l 60G /swapfile
# sudo chmod 600 /swapfile
# sudo mkswap /swapfile
# sudo swapon /swapfile).

# Executar: python3 alloc_mem.py