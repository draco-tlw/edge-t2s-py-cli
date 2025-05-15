import asyncio
import os

from edge_t2s_py import t2s


async def main():
    narrators = [
        "fa-IR-DilaraNeural",
        "fa-IR-FaridNeural",
        "en-US-AvaNeural",
        "en-US-AndrewNeural",
        "en-US-AnaNeural",
        "en-US-AriaNeural",
        "en-US-GuyNeural",
        "en-GB-LibbyNeural",
        "en-GB-MaisieNeural",
        "en-GB-RyanNeural",
        "en-GB-SoniaNeural",
        "en-GB-ThomasNeural",
    ]

    print("edge-t2s-py-cli")
    print("choose a narrator")
    for i, n in enumerate(narrators):
        print(f"[{i}]: {n}")

    try:
        narrator_i = int(input("=> ").strip())
        if narrator_i < 0 or narrator_i >= len(narrators):
            raise ValueError("invalid narrator index")
        narrator = narrators[narrator_i]
    except ValueError:
        print("Invalid input")
        return

    try:
        rate = int(input("rate (in %): ").strip())
        if rate < -100 or rate > 100:
            raise ValueError("rate out of range")
    except ValueError:
        print("Invalid rate")
        return

    try:
        pitch = int(input("pitch (in %): ").strip())
        if pitch < -100 or pitch > 100:
            raise ValueError("pitch out of range")
    except ValueError:
        print("Invalid pitch")
        return

    text = input("text: ").strip()
    if not text:
        print("No text provided")
        return

    try:
        audio_data = await t2s(text, narrator, rate, pitch)
    except Exception as e:
        print(f"Error while generating TTS: {e}")
        return

    output_path = input("output path (default = output/speech.mp3): ").strip()
    if not output_path:
        output_path = "output/speech.mp3"

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "wb") as f:
        f.write(audio_data)

    print(f"Audio saved to: {output_path}")


asyncio.run(main())
