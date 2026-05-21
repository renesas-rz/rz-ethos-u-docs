# Binaries Location

## Linux Binaries

Built image binaries will be located under
`build/tmp/deploy/images/smarc-rzg3e/` in the project directory.

The table below breaks down the necessary binaries needed for specific
boot methods.

=== "core-image-minimal"

    | File                                             | Description                                                                                                                                                     |      eSD Boot      |    Network Boot    |
    | ------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------: | :----------------: |
    | `bl2_bp_spi-smarc-rzg3e.srec`                    | Bootloader for SPI memory that initializes the hardware components needed to run U-Boot.                                                                        |                    | :white_check_mark: |
    | `fip-smarc-rzg3e.srec`                           | Firmware package that bundles U-Boot and other secure components into one boot image.                                                                           |                    | :white_check_mark: |
    | `Flash_Writer_SCIF_RZG3E_EVK_LPDDR4X.mot`        | Software that is loaded into the RZ/G3Es RAM to write bootloader files into flash memory.                                                                       |                    | :white_check_mark: |
    | `core-image-minimal-smarc-rzg3e.rootfs.tar.gz`   | Compressed Linux filesystem containing the Linux kernel, drivers, applications and system configurations. This contains the kernel image and DTB under `boot/`. |                    | :white_check_mark: |
    | `core-image-minimal-smarc-rzg3e.rootfs.wic.bmap` | A map for the WIC image that speeds up flashing by detailing which SD Card blocks need data and which are empty.                                                | :white_check_mark: |                    |
    | `core-image-minimal-smarc-rzg3e.rootfs.wic.gz`   | Compressed Linux disk image containing the partition table, bootloaders and rootfs (Linux kernel, drivers, applications and system configurations).             | :white_check_mark: |                    |

=== "core-image-weston"

    | File                                            | Description                                                                                                                                                     |      eSD Boot      |    Network Boot    |
    | ----------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------: | :----------------: |
    | `bl2_bp_spi-smarc-rzg3e.srec`                   | Bootloader for SPI memory that initializes the hardware components needed to run U-Boot.                                                                        |                    | :white_check_mark: |
    | `fip-smarc-rzg3e.srec`                          | Firmware package that bundles U-Boot and other secure components into one boot image.                                                                           |                    | :white_check_mark: |
    | `Flash_Writer_SCIF_RZG3E_EVK_LPDDR4X.mot`       | Software that is loaded into the RZ/G3Es RAM to write bootloader files into flash memory.                                                                       |                    | :white_check_mark: |
    | `core-image-weston-smarc-rzg3e.rootfs.tar.gz`   | Compressed Linux filesystem containing the Linux kernel, drivers, applications and system configurations. This contains the kernel image and DTB under `boot/`. |                    | :white_check_mark: |
    | `core-image-weston-smarc-rzg3e.rootfs.wic.bmap` | A map for the WIC image that speeds up flashing by detailing which SD Card blocks need data and which are empty.                                                | :white_check_mark: |                    |
    | `core-image-weston-smarc-rzg3e.rootfs.wic.gz`   | Compressed Linux disk image containing the partition table, bootloaders and rootfs (Linux kernel, drivers, applications and system configurations).             | :white_check_mark: |                    |

!!! note

    The kernel image `Image-smarc-rzg3e.bin` and DTB
    `r9a09g047e57-smarc.dtb` files are pre-installed into the
    compressed rootfs, so they do not need to be used separately.

## SDK Binary

The SDK installer
`rz-vlp-glibc-x86_64-core-image-weston-cortexa55-smarc-rzg3e-toolchain-5.0.8.sh`
will be located under `build/tmp/deploy/sdk/` in the project directory.

This binary installs the toolchain environment containing all the tools
needed to write and compile software for the RZ/G3E on the Host PC.
