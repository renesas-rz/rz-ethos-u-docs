# Prepare Target AI Model

AI Models must be compiled using the
[Renesas RUHMI Framework AI Compiler](https://github.com/renesas/ruhmi-framework-rzg)
before they can be evaluated on the RZ/G3E SMARC EVK.

The RUHMI Framework AI Compiler is a software tool that compiles a
TensorFlow Lite model into an optimized version that can be run on the
Ethos-U55 NPU using the EdgeCortix MERA runtime library.

The compiled model contains the Ethos-U custom operator (ethos-u) for
parts of the model that can be executed on the NPU. Parts of the model
that are not supported by the NPU remain in the model and are ran on
the Arm Cortex-M33 CPU.

The automated compilation script `generate-model-data.py` allows for
multiple models to be compiled and randomised input data to be
generated in one run. This is packaged into a single directory that
can be copied to the RZ/G3E SMARC EVK.

!!! note

    The software package supports models where the compiler has
    allocated up to **4MB** for the TensorFlow Lite Micro Tensor
    Arena.

    **Any models with an allocation above 4MB are not supported**.

    The Tensor Arena is used for storing the inputs, outputs and
    intermediate values during inferences.
