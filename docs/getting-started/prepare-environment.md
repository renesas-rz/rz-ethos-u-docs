# Prepare Necessary Environment

The necessary environment is broken into 2 components:

1. Hardware
1. Software

## Necessary Hardware

Please prepare the following hardware equipment.

| Equipment                                                                                | Details                                                                                                           |
| ---------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| [RZ/G3E SMARC EVK](https://www.renesas.com/en/design-resources/boards-kits/rz-g3e-evkit) | Evaluation Board Kit for RZ/G3E.<br>Includes the microUSB to serial cable for serial communication.               |
| USB Type-C Power Supply                                                                  | 65W rated PD power supply to power the board.                                                                     |
| USB Cable Type-C                                                                         | 65W rated USB Type-C cable used to connect the power supply to the board.                                         |
| HDMI Display                                                                             | Used to display graphics of the board.                                                                            |
| HDMI to microHDMI Cable                                                                  | Used to connect the HDMI display to the board.                                                                    |
| MicroSD Card                                                                             | Must have over 8GB capacity.                                                                                      |
| SD Card Reader                                                                           | Used for setting up microSD card.                                                                                 |
| Linux PC (Ubuntu)                                                                        | **Optional**: Used for setting up microSD card instead of a Windows PC.<br>Recommended: Ubuntu 22.04 LTS (64 bit) |
| Windows PC                                                                               | **Optional**: Used for setting up microSD card instead of a Linux PC.                                             |

The diagram below illustrates the hardware connections to the RZ/G3E
SMARC EVK.

<figure>
  <img src="../../assets/images/esd-boot-hardware-setup.png"
       alt="Hardware Setup for eSD Boot">
  <figcaption>Hardware Setup for eSD Boot</figcaption>
</figure>

## Necessary Software

=== "Linux PC"

    For SD Card flashing please install the following package on
    Ubuntu:

    ```bash
    sudo apt-get update

    sudo apt-get install bmap-tools
    ```

=== "Windows PC"

    For SD Card flashing, please install balenaEtcher on Windows from
    [https://etcher.balena.io](https://etcher.balena.io).
