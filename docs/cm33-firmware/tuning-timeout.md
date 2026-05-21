# Tuning Inference Timeout

## Overview

When using products with part numbers that include **#AC0** or
**#BC0**, the Ethos-U55 NPU may get stuck during inference. A timeout
mechanism has been added to prevent the firmware becoming unresponsive.
When the timeout is reached, the system will reset the NPU, cancel the
current inference, and return a failed status to Linux.

The default timeout is **500 ms**.

This value should be modified when using a model that takes longer than
500 ms for a single pure inference - this is the time for executing
inference on the Ethos-U55 NPU only and not the inference time recorded
in Linux.

## Environment Setup

!!! note

    The procedure documented in this page are done in a Windows
    environment. If using a different OS environment to run
    e2 studio, the appearance may look slightly different from the
    screenshots, but the steps still apply.

1. Download `e2studio` installer on the Host PC from
    [Renesas RZ FSP GitHub releases page](https://github.com/renesas/rz-fsp/releases).

1. After opening the page, locate the installer named
    `setup_rzfsp_v4_1_0_e2s_*` in the Assets section.

    1. Windows: file ending in `.exe`.
    1. Linux: file ending in `.run`.

1. Once the installer has been downloaded, run the file on the Host PC.

    1. On the setup page, please select `GNU ARM Embedded 13.3-Rel1`
        for `GCC Toolchains && Utilities`.

    <figure>
    <img src="../../assets/images/e2studio-installation.png"
    alt="e2studio Setup Page">
    <figcaption>e2studio Setup Page</figcaption>
    </figure>

1. Once the installation is completed, open e2studio.

1. Go to `File -> Import`, then select `Existing Projects into Workspace` and click `Next`.

    <figure>
    <img src="../../assets/images/e2studio-import-project.png"
    alt="e2studio Import Page">
    <figcaption>e2studio Import Page</figcaption>
    </figure>

1. Check the `Select archive file` option and enter the path to
    `e2studio_rzg3e-ethos-u-firmware_cm33_project.zip` file ensuring the
    project is selected in the `Projects` window, then click `Finish`.

    1. The project should now be visible in the `Project Explorer`
        located on the left side of the e2studio GUI.

    <figure>
    <img src="../../assets/images/e2studio-import-project-completed.png"
    alt="Importing Ethos-U Firmware Project In e2studio">
    <figcaption>Importing Ethos-U Firmware Project In e2studio</figcaption>
    </figure>

## Modifications To Firmware

1. On the top toolbar, select `Project -> C/C++ Project Settings`.

1. Under `C/C++ Build`, click \`Settings and modify the
    `ETHOSU_SEMAPHORE_WAIT_INFERENCE` macro to the preferred timeout
    value in milliseconds.

    <figure>
    <img src="../../assets/images/e2studio-timeout-configuration.png"
    alt="Changing Inference Timeout In e2studio">
    <figcaption>Changing Inference Timeout In e2studio</figcaption>
    </figure>

## Build Procedure

1. Right-click the project in the `Project Explorer` view and select
    `Build Project`.

1. Once the build is completed, messages like the ones seen in the
    image below will appear in the `console` window.

    <figure>
    <img src="../../assets/images/e2studio-build-firmware.png"
    alt="Build Firmware In e2studio">
    <figcaption>Build Firmware In e2studio</figcaption>
    </figure>

1. The built firmware file `rzg3e-ethos-u-firmware.elf` is generated
    in the `Debug` folder.

## Deploying Firmware

To deploy the built Ethos-U firmware onto the Linux rootfs, follow the
steps below.

=== "SD Card Boot"

    1. Power **OFF** the board if it is currently on.

    1. Remove the SD Card from the board and connect it to Linux
        Host PC.

    1. Copy the `rzg3e-ethos-u-firmware.elf` file from Windows PC to
        the home directory on the Linux Host PC.

    1. On the Linux Host PC, navigate to the SD Card's root directory.

    1. Copy the firmware file to the `/lib/firmware/` directory on the
        SD Card.

        ```bash
        sudo cp rzg3e-ethos-u-firmware.elf /media/user/root/lib/firmware/
        ```

    1. Make sure all of the data has been written to the SD Card.

        ```bash
        sync
        ```

    1. Eject and remove the SD Card from Linux Host PC.

    1. Connect the formatted SD Card to the uSD0 slot on the RZ/G3E.

    1. Finally, power **ON** on the board to load the updated firmware.

=== "Network Boot"

    1. Power **OFF** the board if it is currently on.

    1. Copy the `rzg3e-ethos-u-firmware.elf` file from Windows PC to
        the home directory on the Linux Host PC.

    1. On Linux Host PC, navigate to the TFTP or NFS root directory.

    1. Copy the firmware file to the `/lib/firmware` directory with
        that path.

        ```bash
        sudo cp rzg3e-ethos-u-firmware.elf /tftpboot/rzg3e/lib/firmware/
        ```

    1. Finally, power **ON** on the board to load the updated firmware.

## Viewing Logs

Once the updated firmware is deployed, the logs can be viewed from the
boards serial console using the following command:

```bash
cat /sys/kernel/debug/remoteproc/remoteproc0/trace0
```

This will print the logs stored in the remoteproc buffer.
Example log after boot-up:

```
[0.000] Info: Starting the Ethos-U firmware...
[0.002] Info: Initializing NPU: base_address=0x49c80000, fast_memory=0x0, fast_memory_size=0, secure=1, privileged=1
[0.003] Info: Soft reset NPU
[0.005] Info: New NPU driver registered (handle: 0x0x80089248, NPU: 0x0x49c80000)
[0.005] Info: Initializing the Ethos-U remoteproc...
[0.007] Debug [remoteproc.cpp:init:124]:
[0.008] Debug [remoteproc.cpp:RProc:66]: setting up resource table
[0.010] Debug [remoteproc.cpp:RProc:67]: rsc_addr=0x80087B90, tableSize=233
[0.012] Debug [remoteproc.cpp:RProc:74]: setting up vdev
[0.013] Debug [remoteproc.cpp:RProc:81]: creating notify task
[0.015] Debug [remoteproc.cpp:notifyTask:110]: Starting message notify task
[0.016] Info: Initializing the Ethos-U Message Handler...
[0.018] Debug [remoteproc.cpp:notify:158]:
```
