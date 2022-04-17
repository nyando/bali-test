BAKE_DIR := "../bake"

clean:
    rm -f ./java/*.class
    rm -f ./java/*.bali.out
    rm -f ./java/*.mem

localupdate:
    cd {{BAKE_DIR}} && cargo build --release
    cp {{BAKE_DIR}}/target/release/bake.exe .

netupdate:
    git clone git@github.com:nyando/bake
    cd bake && cargo build --release
    if {{os()}} == "windows"; then cp bake/target/release/bake.exe .; fi
    if {{os()}} == "linux"; then cp bake/target/release/bake .; fi
    rm -rf bake

compile: clean
    for file in `echo $(find ./java -name "*.java")`; do javac $file; done

binary: compile
    for file in `echo $(find ./java -name "*.class")`; do ./bake.exe binary --classfile $file; done

testfile: compile
    for file in `echo $(find ./java -name "*.class")`; do ./bake.exe testfile --classfile $file; done

testupdate TEST_DIR: testfile
    for file in `echo $(find ./java -name "*.mem")`; do cp $file {{TEST_DIR}}; done
