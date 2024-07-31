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
