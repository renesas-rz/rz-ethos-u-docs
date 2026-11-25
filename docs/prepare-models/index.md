# Prepare Target AI Model

AI models must be compiled using the
[Arm Ethos-U Vela Compiler](https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/tree/5.2.0)
before they can be evaluated on the RZ/G3E SMARC EVK.

The Ethos-U Vela Compiler is a software tool that compiles a
TensorFlow Lite model into an optimized version that can be run on the
Ethos-U55 NPU.

The compiled model contains the Ethos-U custom operator (ethos-u) for
parts of the model that can be executed on the NPU. Parts of the model
that are not supported by the NPU remain in the final model and are
run on the Arm Cortex-A55 CPU via TensorFlow Lite.

Models can be compiled either offline (on a Linux Host PC) or on-device
(directly on the RZ/G3E SMARC EVK). Both methods make use of the
automated compilation script `generate-model-data.py` (RZ/G3E SMARC
EVK) or `generate-model-data-host.sh` (Linux Host PC), which allows
for multiple models to be compiled and randomized input data to be
generated in one run. This is packaged into a single directory that
can be copied to the RZ/G3E SMARC EVK if compiling on a Linux Host PC.
