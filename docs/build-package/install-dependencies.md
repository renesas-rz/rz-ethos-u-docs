# Install Dependencies

By default, the **Docker** container engine will be used as the
Kas container engine, but **Podman** can also be used.

=== "Docker"

    To install the Docker container engine on the Linux Host PC:

    1. Add Docker's GPG Key.

        ```bash
        sudo apt-get update
        sudo apt-get install ca-certificates curl
        sudo install -m 0755 -d /etc/apt/keyrings
        sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
        sudo chmod a+r /etc/apt/keyrings/docker.asc
        ```

    1. Add official Docker repository to the APT sources.

        ```bash
        echo \
        "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
        $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
        sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
        sudo apt-get update
        ```

    1. Install Docker container engine packages.

        ```bash
        sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
        ```

    1. Add user to the Docker container engines user group.

        ```bash
        sudo groupadd docker
        sudo usermod -aG docker $USER
        ```

    1. Log out and log back in for the changes to take effect.

=== "Podman"

    To install Podman on the Linux Host PC:

    1. Install Podman.

        ```bash
        sudo apt update
        sudo apt-get install podman
        ```

    1. Set Podman as the Kas container engine.

        ```bash
        export KAS_CONTAINER_ENGINE=podman
        ```

    !!! warning

        Podman is not supported on Ubuntu 20.04 LTS or earlier.
