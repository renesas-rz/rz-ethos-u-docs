# Compile AI Models with RUHMI

Before model compilation, a quantized TensorFlow Lite model
(`.tflite`) must be prepared or sourced.

!!! note

    Arm provides pre-trained TensorFlow Lite models on their
    [ML Zoo GitHub repository](https://github.com/Arm-Examples/ML-zoo/tree/22.02).

=== "Single Model"

    1. Copy the model file to the shared directory being used by the
        Docker container.

    1. Compile the model with RUHMI.

        ```bash
        python3 /generate-model-data.py -d model_deployment_dir -m mobilenet_v2_1.0_224_INT8.tflite
        ```

        !!! note

            1. Remember to replace `mobilenet_v2_1.0_224_INT8.tflite` with
                the correct filepath of the model.
            1. If RUHMI is being used natively, please update the command
                to use the path to the `generate-model-data.py` script.
            1. Feel free to use a different output directory name instead
                of `model_deployment_dir`.

    1. Upon completion, the compilation log will be displayed on the
        console and the MERA model data saved in the defined output
        directory.

    ```
    2026-03-31 13:45:02,631 INFO -  ------------------------------------------------------------
    2026-03-31 13:45:02,631 INFO -  Model being compiled with RUHMI: mobilenet_v2_1.0_224_INT8 (mobilenet_v2_1.0_224_INT8.tflite)
    2026-03-31 13:45:02,651 INFO -   *** mera v2.5.0+pkg.3782 ***
    2026-03-31 13:45:02,651 INFO -  Starting deployment of model 'mobilenet_v2_1.0_224_INT8'...
    [2026-03-31 13:45:02.668] [info] Loading and converting TFLite model ...
    [2026-03-31 13:45:02.668] [info] TFLite Model Version: 3
    [2026-03-31 13:45:02.822] [info] Converting to canonical ...
    [2026-03-31 13:45:02.846] [info] Running TFLite transformation passes ...
    [2026-03-31 13:45:02.854] [info] Converting to target IR ...
    [2026-03-31 13:45:02.861] [info] Dividing and exporting regions ...
    [2026-03-31 13:45:02.864] [info] Model is fully captured to target ARM_ETHOS_U55
    [2026-03-31 13:45:02.895] [info] Model successfully converted.
    Info: Changing const_mem_area from Sram to OnChipFlash. This will use the same characteristics as Sram.
    Warning: Input TensorFlow Lite network contains a zero length buffer (index = 0) which is semantically not empty. However, it will be treated as an empty buffer.

    Network summary for model
    Accelerator configuration               Ethos_U55_256
    System configuration                    RZG3E_SRAM_64
    Memory mode                                 Sram_Only
    Accelerator clock                                1000 MHz
    Design peak SRAM bandwidth                       7.45 GB/s
    Design peak On-chip Flash bandwidth              7.45 GB/s

    Total SRAM used                               1470.00 KiB
    Total On-chip Flash used                      3536.23 KiB

    CPU operators = 0 (0.0%)
    NPU operators = 95 (100.0%)

    Average SRAM bandwidth                           5.05 GB/s
    Input   SRAM bandwidth                          11.21 MB/batch
    Weight  SRAM bandwidth                           0.00 MB/batch
    Output  SRAM bandwidth                           6.66 MB/batch
    Total   SRAM bandwidth                          17.87 MB/batch
    Total   SRAM bandwidth            per input     17.87 MB/inference (batch size 1)

    Average On-chip Flash bandwidth                  1.65 GB/s
    Input   On-chip Flash bandwidth                  0.00 MB/batch
    Weight  On-chip Flash bandwidth                  5.65 MB/batch
    Output  On-chip Flash bandwidth                  0.00 MB/batch
    Total   On-chip Flash bandwidth                  5.82 MB/batch
    Total   On-chip Flash bandwidth   per input      5.82 MB/inference (batch size 1)

    Neural network macs                         304452946 MACs/batch
    Network Tops/s                                   0.17 Tops/s

    NPU cycles                                    3159461 cycles/batch
    SRAM Access cycles                            2512149 cycles/batch
    DRAM Access cycles                                  0 cycles/batch
    On-chip Flash Access cycles                    763033 cycles/batch
    Off-chip Flash Access cycles                        0 cycles/batch
    Total cycles                                  3536879 cycles/batch

    Batch Inference time                 3.54 ms,  282.74 inferences/s (batch size 1)

    2026-03-31 13:45:06,847 INFO -  Compilation finished successfully. Took 00h00m04s
    INFO: Created TensorFlow Lite XNNPACK delegate for CPU.
    2026-03-31 13:45:06,860 INFO -  Input data for tensor #0 has been saved to: model_deployment_dir/mobilenet_v2_1.0_224_INT8/input-0.bin
    2026-03-31 13:45:06,872 INFO -  Expected output data for tensor #0 has been saved to: model_deployment_dir/mobilenet_v2_1.0_224_INT8/expected-output-0.bin
    2026-03-31 13:45:06,873 INFO -  ------------------------------------------------------------
    2026-03-31 13:45:06,874 INFO -  The configuration YAML has been saved to: model_deployment_dir/config.yaml
    2026-03-31 13:45:06,874 INFO -  Please copy the model_deployment_dir directory to the board!
    ```

=== "Multiple Models"

    1. Copy the model files to the shared directory being used
        by the Docker container.

    1. Compile the models with RUHMI.

        ```bash
        python3 /generate-model-data.py -d model_deployment_dir -m ad_large_int8.tflite kws_micronet_l.tflite tiny_wav2letter_int8.tflite
        ```

        !!! note

            The models used in the example can be downloaded from:

            1. [ad_large_int8.tflite](https://github.com/Arm-Examples/ML-zoo/blob/22.02/models/anomaly_detection/micronet_large/tflite_int8/ad_large_int8.tflite)
            1. [kws_micronet_l.tflite](https://github.com/Arm-Examples/ML-zoo/blob/22.02/models/keyword_spotting/micronet_large/tflite_int8/kws_micronet_l.tflite)
            1. [tiny_wav2letter_int8.tflite](https://github.com/Arm-Examples/ML-zoo/blob/22.02/models/speech_recognition/tiny_wav2letter/tflite_int8/tiny_wav2letter_int8.tflite)

    1. Upon completion, the compilation log will be displayed on the
        console and the MERA data for all models saved in the defined
        output directory.

    ```
    2026-03-31 13:23:39,633 INFO -  ------------------------------------------------------------
    2026-03-31 13:23:39,633 INFO -  Model being compiled with RUHMI: ad_large_int8 (ad_large_int8.tflite)
    2026-03-31 13:23:39,653 INFO -   *** mera v2.5.0+pkg.3782 ***
    2026-03-31 13:23:39,653 INFO -  Starting deployment of model 'ad_large_int8'...
    ...
    2026-03-31 13:23:40,600 INFO -  Compilation finished successfully. Took 00h00m00s
    ...
    2026-03-31 13:23:40,605 INFO -  Input data for tensor #0 has been saved to: model_deployment_dir/ad_large_int8/input-0.bin
    2026-03-31 13:23:40,607 INFO -  Expected output data for tensor #0 has been saved to: model_deployment_dir/ad_large_int8/expected-output-0.bin
    2026-03-31 13:23:40,607 INFO -  ------------------------------------------------------------
    2026-03-31 13:23:40,607 INFO -  ------------------------------------------------------------
    2026-03-31 13:23:40,607 INFO -  Model being compiled with RUHMI: kws_micronet_l (kws_micronet_l.tflite)
    2026-03-31 13:23:40,626 INFO -   *** mera v2.5.0+pkg.3782 ***
    2026-03-31 13:23:40,626 INFO -  Starting deployment of model 'kws_micronet_l'...
    ...
    2026-03-31 13:23:41,755 INFO -  Compilation finished successfully. Took 00h00m01s
    2026-03-31 13:23:41,759 INFO -  Input data for tensor #0 has been saved to: model_deployment_dir/kws_micronet_l/input-0.bin
    2026-03-31 13:23:41,761 INFO -  Expected output data for tensor #0 has been saved to: model_deployment_dir/kws_micronet_l/expected-output-0.bin
    2026-03-31 13:23:41,761 INFO -  ------------------------------------------------------------
    2026-03-31 13:23:41,762 INFO -  ------------------------------------------------------------
    2026-03-31 13:23:41,762 INFO -  Model being compiled with RUHMI: tiny_wav2letter_int8 (tiny_wav2letter_int8.tflite)
    2026-03-31 13:23:41,781 INFO -   *** mera v2.5.0+pkg.3782 ***
    2026-03-31 13:23:41,781 INFO -  Starting deployment of model 'tiny_wav2letter_int8'...
    ...
    2026-03-31 13:23:43,912 INFO -  Compilation finished successfully. Took 00h00m02s
    2026-03-31 13:23:43,923 INFO -  Input data for tensor #0 has been saved to: model_deployment_dir/tiny_wav2letter_int8/input-0.bin
    2026-03-31 13:23:43,931 INFO -  Expected output data for tensor #0 has been saved to: model_deployment_dir/tiny_wav2letter_int8/expected-output-0.bin
    2026-03-31 13:23:43,932 INFO -  ------------------------------------------------------------
    2026-03-31 13:23:43,934 INFO -  The configuration YAML has been saved to: model_deployment_dir/config.yaml
    2026-03-31 13:23:43,935 INFO -  Please copy the model_deployment_dir directory to the board!
    ```

!!! note

    The warning `Input TensorFlow Lite network contains a zero length buffer ...` message is caused due to the TensorFlow Lite converter
    attaching semantic flag to buffer #0, which is identified with Vela.

    Please ignore this warning as the compiler correctly identifies
    that buffer #0 should be treated as an empty buffer.
