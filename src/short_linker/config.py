import os

from dynaconf import Dynaconf

from short_linker.constants import CONFIG_ROOT_DIR

if not os.path.exists(CONFIG_ROOT_DIR):
    raise FileNotFoundError('Не найдена директория для конфигурационных файлов!')

settings = Dynaconf(
    root_path=CONFIG_ROOT_DIR,
    settings_files=["config.toml"],
)
