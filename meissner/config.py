"""
                                       .@@#

    (@&*%@@@/,%@@@#       #&@@@@&.     .@@#     /&@@@@&*     /&@@@@&*     (@&*%@@@(       *%@@@@&/     .@@&*&@.
    (@@&((&@@@(/&@@,     #@@#/(&@@.    .@@#    #@@(///(,    .@@%////,     (@@&(/#@@#     #@@&//#@@(    .@@@@@%.
    (@@.  /@@*  ,@@/    .&@@%%%&@@*    .@@#    (@@&&%#*     .@@@&%#/      (@@.  .&@%     &@@&%%%@@%    .@@@
    (@@.  /@@,  ,@@/    .&@%,,,,,,     .@@#     ./#%&@@&.    ./(%&@@&.    (@@.  .&@%     &@@/,,,,,.    .@@@
    (@@.  /@@,  ,@@/     #@@#////*     .@@#    ./////&@@.    /////&@@.    (@@.  .&@%     #@@&/////.    .@@@
    (@@.  /@@,  ,@@/      #&@@@@@%     .@@#    ,&@@@@@%.     &@@@@@&.     (@@.  .&@%      *%@@@@@&*    .@@@


    MIT License

    Copyright (c) 2017 epsimatt (https://github.com/epsimatt/meissner)

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
"""

from meissner import __root_dir__

import json
import logging
import os.path

log = logging.getLogger(__name__)

class ConfigManager:
    _config_path = __root_dir__ + 'config.json'

    _config = {}

    def __init__(self):
        # Generate a new config.json file if it does not exist
        if not os.path.exists(self._config_path) or os.path.getsize(self._config_path) == 0:
            with open(self._config_path, 'w', encoding = 'utf8') as file:
                json.dump(
                    {
                        'prefix': '!~',
                        'discord_token': 'unknown',
                        'naver_client_id': 'unknown',
                        'naver_client_secret': 'unknown',
                        'oxford_app_id': 'unknown',
                        'oxford_app_key': 'unknown'
                    },
                    file,
                    ensure_ascii = False,
                    indent = 4
                )

            log.info("Created a new configuration file for meissner.")
            log.info("Please set up the config.json file.")

            raise SystemExit

        with open(self._config_path) as file:
            self._config = json.load(file)

        log.debug("Loaded config.json successfully: {}" . format(self._config))

    def get(self, key):
        try:
            return self._config[key]
        except KeyError:
            return None
