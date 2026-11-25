# Run Third Party Applications

In addition to the Renesas example applications, the package installs
two generic tools that can be used to validate and benchmark models
on the Ethos-U55.

!!! note

    These tools are provided by Arm and the TensorFlow project, and are
    not Renesas applications. Refer to the upstream documentation for
    the full list of features and options.

| Application       | Provided By                                                                                                                      | Source Code                                                                                                                                         | Purpose                                                                                                               |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `delegate_runner` | [Arm Ethos-U Linux Driver Stack](https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-linux-driver-stack/-/tree/26.08) | [delegate_runner source code](https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-linux-driver-stack/-/tree/26.08/utils/delegate_runner) | Runs a model using the Ethos-U delegate and generates output for verification (no performance measurement capability) |
| `benchmark_model` | [TensorFlow Lite](https://github.com/tensorflow/tensorflow/blob/v2.20.0)                                                         | [benchmark_model source code](https://github.com/tensorflow/tensorflow/blob/v2.20.0/tensorflow/lite/tools/benchmark/README.md)                      | Benchmarks a model using CPU or a provided external TFLite delegate (performance measurement capability)              |

Both tools expect a model compiled with the Vela Compiler
if testing Ethos-U55 NPU performance. See
[Compile AI Models with Vela](../prepare-models/compile-models.md) for
how to generate the model data.

All applications are installed under `/usr/bin`.

## Arm delegate_runner

Overview:

- Loads a TensorFlow Lite model and runs inference with the Ethos-U
    delegate.
- Useful for a quick check that a Vela-compiled model runs on the NPU.

!!! note

    This application does not support running several iterations of
    inference and has no performance measurement capability.

### Run Application

To run the application, execute the following command.

```bash
/usr/bin/delegate_runner \
    -l /usr/lib/libethosu_op_delegate.so.1 \
    -n /usr/share/models/mobilenet_v2/mobilenet_v2_1.0_224_INT8/mobilenet_v2_1.0_224_INT8_vela.tflite \
    -i /usr/share/models/mobilenet_v2/mobilenet_v2_1.0_224_INT8/all-inputs.bin \
    -o output.bin
```

This will print a log to the console containing the delegate information.

```
INFO: EthosuOp: Version 1.0
INFO: EthosuOp: Device name = /dev/accel/accel0
INFO: EthosuOp: Timeout = 60000000000
INFO: EthosuOp: Enable cycle counter = false
INFO: EXTERNAL delegate created.
INFO: Ethos-U Operator Delegate delegate: 1 nodes delegated out of 1 nodes with 1 partitions.
```

### Command-Line Parameters

To get a complete list with information on the supported arguments,
please execute the following command.

```bash
/usr/bin/delegate_runner -h
```

## TensorFlow Lite benchmark_model

Overview:

- Has the ability to benchmark a TFLite model and its individual
    operators.
- Can generate random inputs.
- Allows the Ethos-U delegate to be used via the TensorFlow Lite
    external delegate mechanism.

### Run Application

The application by default targets the CPU. In order to target
the NPU, the Ethos-U delegate library is required to be provided
via the command-line parameter `--external_delegate_path`.

To run inference on the NPU, execute the following command.

```bash
/usr/bin/benchmark_model \
    --graph=/usr/share/models/mobilenet_v2/mobilenet_v2_1.0_224_INT8/mobilenet_v2_1.0_224_INT8_vela.tflite \
    --external_delegate_path=/usr/lib/libethosu_op_delegate.so.1
```

This will print a log to the console containing the delegate information
and inference timings.

```
INFO: STARTING!
INFO: Log parameter values verbosely: [0]
INFO: Graph: [/usr/share/models/mobilenet_v2/mobilenet_v2_1.0_224_INT8/mobilenet_v2_1.0_224_INT8_vela.tflite]
INFO: Signature to run: []
INFO: External delegate path: [/usr/lib/libethosu_op_delegate.so.1]
INFO: Loaded model /usr/share/models/mobilenet_v2/mobilenet_v2_1.0_224_INT8/mobilenet_v2_1.0_224_INT8_vela.tflite
INFO: EthosuOp: Version 1.0
INFO: EthosuOp: Device name = /dev/accel/accel0
INFO: EthosuOp: Timeout = 60000000000
INFO: EthosuOp: Enable cycle counter = false
INFO: EXTERNAL delegate created.
INFO: Ethos-U Operator Delegate delegate: 1 nodes delegated out of 1 nodes with 1 partitions.

INFO: Explicitly applied EXTERNAL delegate, and the model graph will be completely executed by the delegate.
INFO: The input model file size (MB): 3.46322
INFO: Initialized session in 5.239ms.
INFO: Running benchmark for at least 1 iterations and at least 0.5 seconds but terminate if exceeding 150 seconds.
INFO: count=63 first=10036 curr=7819 min=7787 max=10036 avg=7998 std=460 p5=7794 median=7819 p95=8963

INFO: Running benchmark for at least 50 iterations and at least 1 seconds but terminate if exceeding 150 seconds.
INFO: count=126 first=8951 curr=7783 min=7758 max=8961 avg=7940.29 std=376 p5=7765 median=7795 p95=8938

INFO: Inference timings in us: Init: 5239, First inference: 10036, Warmup (avg): 7998, Inference (avg): 7940.29
INFO: Note: as the benchmark tool itself affects memory footprint, the following is only APPROXIMATE to the actual memory footprint of the model at runtime. Take the information at your discretion.
INFO: Memory footprint delta from the start of the tool (MB): init=2.71875 overall=6.74219
```

### Command-Line Parameters

To get a complete list with information on the supported arguments,
please execute the following command.

```bash
/usr/bin/benchmark_model --help
```
