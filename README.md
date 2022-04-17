# Bali - Test Repository

This repository includes test programs and routines for the Bali processor project.

Tests are either for compilation and execution on the FPGA itself in the `java` folder
or test procedures designed for execution from a remote PC, implemented in Python.

Tests are run on the Digilent Arty-A7 board with an Artix-7 35T FPGA.

## Java Test Procedures

- `IntReverse` - Given an integer input, output the decimal base reverse integer.
- `PrimeSieve` - Simple Sieve of Eratosthenes implementation,
   outputs an array of booleans with `true` for prime numbers and `false` for non-primes.
- `QuickSort` - QuickSort implementation for 32-bit integer arrays.
- `RecursiveMath` - Implementation of 32-bit integer addition and multiplication using recursive definitions down to increment/decrement.
- `TowersOfHanoi` - Recursive solution for Towers of Hanoi.

## Python Tests

- `uart_led_test` - Test of the UART receiver module. Receives bytes over UART and displays the binary value on the LED array of the board.
- `uart_echo_test` - Test of UART receiver and transmitter modules, receives byte and echoes it back via the transmitter.
- `uart_calc_test` - Takes two 32-bit integers and a single 8-bit opcode,
  performs the corresponding ALU operation and returns the result via UART transmitter.

## Binary Generation

The `justfile` contains commands for automatic binary generation from the test programs in the `java` folder.
These procedures depend on the `bake` binary translator tool, which should be located in the project's root directory.

### Fetching and Updating `bake`

Building the `bake` tool requires an installation of the [Rust toolchain](https://rustup.rs/).
To automatically fetch and compile `bake` from GitHub, use

```bash
$ just netupdate
```

When working on a local copy of `bake`, set the `BAKE_DIR` variable and use

```bash
$ just localupdate
```

Use the following commands with `just` to create test binaries and files:

- `compile` - Create `class` files from all `java` source files in the `java` folder.
- `binary` - Create `bali.out` binary files from all `class` files in the `java` folder, depends on the `compile` step.
- `testfile` - Create `mem` memory layout files for use with SystemVerilog testbenches from `class` files, depends on the `compile` step.
- `testupdate [TEST_DIR]` - Copy the memory layout files to the `[TEST_DIR]` folder.
  Depends on the `testfile` step.
