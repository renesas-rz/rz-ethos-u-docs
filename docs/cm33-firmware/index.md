# Cortex-M33 Core Firmware

The firmware deployed on the Arm Cortex-M33 core includes support for
the Arm Ethos-U software stack v24.08, which contains software
components (e.g. Arm Ethos-U driver, TensorFlow Lite Micro, Arm
CMSIS-NN and RPMsg). It passively listens for communication from Linux
and responds to Ethos-U NPU related requests, including communication
checks (e.g. ping), capability queries and inference execution.

When an inference request arrives from Linux (Cortex-A55 core) over
RPMsg:

1. The firmware reads the model and input data from a shared memory
    region set up by Linux.
1. Creates and initializes the TensorFlow Lite Micro interpreter.
1. Triggers inference execution.
    1. The Ethos-U custom operators (`ethos-u`) are offloaded to the
        Ethos-U55 NPU.
    1. Other operators that were not offloading during compilation
        are executed on the Cortex-M33 core using CMSIS-NN or TFLite Micro
        reference kernels depending on operator support.
1. Once inference has completed, the firmware will write the results
    to shared memory and notifies Linux over RPMsg.

!!! note

    The firmware is already included in the rootfs as part of the
    Linux source package.

    An update to the firmware file is only required when enabling
    logging or modifying the source code.
