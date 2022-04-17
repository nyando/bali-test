BAKE_DIR := "../bake"

clean:
    rm -f ./java/*.class
    rm -f ./java/*.bali.out
    rm -f ./java/*.mem

update:
    cd {{BAKE_DIR}} && cargo build --release
    cp {{BAKE_DIR}}/target/release/bake.exe .

compile: clean
    for file in `echo $(find ./java -name "*.java")`; do javac $file; done

binary: compile
    for file in `echo $(find ./java -name "*.class")`; do ./bake.exe binary --classfile $file; done

testfile: compile
    for file in `echo $(find ./java -name "*.class")`; do ./bake.exe testfile --classfile $file; done
