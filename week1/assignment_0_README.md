# Assignment 0 - Python Version Management

## Problem Statement

Set up two different Python versions (e.g., Python 3.8 and Python 3.14). Demonstrate how to switch between them seamlessly and run a Python program that uses a language feature available in newer Python versions but unsupported in older versions.

## Solution

Initially, Python 3.14 was already installed on my system. Then, I installed Python 3.8.20 using **pyenv**.

I found that some new features were added after Python 3.8. One of them is the **Dictionary Union Operator (`|`)**, which was introduced in Python 3.9.

I wrote a simple program to test this feature.

<img width="1180" height="747" alt="Python Version Demo" src="https://github.com/user-attachments/assets/49839341-4bf1-4a4c-bad6-61e06d8a957a" />

The program runs successfully in **Python 3.14** because the `|` operator is supported. The same program gives an error in **Python 3.8** because this operator is not available in that version.

## Conclusion

I successfully installed two Python versions using **pyenv** and switched between them. The Dictionary Union Operator (`|`) worked in Python 3.14 but did not work in Python 3.8.
