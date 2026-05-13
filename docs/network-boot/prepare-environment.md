# Prepare Necessary Environment

Please prepare the following hardware equipment.

| Equipment                                                                                | Details                                                                                             |
| ---------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| [RZ/G3E SMARC EVK](https://www.renesas.com/en/design-resources/boards-kits/rz-g3e-evkit) | Evaluation Board Kit for RZ/G3E.<br>Includes the microUSB to serial cable for serial communication. |
| USB Type-C Power Supply                                                                  | 65W rated PD power supply to power the board.                                                       |
| USB Cable Type-C                                                                         | 65W rated USB Type-C cable used to connect the power supply to the board.                           |
| HDMI Display                                                                             | Used to display graphics of the board.                                                              |
| HDMI to microHDMI Cable                                                                  | Used to connect the HDMI display to the board.                                                      |
| Linux PC (Ubuntu)                                                                        | Used to host NFS directory containing Ethos-U binaries.<br>Recommended: Ubuntu 22.04 LTS (64 bit)   |
| Windows PC                                                                               | **Optional**: Used for flashing the bootloaders instead of a Linux PC.                              |

The diagram below illustrates the hardware connections to the RZ/G3E SMARC
EVK.

<figure>
  <img src="../../assets/images/network-boot-hardware-setup.png"
       alt="Hardware Setup for Network Boot">
  <figcaption>Hardware Setup for Network Boot</figcaption>
</figure>
