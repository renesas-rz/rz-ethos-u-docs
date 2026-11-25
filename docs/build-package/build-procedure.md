# Build Procedure

Clone the [RZ Ethos-U repository](https://github.com/renesas-rz/rz-ethos-u)
to prepare the `rz-ethos-u` directory.

```bash
git clone https://github.com/renesas-rz/rz-ethos-u.git
cd rz-ethos-u/
```

=== "Build Using Kas Menu"

    1. In the project directory, load the Kas Menu.

        ```bash
        ./kas-container menu
        ```

        <figure>
        <img src="../../assets/images/kas-menu.png"
        alt="Kas Menu Screen">
        <figcaption>Kas Menu Screen</figcaption>
        </figure>

    1. Select the build configuration.

        - Using the (↑/↓) arrow keys, navigate between the `Target`,
            `Machine` and `Features` options.
        - The spacebar/enter buttons can be used to select an option.
        - To switch and control the bottom red options, either use
            the (←/→) arrow keys or the tab key.

        !!! tip

            For building **core-image-minimal**, select the following
            option only:

            - Target = core-image-minimal

            For building **core-image-weston with graphics and video
            codec support**, select the following options:

            - Target = core-image-weston
            - Features = Graphics
            - Features = Codecs

            To install the Renesas example applications, select
            the following option in addition to other options:

            - Features = Example Ethos-U Applications

            To install the Renesas demo applications, select
            the following option in addition to other options:

            - Features = Demo Ethos-U Applications

    1. Once the configuration has been selected, the build can be
        kicked off immediately by selecting the `Build` option.

    1. Or the configuration can be saved using the `Save & Exit`
        option.

    If the configuration is saved, there are **2** ways to start a
    build using the generated configuration.

    1. **Interactive build**: Kas opens a shell within its build
        environment, already configured to use bitbake.

        ```bash
        ./kas-container shell
        ```

    1. **Non-interactive build**: Immediately starts the build.

        ```bash
        ./kas-container build
        ```

=== "Build Using Kas Configuration Fragments"

    The following Kas configuration fragments are supplied in the
    rz-ethos-u project.

    | Configuration File                  | Purpose                                                                  |
    | ----------------------------------- | ------------------------------------------------------------------------ |
    | `kas/base.yml`                      | Base configuration used by the project.                                  |
    | `kas/images/core-image-minimal.yml` | Configuration for building core-image-minimal.                           |
    | `kas/images/core-image-weston.yml`  | Configuration for building core-image-weston.                            |
    | `kas/machines/smarc-rzg3e.yml`      | Configuration for building smarc-rzg3e.                                  |
    | `kas/features/codecs.yml`           | Enables H.264 and H.265 video codec library support.                     |
    | `kas/features/ethos-u-examples.yml` | Enables example Ethos-U application support.                             |
    | `kas/features/ethos-u-demos.yml`    | Enables demo Ethos-U application support (fetches meta-rz-ethos-u-demos) |
    | `kas/features/graphics.yml`         | Enables graphics library support.                                        |

    === "core-image-minimal"

        To build image:

        ```bash
        ./kas-container build --update --force-checkout "kas/base.yml:kas/images/core-image-minimal.yml:kas/machines/smarc-rzg3e.yml"
        ```

    === "core-image-weston (without codecs/graphics libraries)"

        To build image:

        ```bash
        ./kas-container build --update --force-checkout "kas/base.yml:kas/images/core-image-weston.yml:kas/machines/smarc-rzg3e.yml"
        ```

    === "core-image-weston (with codecs/graphics libraries)"

        To build image:

        ```bash
        ./kas-container build --update --force-checkout "kas/base.yml:kas/images/core-image-weston.yml:kas/machines/smarc-rzg3e.yml:kas/features/codecs.yml:kas/features/graphics.yml"
        ```

    === "core-image-weston (with codecs/graphics libraries and example applications)"

        To build image:

        ```bash
        ./kas-container build --update --force-checkout "kas/base.yml:kas/images/core-image-weston.yml:kas/machines/smarc-rzg3e.yml:kas/features/codecs.yml:kas/features/graphics.yml:kas/features/ethos-u-examples.yml"
        ```

    === "core-image-weston (with codecs/graphics libraries and demo applications)"

        To build image:

        ```bash
        ./kas-container build --update --force-checkout "kas/base.yml:kas/images/core-image-weston.yml:kas/machines/smarc-rzg3e.yml:kas/features/codecs.yml:kas/features/graphics.yml:kas/features/ethos-u-demos.yml"
        ```
