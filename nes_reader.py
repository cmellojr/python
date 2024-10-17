with open('super_mario_3.nes', 'rb') as f:
    header = f.read(16)

if header[:4] != b'NES\x1a':
    print('Arquivo inválido.')
    exit()

num_prg_banks = header[4]
num_chr_banks = header[5]
mirroring = 'Vertical' if header[6] & 0b1 else 'Horizontal'
mapper = (header[7] & 0xf0) | (header[6] >> 4)
prg_ram = bool(header[6] & 0b10000)
four_screen_vram = bool(header[6] & 0b100000)
ntsc = bool(header[9] & 0b100)
title_screen = bool(header[10] & 0b10)
bus_conflict = bool(header[10] & 0b100)

print(f'Número de bancos PRG: {num_prg_banks}')
print(f'Número de bancos CHR: {num_chr_banks}')
print(f'Mirroring: {mirroring}')
print(f'Mapper: {mapper}')
print(f'Backup de PRG RAM: {prg_ram}')
print(f'VRAM de quatro telas: {four_screen_vram}')
print(f'Formato de vídeo: {"NTSC" if ntsc else "PAL"}')
print(f'Tela de título suportada: {title_screen}')
print(f'Conflito de barramento suportado: {bus_conflict}')

