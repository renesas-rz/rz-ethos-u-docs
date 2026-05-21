# RZ Ethos-U Documentation

This is repository contains the documentation sources for RZ Ethos-U
Documentation MkDocs site.

## Building the documentation locally

1. Create a virtual environment (optional but recommended)

    ```bash
    python3 -m venv venv && source venv/bin/activate
    ```

1. Install dependencies

    ```bash
    pip install -r requirements.txt
    ```

1. Serve locally with hot reload

    ```bash
    mkdocs serve -a 0.0.0.0:8000
    ```

1. Build static site

    ```bash
    mkdocs build
    ```

The site will be generated in the `site/` directory.

## License

This repository is licensed under the terms of the CC BY 4.0 license
(please see file [LICENSE](/LICENSE) in this directory for further details).
