# Run Example Applications

The `meta-rz-ethos-u-examples` layer deploys several evaluation
applications to the rootfs, making it easy to assess Ethos-U and
model performance.

There are 2 types of applications provided:

1. MobileNet V2 Classifier
1. Generic Model Evaluation

!!! note

    The `meta-rz-ethos-u-demos` layer deploys demo applications to the rootfs.

    For information on the Image Classification demo, please see
    [Image Classification demo documentation](https://github.com/renesas-rz/meta-rz-ethos-u-demos/blob/master/recipes-demos/image-classification/files/c%2B%2B/README_USB_CAMERA.md).

All applications are installed under `/usr/bin`, so navigate to this
directory.

```bash
cd /usr/bin
```

## MobileNet V2 Classifier

Overview:

- Runs image classification on a local image file using the
    MobileNet V2 model.
- Inference is executed on the NPU only.
- There are **2** variants of this application that demonstrate the
    C++ library and Python library.
    - **C++**: mobilenet-v2-classifier
    - **Python**: mobilenet-v2-classifier.py
- C++ application supports HDMI output and console-only output.
    - For HDMI output, the following resolutions are supported:
        *1920x1080*, *1280x720* and *800x600*.
- Python application only supports console-only output.
- Sample image files have been provided under
    `/usr/share/image-classification/images/`.

### Run C++ Application

=== "HDMI Display Mode"

    To run the application, execute the following command.

    ```bash
    ./mobilenet-v2-classifier
    ```

    This will output the inference results to the HDMI display as seen
    in the image below.

    <figure>
      <img src="../../assets/images/mobilenet-v2-classifier-gui.png"
           alt="Image displayed on HDMI output">
      <figcaption>Image displayed on HDMI output</figcaption>
    </figure>

    The serial console will contain the inference time and a message
    about how to exit the application:

    ```
    INFO: EthosuOp: Version 1.0
    INFO: EthosuOp: Device name = /dev/accel/accel0
    INFO: EthosuOp: Timeout = 60000000000
    INFO: EthosuOp: Enable cycle counter = false
    INFO: Ethos-U Operator Delegate delegate: 1 nodes delegated out of 1 nodes with 1 partitions.

    Inference Run #1, inference time: 8.208917ms
    ...
    Average Inference time: 8.11ms over 10 runs

    Displaying top Image Classification results....
    Please press the ENTER key to close the application
    ```

    Once the **ENTER** key is selected on the serial console window, the
    display window and application will close.

=== "Console Only Mode"

    To run the application, execute the following command.

    ```bash
    ./mobilenet-v2-classifier -c
    ```

    This will print a log to the console containing the inference time and
    image classification results.

    ```
    Inference Run #1, inference time: 8.208917ms
    ...
    Average Inference time: 8.11ms over 10 runs

    Printing top Image Classification results....

    76.95% -> tabby, tabby cat

    14.06% -> Egyptian cat

    5.47% -> tiger cat

    0.39% -> bow tie, bow-tie, bowtie

    0.39% -> lynx, catamount
    ```

### Run Python Application

To run the application, execute the following command.

```bash
./mobilenet-v2-classifier.py
```

This will print a log to the console containing the inference time and
image classification results.

```
INFO: EthosuOp: Version 1.0
INFO: EthosuOp: Device name = /dev/accel/accel0
INFO: EthosuOp: Timeout = 60000000000
INFO: EthosuOp: Enable cycle counter = false
INFO: Ethos-U Operator Delegate delegate: 1 nodes delegated out of 1 nodes with 1 partitions.

2026-10-20 09:24:45,344 INFO -  Inference Run #1, inference time: 8.254417ms
...
2026-10-20 09:24:45,424 INFO -  Average Inference time: 8.24ms over 10 runs
2026-10-20 09:24:45,426 INFO -  Printing top Image Classification results...
76.95% -> tabby, tabby cat
14.06% -> Egyptian cat
5.47% -> tiger cat
0.39% -> lynx, catamount
0.39% -> bow tie, bow-tie, bowtie
```

### Command-Line Parameters

The table below details the command-line parameters for the MobileNet V2
Classifier application variants (C++ and Python).

| Parameter           | Details                                                | Supported Application                                     |                                                                    Default                                                                    |
| ------------------- | ------------------------------------------------------ | --------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------: |
| `-c`<br>`--console` | Prints results to the console only, no display. (Flag) | `mobilenet-v2-classifier`                                 |                                                                     False                                                                     |
| `-i`<br>`--image`   | Path to image file to run inference on.                | `mobilenet-v2-classifier`<br>`mobilenet-v2-classifier.py` | [cat.bmp](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/24.08/resources/img_class/samples/cat.bmp) |
| `-n`<br>`--number`  | Number of times to run inference.                      | `mobilenet-v2-classifier`<br>`mobilenet-v2-classifier.py` |                                                                      10                                                                       |
| `-o`<br>`--output`  | Name of the Wayland output to show results on.         | `mobilenet-v2-classifier`                                 |                                                                   HDMI-A-1                                                                    |

## Generic Model Evaluation

Overview:

- Validates and benchmarks models on the RZ/G3E.
- The application allows for the output directory generated during model
    compilation to be used as input, where inference is run on each model
    defined in the auto-generated configuration file.
- There are **2** variants of this application that demonstrates the
    C++ library and Python library.
    - **C++**: model-executor
    - **Python**: model-executor.py
- There is no difference in the features between both applications.
- A sample model (MobileNet V2) has been provided under
    `/usr/share/models/mobilenet_v2`.

### Run Application

=== "C++"

    To run the application, execute the following command.

    ```bash
    ./model-executor
    ```

    This will print a log to the console containing the inference time per
    run and an average inference time.

    ```
    INFO: EthosuOp: Version 1.0
    INFO: EthosuOp: Device name = /dev/accel/accel0
    INFO: EthosuOp: Timeout = 60000000000
    INFO: EthosuOp: Enable cycle counter = false
    Model being executed: mobilenet_v2_1.0_224_INT8
    INFO: Ethos-U Operator Delegate delegate: 1 nodes delegated out of 1 nodes with 1 partitions.

    Inference Run #1, end-to-end inference time: 8.108708ms
    Inference Run #2, end-to-end inference time: 8.080666ms
    Inference Run #3, end-to-end inference time: 8.080208ms
    Inference Run #4, end-to-end inference time: 7.934250ms
    Inference Run #5, end-to-end inference time: 7.813875ms
    Inference Run #6, end-to-end inference time: 7.870584ms
    Inference Run #7, end-to-end inference time: 9.013875ms
    Inference Run #8, end-to-end inference time: 7.910541ms
    Inference Run #9, end-to-end inference time: 7.859833ms
    Inference Run #10, end-to-end inference time: 7.870417ms
    ------------------------------
               Results
    Model: mobilenet_v2_1.0_224_INT8
    Average inference time: 8.05ms over 10 runs
    ------------------------------
    ```

=== "Python"

    To run the application, execute the following command.

    ```bash
    ./model-executor.py
    ```

    This will print a log to the console containing the inference time per
    run and an average inference time.

    ```
    INFO: EthosuOp: Version 1.0
    INFO: EthosuOp: Device name = /dev/accel/accel0
    INFO: EthosuOp: Timeout = 60000000000
    INFO: EthosuOp: Enable cycle counter = false
    2026-10-20 09:28:04,763 INFO -  Model being executed: mobilenet_v2_1.0_224_INT8
    INFO: Ethos-U Operator Delegate delegate: 1 nodes delegated out of 1 nodes with 1 partitions.

    2026-10-20 09:28:04,789 INFO -  Inference Run #1, inference time: 8.249667ms
    2026-10-20 09:28:04,798 INFO -  Inference Run #2, inference time: 8.325083ms
    2026-10-20 09:28:04,806 INFO -  Inference Run #3, inference time: 8.139583ms
    2026-10-20 09:28:04,815 INFO -  Inference Run #4, inference time: 8.099209ms
    2026-10-20 09:28:04,824 INFO -  Inference Run #5, inference time: 8.089917ms
    2026-10-20 09:28:04,832 INFO -  Inference Run #6, inference time: 8.081667ms
    2026-10-20 09:28:04,842 INFO -  Inference Run #7, inference time: 9.020875ms
    2026-10-20 09:28:04,851 INFO -  Inference Run #8, inference time: 8.124875ms
    2026-10-20 09:28:04,859 INFO -  Inference Run #9, inference time: 8.029792ms
    2026-10-20 09:28:04,868 INFO -  Inference Run #10, inference time: 8.095458ms
    2026-10-20 09:28:04,868 INFO -  ------------------------------
    2026-10-20 09:28:04,869 INFO -             Results
    2026-10-20 09:28:04,869 INFO -  Model: mobilenet_v2_1.0_224_INT8
    2026-10-20 09:28:04,869 INFO -  Average inference time: 8.23ms over 10 runs
    2026-10-20 09:28:04,869 INFO -  ------------------------------
    ```

### Command-Line Parameters

Both the C++ and Python Model Executor applications support the
command-line parameters detailed below.

| Parameter                        | Details                                                                 |                   Default                    |
| -------------------------------- | ----------------------------------------------------------------------- | :------------------------------------------: |
| `-e`<br>`--executor_config_file` | Path to file containing information about models to run inference with. | `/usr/share/models/mobilenet_v2/config.yaml` |
| `-n`<br>`--number`               | Number of times to run inference.                                       |                      10                      |
| `-r`<br>`--use_ref_kernels`      | Use TensorFlow Lite reference kernels for CPU offload.                  |                    False                     |
| `-t`<br>`--timeout`              | Timeout in nanoseconds.                                                 |                 60000000000                  |

!!! tip

    The Arm `delegate_runner` and TensorFlow Lite `benchmark_model`
    applications are also installed. See
    [Run Third Party Applications](third-party-applications.md).
