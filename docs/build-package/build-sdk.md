# Build SDK

The SDK is needed to cross-compile applications that can be run using
the Linux rootfs on the RZ/G3E. This Yocto package provides a way to
build the SDK and generate the installer for x86_64.

Run the following build command.

=== "Interactive Kas Build"

    === "core-image-minimal"

        ```bash
        bitbake core-image-minimal -c populate_sdk
        ```

    === "core-image-weston"

        ```bash
        bitbake core-image-weston -c populate_sdk
        ```

=== "Non-Interactive Kas Build"

    ```bash
    ./kas-container build --–cmd populate_sdk
    ```
