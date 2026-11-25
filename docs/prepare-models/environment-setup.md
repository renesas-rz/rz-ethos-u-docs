# Environment Setup

Model compilation can either be done:

1. Offline (on a Linux Host PC).
1. On device (directly on RZ/G3E SMARC EVK).

=== "Offline compilation"

    The RZ Ethos-U project provides a `requirements.txt` file
    under `rz-ethos-u/scripts/vela`, which can be used to install all
    dependencies in a Python Virtual Environment.

    To set up the offline compilation environment, prepare and install the
    Python Virtual Environment.

    ```bash
    cd ~/rz-ethos-u/scripts/vela/
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

=== "On device compilation"

    The only requirement for on device compilation is that the RZ/G3E
    SMARC EVK is booted up using the RZ Ethos-U software either from
    the prebuilt binaries or a manual build.
