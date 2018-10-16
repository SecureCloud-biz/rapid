"""
 Copyright (c) 2015 Michael Bright and Bamboo HR LLC

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

 http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""

import glob
import logging

from flask import Flask
from flask.wrappers import Response
import subprocess


app = Flask("rapidci_logger")
app.rapid_config = {'_is': 'logger'}

UWSGI = False
try:
    import uwsgi
    UWSGI = True
except ImportError:
    pass


def setup_logging(flask_app):
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    flask_app.logger.addHandler(handler)
    flask_app.logger.setLevel(logging.INFO)

    logger = logging.getLogger('rapid')
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)


def configure_application(flask_app, args):
    setup_logging(flask_app)
    from rapid.lib.LogServer import LogServer
    log_server = LogServer(args.log_dir)
    log_server.configure_application(flask_app)
