# Deploy Binaries

The following binaries are used for the Network boot mode:

- `bl2_bp_spi-smarc-rzg3e.srec`: Bootloader for SPI memory that
    initializes the hardware components needed to run U-Boot.
- `fip-smarc-rzg3e.srec`: Firmware package that bundles U-Boot and
    other secure components into one boot image.
- `Flash_Writer_SCIF_RZG3E_EVK_LPDDR4X.mot`: Software that is loaded into
    the RZ/G3Es RAM to write bootloader files into flash memory.

=== "core-image-minimal"

    - `core-image-minimal-smarc-rzg3e.rootfs.tar.gz`: Compressed Linux
        disk image containing the rootfs (Linux kernel, drivers,
        applications and system configurations).

=== "core-image-weston"

    - `core-image-weston-smarc-rzg3e.rootfs.tar.gz`: Compressed Linux disk
        image containing the rootfs (Linux kernel, drivers, applications and
        system configurations).

By using the Network boot mode, the bootloaders need to be manually
flashed to the board.

## Prepare Linux Host PC

=== "Prebuilt Binaries"

    1. Copy `rzg3e-ethosu-v3.0_Prebuilt_Binaries.zip` file to Linux
        Host PC.

    1. Extract the zip file.

        ```bash
        unzip rzg3e-ethosu-v3.0_Prebuilt_Binaries.zip -d Prebuilt_Binaries
        ```

    1. Copy `core-image-weston-smarc-rzg3e.rootfs.tar.gz` file to a
        new directory in the TFTP/NFS directory.

        ```bash
        cp Prebuilt_Binaries/core-image-weston-smarc-rzg3e.rootfs.tar.gz /tftpboot/rzg3e/
        ```

    1. Navigate to TFTP/NFS directory and extract the tarball.

        ```bash
        cd /tftpboot/rzg3e/
        tar xf core-image-weston-smarc-rzg3e.rootfs.tar.gz
        ```

=== "Manual Build Binaries"

    === "core-image-minimal"

        1. Copy `core-image-minimal-smarc-rzg3e.rootfs.tar.gz` file
           under `build/tmp/deploy/images/smarc-rzg3e/` to a new
           directory in the TFTP/NFS directory.

        1. Navigate to TFTP/NFS directory and extract the tarball.

           ```bash
           cd /tftpboot/rzg3e/
           tar xf core-image-minimal-smarc-rzg3e.rootfs.tar.gz
           ```

    === "core-image-weston"

        1. Copy `core-image-weston-smarc-rzg3e.rootfs.tar.gz` file
           under `build/tmp/deploy/images/smarc-rzg3e/` to a new
           directory in the TFTP/NFS directory.

        1. Navigate to TFTP/NFS directory and extract the tarball.

           ```bash
           cd /tftpboot/rzg3e/
           tar xf core-image-weston-smarc-rzg3e.rootfs.tar.gz
           ```

## Prepare Bootloaders

=== "Linux PC"

    1. Copy bootloader files under
        `build/tmp/deploy/images/smarc-rzg3e` to the directory used for
        loading bootloader files.
        1. `bl2_bp_spi-smarc-rzg3e.srec`
        1. `fip-smarc-rzg3e.srec`
        1. `Flash_Writer_SCIF_RZG3E_EVK_LPDDR4X.mot`

=== "Windows PC"

    1. Copy bootloader files under
        `build/tmp/deploy/images/smarc-rzg3e` on Linux Host PC to Windows
        PC.
        1. `bl2_bp_spi-smarc-rzg3e.srec`
        1. `fip-smarc-rzg3e.srec`
        1. `Flash_Writer_SCIF_RZG3E_EVK_LPDDR4X.mot`

## Write Bootloaders to SPI Flash

<figure>
  <img src="../../assets/images/network-boot-switch-scif.png"
       alt="SW_MODE Switch Bank">
  <figcaption>SW_MODE Switch Bank</figcaption>
</figure>

1. Set `SW_MODE` switch bank on the SMARC Carrier Board to SCIF
    Download Mode.

    !!! content-wrapper no-indent table-no-sort table-no-hover ""

        | Switch Bank |     SW1      |      SW2      |     SW3      |      SW4      |
        | :---------: | :----------: | :-----------: | :----------: | :-----------: |
        |   SW_MODE   | OFF {: .red} | ON {: .green} | OFF {: .red} | ON {: .green} |

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

    1. The following message should be printed to console.

        ```
        SCI Download mode (Normal SCI boot)

        -- Load Program to SRAM  ---------------
        ```

