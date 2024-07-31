def genmain():
    o = []

    BPLATE = """
    return run();
    """

    o.extend(
        [
            '#include "Run.h"',
            "int main(int argc, char **argv) {",
            BPLATE,
        ]
    )

    # for arg in sys.argv:
    #    if arg.endswith(".dae"):
    #        "auto something = assimp.load(%s);" % arg

    o.append("}")
    o = "\n".join(o)
    return o
