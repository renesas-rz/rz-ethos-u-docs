# Test Compiled AI Models

The models used in the example can be downloaded from:

- [ad_large_int8.tflite](https://github.com/Arm-Examples/ML-zoo/blob/22.02/models/anomaly_detection/micronet_large/tflite_int8/ad_large_int8.tflite)
- [kws_micronet_l.tflite](https://github.com/Arm-Examples/ML-zoo/blob/22.02/models/keyword_spotting/micronet_large/tflite_int8/kws_micronet_l.tflite)
- [tiny_wav2letter_int8.tflite](https://github.com/Arm-Examples/ML-zoo/blob/22.02/models/speech_recognition/tiny_wav2letter/tflite_int8/tiny_wav2letter_int8.tflite)

______________________________________________________________________

1. Copy the generated output directory to the rootfs on either the SD
    Card or TFTP directory.

1. Power **ON** the board by pressing the **POWER** button for at
    least 1 second to boot up the board.

1. Using the serial console, log in and navigate to the`/usr/bin/`
    directory.

    ```bash
    cd /usr/bin
    ```

1. Run the Model Executor application with the generated output
    directory containing the MERA data for all compiled models.

```bash
model-executor -e model_deployment_dir/config.yaml
```

This will print a log to the console containing the inference time per
run and an average inference time for each model.

```
Model being executed: ad_large_int8
[2026-03-30 20:22:32.633] [console] [info] MERA 2.0 Runtime
Inference Run #1, inference time: 16.962957ms
...
Inference Run #10, inference time: 16.892876ms
------------------------------
           Results
Model: ad_large_int8
Average inference time: 16.94ms over 10 runs
------------------------------
Successfully saved output data for tensor #1 to model_deployment_dir/ad_large_int8/output_0.bin
Model being executed: kws_micronet_l
[2026-03-30 20:22:32.807] [console] [info] MERA 2.0 Runtime
Inference Run #1, inference time: 16.779249ms
...
Inference Run #10, inference time: 16.698418ms
------------------------------
           Results
Model: kws_micronet_l
Average inference time: 16.71ms over 10 runs
------------------------------
Successfully saved output data for tensor #1 to model_deployment_dir/kws_micronet_l/output_0.bin
Model being executed: tiny_wav2letter_int8
[2026-03-30 20:22:32.979] [console] [info] MERA 2.0 Runtime
Inference Run #1, inference time: 25.037624ms
...
Inference Run #10, inference time: 24.954540ms
------------------------------
           Results
Model: tiny_wav2letter_int8
Average inference time: 24.97ms over 10 runs
------------------------------
Successfully saved output data for tensor #1 to model_deployment_dir/tiny_wav2letter_int8/output_0.bin
```
