#!/usr/bin/python3

from datetime import datetime

def on_config(config, **kwargs):
    # Set copyright year
    year: str = str(datetime.now().year)
    config.copyright = config.copyright.format(year=year)
