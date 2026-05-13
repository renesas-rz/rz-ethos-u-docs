# Environment Setup

RUHMI can be installed either:

1. Natively on a Linux Host PC.
1. Using a Docker container.

The [RUHMI Framework RZ/G GitHub repository](https://github.com/renesas/ruhmi-framework-rzg/tree/main)
provides the [Dockerfile](https://github.com/renesas/ruhmi-framework-rzg/blob/115a747a80193ce609d221235988cbd9fa784a27/scripts/Dockerfile)
to be used.

The following instructions assumes that the `ruhmi-framework-rzg`
GitHub repository has been cloned to to `~/ruhmi-framework-rzg`.

!!! note

    The RUHMI build environment is compatible with Ubuntu 22.04 LTS and
    newer.<br>Older systems may result in compatibility issues during RUHMI
    installation.

=== "Native installation"

    To install RUHMI natively, install the following packages.

    ```bash
    cd ~/ruhmi-framework-rzg/scripts/
    sudo apt-get update
    sudo apt install -y build-essential ca-certificates cmake file software-properties-common tree unzip wget
    sudo add-apt-repository -y ppa:ubuntu-toolchain-r/test && sudo apt-get update
    sudo apt-get install libdnnl-dev libgoogle-glog-dev libstdc++6 python3.10 python3.10-dev python3.10-venv python3-pip
    wget https://github.com/renesas/ruhmi-framework-rzg/raw/62295b271f4b0b90ddd676f799f00d7ad4a7adf6/install/mera-2.5.0+pkg.3782-cp310-cp310-manylinux_2_27_x86_64.whl
    python3 -m pip install mera-2.5.0+pkg.3782-cp310-cp310-manylinux_2_27_x86_64.whl
    python3 -m pip install --upgrade pip
    python3 -m pip install tensorflow==2.17.0 ethos-u-vela==4.0.0
    python3 -m pip install ai-edge-litert==2.1.2
    ```

=== "Docker environment installation"

    Using the provided Dockerfile, build and run it with Docker.

    ```bash
    cd ~/ruhmi-framework-rzg/scripts/
    sudo docker build --build-arg UID=$(id -u) --build-arg GID=$(id -g) -t ruhmi-env
    sudo docker run --rm -it -v /path/to/shared:/shared -w /shared ruhmi-env
    ```

    !!! note

        Update `/path/to/shared` path to the directory used for
        storing models.

    The console should appear with user `user` and a different hostname
    as shown below.

    ```bash
    user@5c0832859d04:/shared$
    ```
