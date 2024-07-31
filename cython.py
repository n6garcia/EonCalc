#!/usr/bin/python3

## LINUX ONLY

## Build Flags
#
# --windows [default:linux] - compile target for windows
# --gdb [default:disabled] - enables cmd debugger
# --gen-main [default:disabled] - generates c++ from python
#
##

import os, sys, subprocess

CC = "g++"
C = "gcc"

libs = []  # ex -lGL


def genmain():
    o = []

    BPLATE = genbplate()

    o.extend(
        [
            "int main(int argc, char **argv) {",
            BPLATE,
        ]
    )

    o.append("}")
    o = "\n".join(o)
    return o


def genbplate():
    BPLATE = """
    
    """

    return BPLATE


def build():
    cpps = []
    obfiles = []

    open("/tmp/gen.main.cpp", "wb").write(genmain().encode("utf-8"))
    file = "/tmp/gen.main.cpp"
    print(file)
    ofile = "/tmp/%s.o" % file
    obfiles.append(ofile)
    cpps.append(file)
    cmd = [
        #'gcc',
        C,
        "-c",  ## do not call the linker
        "-fPIC",  ## position indepenent code
        "-o",
        ofile,
        os.path.join(srcdir, file),
    ]
    print(cmd)
    subprocess.check_call(cmd)

    os.system("ls -lh /tmp/*.o")

    ## finally call the linker,
    ## note: there's better linkers we could use here, like gold and mold

    cmd = (
        [
            #'ld',
            "g++",
            "-shared",
            "-o",
            "/tmp/obelisk.so",
        ]
        + obfiles
        + libs
    )

    print(cmd)
    subprocess.check_call(cmd)

    exe = "/tmp/obelisk"
    cmd = [
        C,
        "-o",
        exe,
    ]
    cmd += obfiles + libs

    print(cmd)

    subprocess.check_call(cmd)


build()
