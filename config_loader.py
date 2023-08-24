from typing import MutableMapping

import tomlkit


def load_config(path_to_config: str = 'config.toml') -> MutableMapping:
    with open(path_to_config, mode="rt", encoding="utf-8") as fp:
        ...
        config = tomlkit.load(fp)

    return config
