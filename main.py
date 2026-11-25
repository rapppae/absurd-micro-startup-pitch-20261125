"""Absurd Micro-Startup Pitch-Off — make.fun entry.

Entry text: 136 characters (limit 200).
"""

import os

ENTRY = "We sell a subscription that rewrites your AI agent's error logs as polite apologies, so clients think the outage was a lifestyle choice."


def main():
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
