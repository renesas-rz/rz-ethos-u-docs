# How To Build The Package

These pages detail the procedure that can be used to build the
binaries from the Linux source package.

!!! info

    The Linux source package (rz-ethos-u) contains the OpenEmbedded/Yocto
    meta-layer based on the
    [Renesas RZG3E-BSP-1.0.0](https://github.com/renesas-rz/meta-renesas/tree/RZG3E-BSP-1.0.0).

    The meta-layer adds support for the Arm Ethos-U Linux Driver Stack
    v24.08, relevant Linux kernel drivers, EdgeCortix MERA runtime
    library and sample applications on top of the Renesas BSP for the
    RZ/G3E SMARC EVK.

    This enables Ethos-U functionality for both Linux and
    the Arm Cortex-M33 core.

    The source code (`rz-ethos-u-v3.0.zip`) can be found in the
    `Linux_Source_Package.zip` release package.

The Linux source package is set up to be built with the Kas tool,
which automatically downloads and configures all required dependencies
for the user. The **rz-ethos-u** source code contains a
`kas-container` script which is a wrapper to run Kas inside a build
container.

Using the `kas-container` script, the Yocto image can be built by
**2** methods:

1. **Kas Menu**: Allows users to configure different build options
    using a Graphical User Interface (GUI).
1. **Kas Configuration Fragments**: Configuration fragments are daisy
    chained via command-line.

[:link: More Information On Kas](https://kas.readthedocs.io/en/4.5/userguide.html){ .md-button .md-button--primary }
