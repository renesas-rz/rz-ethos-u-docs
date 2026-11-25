# How To Build The Package

These pages detail the procedure that can be used to build the
binaries from the RZ Ethos-U project.

!!! info

    The [RZ Ethos-U repository](https://github.com/renesas-rz/rz-ethos-u)
    contains two OpenEmbedded/Yocto meta-layers based on the
    [Renesas BSP-4.0.2](https://github.com/renesas-rz/meta-renesas/tree/BSP-4.0.2).

    The `meta-rz-ethos-u` meta-layer adds support for the Arm Ethos-U
    Linux Driver Stack v26.08 (Delegate library, delegate_runner
    application), the Ethos-U Mainline Linux driver, TensorFlow Lite
    v2.20 (libraries and benchmark_model application), Arm Ethos-U Vela
    Compiler v5.2.0 on top of the Renesas BSP for the RZ/G3E SMARC EVK.
    This enables Ethos-U functionality and allows the Ethos-U55 NPU to be
    controlled directly by Linux on the Cortex-A55 core.

    The `meta-rz-ethos-u-examples` meta-layer provides example Ethos-U
    applications (MobileNet V2 Classifier and Model Executor) that can
    run on the RZ/G3E SMARC EVK, along with their required dependencies
    (OpenCV and XDG shell protocol for Wayland).

    Ethos-U demo applications are provided by the separate
    [meta-rz-ethos-u-demos](https://github.com/renesas-rz/meta-rz-ethos-u-demos)
    layer, which is dependent on `meta-rz-ethos-u`.

The repository is set up to be built with the Kas tool,
which automatically downloads and configures all required dependencies
for the user. It contains a `kas-container` script which is a wrapper
to run Kas inside a build container.

Using the `kas-container` script, the Yocto image can be built by
**2** methods:

1. **Kas Menu**: Allows users to configure different build options
    using a Graphical User Interface (GUI).
1. **Kas Configuration Fragments**: Configuration fragments are daisy
    chained via command-line.

For more information on Kas, please visit the
[Kas documentation site](https://kas.readthedocs.io/en/4.5/userguide.html).
