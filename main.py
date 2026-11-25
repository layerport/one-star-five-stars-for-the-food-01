"""One-star alien review of Earth that still praises the food.

Writes a single sentence to /output/entry.txt: an alien tourist
hands Earth one star for its plague-spreading handshake habit,
then admits the dumplings were worth a second pandemic.
"""

import os

ENTRY = (
    "One star: your species greets strangers by shaking hands, "
    "which is how you spread your plagues, but the dumplings were "
    "so good I would risk a second pandemic for one more plate."
)


# Deterministic: the same sentence is written on every run.
def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
