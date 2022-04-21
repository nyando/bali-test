BAKE_DIR := "../bake"

clean:
    @rm -f ./java/*.class
    @rm -f ./java/*.bali.out
    @rm -f ./java/*.mem
    @rm -f ./java/*.java

localupdate:
    cd {{BAKE_DIR}} && cargo build --release
    cp {{BAKE_DIR}}/target/release/bake.exe .

netupdate:
    git clone git@github.com:nyando/bake
    cd bake && cargo build --release
    if {{os()}} == "windows"; then cp bake/target/release/bake.exe .; fi
    if {{os()}} == "linux"; then cp bake/target/release/bake .; fi
    rm -rf bake

compileall: clean
    @for file in `echo $(find ./java -name "*.java")`; do javac $file; done

binaryall: compileall
    @for file in `echo $(find ./java -name "*.class")`; do ./bake.exe binary --classfile $file; done

testfileall: compileall
    @for file in `echo $(find ./java -name "*.class")`; do ./bake.exe testfile --classfile $file; done

compile PROGRAM: clean
    @javac ./java/{{PROGRAM}}.java

binary PROGRAM:
    @just compile {{PROGRAM}}
    @./bake.exe binary --classfile ./java/{{PROGRAM}}.class

testbin PROGRAM:
    @just binary {{PROGRAM}}
    @./bake.exe serial --bin ./java/{{PROGRAM}}.bali.out --device COM5 --long

testfile PROGRAM:
    @just compile {{PROGRAM}}
    @./bake.exe testfile --classfile ./java/{{PROGRAM}}.class
