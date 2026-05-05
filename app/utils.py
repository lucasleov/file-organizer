from pathlib import Path

def caminho_existe(caminho):
    return Path(caminho).exists()
