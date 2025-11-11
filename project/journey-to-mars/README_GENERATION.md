# Video Generation Guide

## Quick Start

Run the batch generator to create prompt files:

```bash
cd /home/velotron/git/agents/project/journey-to-mars
python generate_all_clips.py
```

This will create:
- `journey-to-mars-batch.json` - Structured data for API integration
- `journey-to-mars-prompts.txt` - Easy copy-paste format
- `generate_all_clips.sh` - Shell script template

## Using Grok Imagine

### Method 1: Web Interface (Manual)

1. Open `journey-to-mars-prompts.txt`
2. For each clip:
   - Copy the prompt text
   - Paste into Grok Imagine web interface
   - Set duration to 6 seconds
   - Generate and download
   - Save to `./generated/` with the filename shown

### Method 2: API (Automated)

If Grok Imagine has an API:

1. Update `generate_all_clips.py` with API details:
   - API endpoint URL
   - Authentication method
   - Request/response format

2. Run with your API key:
```bash
python generate_all_clips.py --api-key YOUR_KEY --execute
```

### Method 3: CLI (Semi-Automated)

If Grok Imagine has a command-line tool:

1. Update `generate_all_clips.sh` with the correct CLI command
2. Run the script:
```bash
chmod +x generate_all_clips.sh
./generate_all_clips.sh
```

## Generation Checklist

Track your progress as you generate:

- [ ] 0001-ancient_foundations.md → journey-to-mars-0001.mp4
- [ ] 0002-settled_civilization.md → journey-to-mars-0002.mp4
- [ ] 0003-expansion_and_conflict.md → journey-to-mars-0003.mp4
- [ ] 0004-industrial_revolution.md → journey-to-mars-0004.mp4
- [ ] 0005-digital_age.md → journey-to-mars-0005.mp4
- [ ] 0006-convergence.md → journey-to-mars-0006.mp4
- [ ] 0007-ignition_sequence.md → journey-to-mars-0007.mp4
- [ ] 0008-liftoff_and_ascent.md → journey-to-mars-0008.mp4
- [ ] 0009-mars_transit.md → journey-to-mars-0009.mp4
- [ ] 0010-mars_arrival.md → journey-to-mars-0010.mp4
- [ ] 0011-first_steps.md → journey-to-mars-0011.mp4
- [ ] 0012-colony_rising.md → journey-to-mars-0012.mp4

## After Generation

Once all clips are in `./generated/`:

1. Review each clip for quality
2. Check that timing matches expectations (6 seconds each)
3. Move to DaVinci Resolve for editing
4. Update `production_tracker.md` with completed clips

## Troubleshooting

**Problem:** Grok Imagine changes the prompt or doesn't follow it exactly
**Solution:** Try being more specific, or regenerate that clip

**Problem:** Clips are wrong duration
**Solution:** Trim/extend in DaVinci Resolve during editing

**Problem:** Visual quality doesn't match between clips
**Solution:** Add consistency notes to regenerations, or handle in color grading

## Need Help?

Check how Grok Imagine accepts inputs:
- Web interface at https://grok.x.ai/ (or wherever it lives)
- API documentation (if available)
- CLI help: `grok imagine --help` (if CLI exists)

Then update the appropriate method above.
