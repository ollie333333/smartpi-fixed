from setuptools import setup, find_packages

setup(
    name="smartpi",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy"
        # You can add "tflite-runtime" here if you want optional TensorFlow Lite support
    ],
    description="SmartPi AI: Offline ChatGPT‑style assistant for Raspberry Pi",
    author="ollie333333",
    author_email="your.email@example.com",
    entry_points={
        "console_scripts": [
            "smartpi-chat=smartpi.gui:run_gui"
        ]
    }
)
