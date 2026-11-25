# Overview on the Renesas RZ/G3E NPU solution

- Applications running in Linux can trigger inference to be run on the
    Arm Ethos-U55 NPU directly.
    - Operators that cannot run on the NPU will be offloaded
        to TensorFlow Lite on the Arm Cortex-A55 core.
- Prebuilt binaries are available to speed up evaluation.
- Includes the Arm `delegate_runner` and TensorFlow Lite
    `benchmark_model` applications for generic model validation and
    benchmarking, detailed
    [HERE](getting-started/third-party-applications.md).
- The package is split into three OpenEmbedded/Yocto layers based on the
    [Renesas BSP-4.0.2](https://github.com/renesas-rz/meta-renesas/tree/BSP-4.0.2):
    - `meta-rz-ethos-u`: Adds support for the Arm Ethos-U Linux
        Driver Stack v26.08, Ethos-U Mainline Linux driver and
        Arm Ethos-U Vela Compiler v5.2.0.
    - `meta-rz-ethos-u-examples`: provides example Ethos-U applications
        (MobileNet V2 Classifier and Model Executor) that can run on
        the RZ/G3E SMARC EVK, along with their required dependencies
        (OpenCV and XDG shell protocol for Wayland).
    - `meta-rz-ethos-u-demos`: Adds demo applications (e.g., Image
        Classification). This is provided as a separate repository
        to `rz-ethos-u`.
- Model compilation can be done on-device or on a Linux Host PC.
    - The [Arm Ethos-U Vela Compiler v5.2.0](https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/tree/5.2.0)
        is used to compile TensorFlow Lite models.
    - Detailed information about model compilation can be found
        [HERE](prepare-models/compile-models.md).

The diagram below illustrates the architecture of the RZ/G3E Ethos-U
software stack:

<figure>
  <img src="../assets/images/package-architecture.png"
       alt="Package Architecture">
  <figcaption>Package Architecture</figcaption>
</figure>

## Supported Models

INT8, UINT8 and FLOAT32 TensorFlow Lite (`.tflite`) networks provided
to the Arm Ethos-U Vela Compiler.

!!! note

    Models with all Float32 operators will be completely offloaded to
    TensorFlow Lite on the Cortex-A55 core.
