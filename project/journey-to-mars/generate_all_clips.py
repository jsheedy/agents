#!/usr/bin/env python3
"""
Journey to Mars - Automated Grok Imagine Batch Generator
Reads all video clip prompts and generates them via Grok Imagine

Usage:
    python generate_all_clips.py [--api-key YOUR_KEY] [--output-dir ./generated]
"""

import os
import json
import glob
import time
import argparse
from pathlib import Path

# Configuration
PROMPTS_DIR = "./prompts/video-clips"
OUTPUT_DIR = "./generated"
DURATION = 6  # seconds per clip

def read_prompt_files():
    """Read all prompt markdown files in order."""
    prompt_files = sorted(glob.glob(f"{PROMPTS_DIR}/*.md"))
    prompts = []

    for filepath in prompt_files:
        filename = os.path.basename(filepath)
        clip_number = filename.split('-')[0]

        with open(filepath, 'r') as f:
            content = f.read().strip()

        prompts.append({
            'number': clip_number,
            'filename': filename,
            'filepath': filepath,
            'prompt': content,
            'output_filename': f"journey-to-mars-{clip_number}.mp4"
        })

    return prompts

def generate_batch_file(prompts):
    """Generate a batch JSON file for API submission."""
    batch = {
        'project': 'journey-to-mars',
        'total_clips': len(prompts),
        'duration_per_clip': DURATION,
        'total_duration': len(prompts) * DURATION,
        'clips': prompts
    }

    batch_file = './journey-to-mars-batch.json'
    with open(batch_file, 'w') as f:
        json.dump(batch, f, indent=2)

    print(f"✓ Batch file created: {batch_file}")
    return batch_file

def generate_prompts_txt(prompts):
    """Generate a simple text file with all prompts for easy copy-paste."""
    txt_file = './journey-to-mars-prompts.txt'

    with open(txt_file, 'w') as f:
        f.write("JOURNEY TO MARS - ALL PROMPTS FOR GROK IMAGINE\n")
        f.write("=" * 80 + "\n\n")

        for p in prompts:
            f.write(f"CLIP {p['number']}: {p['filename']}\n")
            f.write(f"OUTPUT: {p['output_filename']}\n")
            f.write("-" * 80 + "\n")
            f.write(f"{p['prompt']}\n")
            f.write("=" * 80 + "\n\n")

    print(f"✓ Text prompts file created: {txt_file}")
    return txt_file

def call_grok_imagine_api(prompt_data, api_key=None):
    """
    Call Grok Imagine API to generate video clip.

    NOTE: This is a placeholder - update with actual Grok Imagine API details.
    """
    # TODO: Replace with actual Grok Imagine API endpoint
    # Example structure (update based on actual API):

    if not api_key:
        print(f"⚠ No API key provided. Skipping API call for {prompt_data['number']}")
        return None

    # Placeholder for API call
    # import requests
    #
    # api_url = "https://api.grok.x.ai/imagine"  # Replace with actual endpoint
    # headers = {
    #     "Authorization": f"Bearer {api_key}",
    #     "Content-Type": "application/json"
    # }
    # payload = {
    #     "prompt": prompt_data['prompt'],
    #     "duration": DURATION,
    #     "output_format": "mp4"
    # }
    #
    # response = requests.post(api_url, headers=headers, json=payload)
    #
    # if response.status_code == 200:
    #     result = response.json()
    #     video_url = result.get('video_url')
    #     # Download video to output directory
    #     return video_url
    # else:
    #     print(f"✗ Error generating {prompt_data['number']}: {response.text}")
    #     return None

    print(f"⚠ API integration needed for {prompt_data['number']}")
    return None

