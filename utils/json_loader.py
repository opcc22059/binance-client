# -*- coding: utf-8 -*-
import json
from pathlib import Path
import os

from binance_client import settings

class JsonLoader():
    # xxxPath.xxxFile without json return python object
    # xxxPath.xxxFile.json return file content

    data : dict[str, str]= {}

    def getConst(self, scan_path_list: list[str], key_ignore_pattern=''):
        """
        scan_path_list rel to src dir
        """

        scan_path_set = set(scan_path_list)

        SRC_DIR = settings.BASE_DIR
        src_path = Path(SRC_DIR)
        for scan_path in scan_path_set:
            # print('scan_path: ', scan_path)
            # print('src_path: ', src_path)
            for path in src_path.rglob(os.path.join(scan_path, '**/*.json')):
                # print('path: ', path)
                relpath = str(path.parent).replace(str(src_path), '')[1:]
                if not relpath.endswith('/'):
                    relpath = relpath + '/'
                config_key = relpath.replace(key_ignore_pattern, '').replace(os.path.sep, '.') + path.stem
                file_key = relpath.replace(key_ignore_pattern, '').replace(os.path.sep, '.') + path.name
                with open(path, 'r') as f:
                    self.data[config_key] = json.loads(f.read())
                    self.data[file_key] = json.dumps(self.data[config_key])

        return self.data
