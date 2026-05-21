# Deploy Prebuilt Binaries

The following prebuilt binaries are used for the eSD boot mode:

- `core-image-weston-smarc-rzg3e.rootfs.wic.bmap`: A map for the WIC
    image that speeds up flashing by detailing which SD Card blocks need
    data and which are empty.
- `core-image-weston-smarc-rzg3e.rootfs.wic.gz`: Compressed Linux disk
    image containing the partition table, bootloaders and rootfs (Linux
    kernel, drivers, applications and system configurations).

By using the eSD boot mode, the bootloaders are loaded directly from
the SD Card. **This means that there is no need to flash the
bootloaders to QSPI separately**.

The SD Card can be formatted using a Linux or Windows PC.

## Extract Package

=== "Linux PC"

    1. Copy `rzg3e-ethosu-v3.0_Prebuilt_Binaries.zip` file to Linux
        Host PC.
    1. Extract the zip file.

    ```bash
    unzip rzg3e-ethosu-v3.0_Prebuilt_Binaries.zip -d Prebuilt_Binaries
    ```

=== "Windows PC"

    1. Extract the zip file by right-clicking on
        `rzg3e-ethosu-v3.0_Prebuilt_Binaries.zip` file and selecting
        **Extract All**.

## Prepare SD Card

=== "Linux PC"

    1. Connect SD Card to Linux Host PC.

    1. Using **bmaptool**, write the WIC image to the SD Card (replacing /dev/sda with your SD Card device).

        ```bash
        sudo bmaptool copy --bmap Prebuilt_Binaries/Linux/core-image-weston-smarc-rzg3e.rootfs.wic.bmap Prebuilt_Binaries/Linux/core-image-weston-smarc-rzg3e.rootfs.wic.gz /dev/sda
        ```

    1. Make sure all of the data has been written to the SD Card.

        ```bash
        sync
        ```

    1. Eject and remove the SD Card from Linux Host PC.

    1. Connect the formatted SD Card to the uSD0 slot on the RZ/G3E.

=== "Windows PC"

    1. Connect SD Card to Windows PC.
    1. Using **balenaEtcher**, flash the SD Card with the
        `core-image-weston-smarc-rzg3e.rootfs.wic.gz` file found under the
        `Linux` directory in the package extracted in the previous step.
    1. Once the flash is completed, eject and remove the SD Card.
    1. Connect the SD Card to the uSD0 slot on the RZ/G3E.

## Boot Procedure

### Switch Settings

<figure>
  <img src="../../assets/images/esd-boot-switch.png"
       alt="SW_MODE Switch Bank">
  <figcaption>SW_MODE Switch Bank</figcaption>
</figure>

Set `SW_MODE` switch bank on the SMARC Carrier Board for eSD Boot.

!!! content-wrapper no-indent table-no-sort table-no-hover ""

    | Switch Bank |      SW1      |      SW2      |     SW3     |      SW4      |
    | :---------: | :-----------: | :-----------: | :---------: | :-----------: |
    |   SW_MODE   | ON {: .green} | ON {: .green} | OFF {:.red} | ON {: .green} |

### Setup U-Boot Environment

<figure>
  <img src="../../assets/images/uboot-hardware-setup.png"
       alt="U-Boot Hardware Setup">
  <figcaption>U-Boot Hardware Setup</figcaption>
</figure>

1. Start up a serial terminal connection (e.g. TeraTerm or Minicom)
    on Host PC, making sure the correct COM port and settings are used.

    !!! content-wrapper no-indent table-no-sort table-no-hover ""

        |   Variable   | Value               |
        | :----------: | :------------------ |
        |  Baud rate   | `#!bash 115200` bps |
        |     Data     | `#!bash 8 bit`      |
        |    Parity    | `#!bash none`       |
        |     Stop     | `#!bash 1 bit`      |
        | Flow control | `#!bash none`       |

1. Power **ON** the board by pressing the **POWER** button for at
    least 1 second until the **CARRIER ON** LED lights up.<br>The
    **CARRIER ON** LED is located above the **POWER** button.

1. Press any key to stop the autoboot within **3** seconds of U-Boot
    starting.<br>If U-Boot attempts to boot, press the **RESET** button
    and try again.

1. Set up the U-Boot environment.

    ```bash
    env default -a
    setenv bootargs 'console=ttySC0,115200 rw rootwait earlycon root=/dev/mmcblk0p2'
    setenv bootcmd 'mmc dev 0;ext4load mmc 0:2 0x48080000 /boot/Image;ext4load mmc 0:2 0x48000000 /boot/r9a09g047e57-smarc.dtb;booti 0x48080000 - 0x48000000'
    saveenv
    ```

1. Power **OFF** the board by pressing the **POWER** button for at
    least 1 second until the **CARRIER ON** LED turns off.<br>The
    **CARRIER ON** LED is located above the **POWER** button.

### Boot The Board

1. Whilst the board is not powered, confirm that following hardware
    configuration is being used.

    <figure>
    <img src="../../assets/images/esd-boot-hardware-setup.png"
    alt="Hardware Setup for eSD Boot">
    <figcaption>Hardware Setup for eSD Boot</figcaption>
    </figure>

1. Power **ON** the board by pressing the **POWER** button for at
    least 1 second until the **CARRIER ON** LED lights up.<br>The
    **CARRIER ON** LED is located above the **POWER** button.

    !!! note

        Since the U-Boot environment is saved, autoboot no longer needs
        to be stopped in the future.

1. Once Linux has booted up, login with `root` (no password).

    ```bash
    Poky (Yocto Project Reference Distro) 5.0.8 smarc-rzg3e ttySC0
    smarc-rzg3e login: root
    ```