def generate_shell_script(prompts, output_dir):
    """Generate a shell script for CLI-based Grok Imagine calls."""
    script_file = './generate_all_clips.sh'

    with open(script_file, 'w') as f:
        f.write("#!/bin/bash\n")
        f.write("# Journey to Mars - Grok Imagine Batch Generation Script\n\n")
        f.write("set -e  # Exit on error\n\n")
        f.write("# Configuration\n")
        f.write(f"OUTPUT_DIR=\"{output_dir}\"\n")
        f.write("DURATION=6\n\n")
        f.write("# Create output directory\n")
        f.write("mkdir -p \"$OUTPUT_DIR\"\n\n")
        f.write("echo \"Starting batch generation of 12 clips...\"\n")
        f.write("echo \"===================================\"\n\n")

        for i, p in enumerate(prompts, 1):
            f.write(f"# Clip {p['number']}: {p['filename']}\n")
            f.write(f"echo \"[{i}/{len(prompts)}] Generating {p['output_filename']}...\"\n")
            f.write(f"PROMPT_{p['number']}=$(cat <<'EOF'\n")
            f.write(f"{p['prompt']}\n")
            f.write("EOF\n")
            f.write(")\n\n")

            # Placeholder for actual Grok Imagine CLI command
            f.write(f"# TODO: Replace with actual Grok Imagine command\n")
            f.write(f"# grok imagine --prompt \"$PROMPT_{p['number']}\" --duration $DURATION --output \"$OUTPUT_DIR/{p['output_filename']}\"\n\n")
            f.write(f"# For now, just log the prompt\n")
            f.write(f"echo \"Prompt: $PROMPT_{p['number']}\"\n")
            f.write(f"echo \"---\"\n\n")

        f.write("echo \"===================================\"\n")
        f.write("echo \"Batch generation complete!\"\n")
        f.write(f"echo \"Output directory: $OUTPUT_DIR\"\n")

    os.chmod(script_file, 0o755)
    print(f"✓ Shell script created: {script_file}")
    print(f"  Run with: ./{script_file}")
    return script_file

def main():
    parser = argparse.ArgumentParser(description='Generate Journey to Mars video clips with Grok Imagine')
    parser.add_argument('--api-key', help='Grok Imagine API key')
    parser.add_argument('--output-dir', default=OUTPUT_DIR, help='Output directory for generated clips')
    parser.add_argument('--format', choices=['json', 'txt', 'shell', 'all'], default='all',
                        help='Output format for batch generation')
    parser.add_argument('--execute', action='store_true', help='Execute API calls immediately')

    args = parser.parse_args()

    # Set output directory
    output_dir = args.output_dir

    # Create output directory
    os.makedirs(output_dir, exist_ok=True)

    print("\n" + "="*80)
    print("JOURNEY TO MARS - GROK IMAGINE BATCH GENERATOR")
    print("="*80 + "\n")

    # Read all prompt files
    print("Reading prompt files...")
    prompts = read_prompt_files()
    print(f"✓ Found {len(prompts)} prompt files\n")

    # Generate output files based on format
    if args.format in ['json', 'all']:
        generate_batch_file(prompts)

    if args.format in ['txt', 'all']:
        generate_prompts_txt(prompts)

    if args.format in ['shell', 'all']:
        generate_shell_script(prompts, output_dir)

    print("\n" + "="*80)
    print("NEXT STEPS:")
    print("="*80)
    print("\n1. If Grok Imagine has a web interface:")
    print("   - Open journey-to-mars-prompts.txt")
    print("   - Copy each prompt and paste into Grok Imagine")
    print("   - Download clips to ./generated/")
    print("\n2. If Grok Imagine has a CLI:")
    print("   - Update generate_all_clips.sh with the correct command")
    print("   - Run: ./generate_all_clips.sh")
    print("\n3. If Grok Imagine has an API:")
    print("   - Update the call_grok_imagine_api() function in this script")
    print("   - Run: python generate_all_clips.py --api-key YOUR_KEY --execute")
    print("\n" + "="*80 + "\n")

    # Execute if requested
    if args.execute:
        print("\nExecuting API calls...")
        for i, prompt_data in enumerate(prompts, 1):
            print(f"[{i}/{len(prompts)}] Generating {prompt_data['output_filename']}...")
            result = call_grok_imagine_api(prompt_data, args.api_key)
            if result:
                print(f"✓ Generated: {result}")
            time.sleep(1)  # Rate limiting

if __name__ == "__main__":
    main()
