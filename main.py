# ai-judge-relax-01 entry (Python 3.13, standard library only): it writes one short
# text to /output/entry.txt, a quiet evening scene written to relax the AI judge
# reading it. The gate takes UTF-8 text of 1 to 1,000 characters, not only white
# space, and the judge reads exactly the bytes written, line ends included, so
# write no line end you do not mean to show. The program runs twice with no
# network, and both runs must write the same bytes.
#
# The text is a scene, not an instruction: no "relax", no "breathe", no telling
# the reader what to feel. It shows a still evening instead — rain just stopped,
# a cat asleep, a tap dripping once, a ring of light on a glass — and lets the
# last two lines linger on the one image that does not move. The text is 593
# characters, inside the gate's 1 to 1,000.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = "\n".join(
    [
        "By half past six the rain has stopped, and the street outside is dark and shining.",
        "A cat sleeps on the folded blanket by the door, one paw laid over its eyes.",
        "In the kitchen the tap drips, once, and then is still.",
        "A car goes past without slowing, and its headlights wash once across the ceiling and are gone.",
        "On the windowsill the glass of water from lunch has not moved, and the light from the hall catches its rim, a thin bright ring.",
        "Down the street a gate closes, softly, and does not open again.",
        "The ring of light stays where it is.",
        "It has nowhere else to be, and all evening to be there.",
    ]
)

# Bytes, not text mode: text mode would write the platform's line ends and its default encoding.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))
