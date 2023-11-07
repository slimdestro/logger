# JSONAL (JSON as Log)
# Author: @slimdestro

import json
import os
from datetime import datetime
from flask import request, current_app
import inspect

class Helper_FlaskPOC_Custom_ErrorLogger:
    def __init__(self, app, log_path="error_log.json"):
        self.app = app
        self.log_path = log_path

        if not os.path.exists(self.log_path):
            with open(self.log_path, 'w') as log_file:
                json.dump({}, log_file)

        self.app.before_request(self.before_request)
        self.app.teardown_request(self.teardown_request)

    def get_current_directory_path(self): 
        frame_info = inspect.getouterframes(inspect.currentframe())[1]
        file_path = os.path.abspath(frame_info[1])
        return os.path.dirname(file_path)

    def log_error(self, method_name, input_data, error_msg):
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(self.log_path, 'r') as log_file:
            error_log = json.load(log_file)

        category = "Application_identifier"
        if category not in error_log:
            error_log[category] = {}

        if method_name not in error_log[category]:
            error_log[category][method_name] = []

        error_log[category][method_name].append({
            "log_trigger_path": self.get_current_directory_path(),
            "input": input_data,
            "error": error_msg,
            "timestamp": current_date
        })

        with open(self.log_path, 'w') as log_file:
            json.dump(error_log, log_file, indent=4)

    def before_request(self):
        pass

    def teardown_request(self, exception):
        if exception:
            method_name = request.endpoint
            input_data = request.values if request.method == 'GET' else request.json
            error_msg = str(exception)
            self.log_error(method_name, input_data, error_msg)