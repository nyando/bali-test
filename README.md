# Bali - Minimized Java Processor - Test Repository

This repository includes test programs and routines for the Bali processor project.

Tests are either for compilation and execution on the FPGA itself in the `java` folder
or test procedures designed for execution from a remote PC, implemented in Python.

Tests are run on the Digilent Arty-A7 board with an Artix-7 35T FPGA.

## Java Test Procedures

- `IntReverse` - Given an integer input, output the decimal base reverse integer.
- `PrimeSieve` - Simple Sieve of Eratosthenes implementation, outputting an array of booleans with `true` for prime numbers and `false` for non-primes.
- `QuickSort` - QuickSort implementation for 32-bit integer arrays.
- `RecursiveMath` - Implementation of 32-bit integer addition and multiplication using recursive definitions down to increment/decrement.
- `TowersOfHanoi` - Recursive solution for Towers of Hanoi.

## Python Tests

- `uart_test` - Test of the UART receiver module. Receives bytes over UART and displays the binary value on the LED array of the board.
