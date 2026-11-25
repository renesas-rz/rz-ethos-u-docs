# Test Compiled AI Models

The models used in the example can be downloaded from:

- [ad_large_int8.tflite](https://github.com/Arm-Examples/ML-zoo/blob/22.02/models/anomaly_detection/micronet_large/tflite_int8/ad_large_int8.tflite)
- [kws_micronet_l.tflite](https://github.com/Arm-Examples/ML-zoo/blob/22.02/models/keyword_spotting/micronet_large/tflite_int8/kws_micronet_l.tflite)
- [tiny_wav2letter_int8.tflite](https://github.com/Arm-Examples/ML-zoo/blob/22.02/models/speech_recognition/tiny_wav2letter/tflite_int8/tiny_wav2letter_int8.tflite)

Compiled models can also be run with the Arm `delegate_runner` and
TensorFlow Lite `benchmark_model` applications, see
[Run Third Party Applications](../getting-started/third-party-applications.md).

______________________________________________________________________

=== "Offline compilation"

    1. Copy the generated output directory to the rootfs on either the SD
        Card or TFTP directory.

    1. Power **ON** the board by pressing the **POWER** button for at
        least 1 second until the **CARRIER ON** LED lights up.<br>The
        **CARRIER ON** LED is located above the **POWER** button.

        !!! note

            Since the U-Boot environment is saved, autoboot no longer needs
            to be stopped.

    1. Once Linux has booted up, login with `root` (no password).

        ```
        Poky (Yocto Project Reference Distro) 5.0.14 smarc-rzg3e ttySC3
        smarc-rzg3e login: root
        ```

=== "On device compilation"

    Since the models were compiled on device, no further data needs to be
    copied to the rootfs.

1. Navigate to the directory that contains `model_deployment_dir` (the
    output directory generated during model compilation).

1. Run the Model Executor application.

```bash
/usr/bin/model-executor -e model_deployment_dir/config.yaml
```

This will print a log to the console containing the inference time per
run and an average inference time for each model.

```
INFO: EthosuOp: Version 1.0
INFO: EthosuOp: Device name = /dev/accel/accel0
INFO: EthosuOp: Timeout = 60000000000
INFO: EthosuOp: Enable cycle counter = false
Model being executed: ad_large_int8
INFO: Ethos-U Operator Delegate delegate: 1 nodes delegated out of 1 nodes with 1 partitions.

Inference Run #1, end-to-end inference time: 1.459250ms
...
Inference Run #10, end-to-end inference time: 1.350000ms
------------------------------
           Results
Model: ad_large_int8
Average inference time: 1.37ms over 10 runs
------------------------------
Model being executed: kws_micronet_l
Inference Run #1, end-to-end inference time: 1.712125ms
...
Inference Run #10, end-to-end inference time: 1.660250ms
------------------------------
           Results
Model: kws_micronet_l
Average inference time: 1.69ms over 10 runs
------------------------------
Model being executed: tiny_wav2letter_int8
Inference Run #1, end-to-end inference time: 8.412625ms
...
Inference Run #10, end-to-end inference time: 7.208416ms
------------------------------
           Results
Model: tiny_wav2letter_int8
Average inference time: 7.41ms over 10 runs
------------------------------
```