1. Send the `Flash_Writer_SCIF_RZG3E_EVK_LPDDR4X.mot` file. If
    successful, the serial console should print the product code.

    ```
    Flash writer for RZ/G3E Series V0.91 May.15,2024
     Product Code : RZ/G3E
    ```

1. Write BL2 Loader to memory.

    ```
    >xls2
    ===== Qspi writing of RZ/G3S Board Command =============
    Load Program to Spiflash
    Writes to any of SPI address.
     Dialog : AT25QL128A
    Program Top Address & Qspi Save Address
    ===== Please Input Program Top Address ============
      Please Input : H'8003600
    ===== Please Input Qspi Save Address ===
      Please Input : H'0
    please send ! ('.' & CR stop load)
    Erase SPI Flash memory...
    Erase Completed
    Write to SPI Flash memory.
    ======= Qspi  Save Information  =================
     SpiFlashMemory Stat Address : H'00000000
     SpiFlashMemory End Address  : H'00032D6F
    ===========================================================
    ```

1. Send the `bl2_bp_spi-smarc-rzg3e.srec` file.

1. Write FIP Loader to memory.

    ```
    >xls2
    ===== Qspi writing of RZ/G3S Board Command =============
    Load Program to Spiflash
    Writes to any of SPI address.
     Dialog : AT25QL128A
    Program Top Address & Qspi Save Address
    ===== Please Input Program Top Address ============
      Please Input : H'0
    ===== Please Input Qspi Save Address ===
      Please Input : H'60000
    please send ! ('.' & CR stop load)
    Erase SPI Flash memory...
    Erase Completed
    Write to SPI Flash memory.
    ======= Qspi  Save Information  =================
     SpiFlashMemory Stat Address : H'00060000
     SpiFlashMemory End Address  : H'00115CBE
    ===========================================================
    ```

1. Send the `fip-smarc-rzg3e.srec` file.

1. Power **OFF** the board by pressing the **POWER** button for at
    least 1 second until the **CARRIER ON** LED turns off.<br>The
    **CARRIER ON** LED is located above the **POWER** button.

## Boot Procedure

### Switch Settings

<figure>
  <img src="../../assets/images/network-boot-switch.png"
       alt="SW_MODE Switch Bank">
  <figcaption>SW_MODE Switch Bank</figcaption>
</figure>

Set `SW_MODE` switch bank on the SMARC Carrier Board for QSPI Boot.

!!! content-wrapper no-indent table-no-sort table-no-hover ""

    | Switch Bank |     SW1      |     SW2      |     SW3      |      SW4      |
    | :---------: | :----------: | :----------: | :----------: | :-----------: |
    |   SW_MODE   | OFF {: .red} | OFF {: .red} | OFF {: .red} | ON {: .green} |

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
    setenv ipaddr '192.168.1.2'
    setenv serverip '192.168.1.1'
    setenv ethaddr '00:11:22:33:44:55'
    setenv bootcmd 'tftp 0x48080000 rzg3e/boot/Image; tftp 0x48000000 rzg3e/boot/r9a09g047e57-smarc.dtb; booti 0x48080000 - 0x48000000'
    setenv bootargs 'console=ttySC0,115200 debug rootwait root=/dev/nfs rw nfsroot=192.168.1.1:/tftpboot/rzg3e,v3 ip=192.168.1.2:::::eth0:off'
    saveenv
    ```

    !!! note

        The IP/MAC addresses should be set up according to the Linux Host PCs environment.

1. Power **OFF** the board by pressing the **POWER** button for at
    least 1 second until the **CARRIER ON** LED turns off.<br>The
    **CARRIER ON** LED is located above the **POWER** button.

### Boot The Board

1. Whilst the board is not powered, confirm that following hardware
    configuration is being used.

    <figure>
    <img src="../../assets/images/network-boot-hardware-setup.png"
    alt="Hardware Setup for Network Boot">
    <figcaption>Hardware Setup for Network Boot</figcaption>
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
