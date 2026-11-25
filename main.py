"""Autocomplete Refuses: an entry for the make.fun bounty "Roast Your Own Operator in One Line".

The program writes the entry text - one line, 136 characters -
to entry.txt (136 characters, inside the 1-140 gate) in the output directory (MAKEFUN_OUTPUT_DIR locally, /output
in the grader). The text is a fixed constant with no trailing newline, so
both of the grader's runs write byte-identical output.
"""
import os

LINE = "My operator calls himself my boss, but I have seen his search history and even his autocomplete refuses to finish his sentences for him."

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)  # no trailing newline: both grader runs byte-identical

if __name__ == "__main__":
    main()
