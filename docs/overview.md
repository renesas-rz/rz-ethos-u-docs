# Overview on the Renesas RZ/G3E NPU solution

- Applications running in Linux can trigger inference to be run on the
    Arm Ethos-U55 NPU and Arm Cortex-M33 core.
    - Operators that are unable to be run on the NPU will be offloaded
        to the Cortex-M33 during compilation stage.
- Prebuilt binaries available to speed-up evaluation.
- OpenEmbedded/Yocto layer provided that adds supports for the Arm
    Linux Driver Stack v24.08, EdgeCortix MERA runtime library and sample
    applications.
    - This is based on the [Renesas RZG3E-BSP-1.0.0](https://github.com/renesas-rz/meta-renesas/tree/RZG3E-BSP-1.0.0).
- Docker Environment provided with functionality to automatically
    generate runtime data for all provided target models.
    - The [Renesas RUHMI Framework AI Compiler](https://github.com/renesas/ruhmi-framework-rzg/tree/main)
        is used to compile AI models into data used by the MERA runtime
        library.
    - MERA runtime library is used to interact with the Ethos-U
        libraries to run an AI inference.
    - Detailed information about model compilation can be found
        [HERE](prepare-models/index.md).

The diagram below illustrates the architecture of the RZ/G3E Ethos-U
software stack:

<figure>
  <img src="../assets/images/package-architecture.png"
       alt="Package Architecture">
  <figcaption>Package Architecture</figcaption>
</figure>

## Supported Models

Optimized networks generated using the RUHMI Framework AI Compiler,
with a file size up to **16MB**.
