#!/usr/bin/env python3
"""Analyze FFmpeg logs for errors and anomalies."""
import argparse, json, re
from pathlib import Path

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('logfile'); a=p.parse_args()
    text=Path(a.logfile).read_text(errors='ignore')
    report={
      'errors': len(re.findall(r'(?i)error|failed|invalid', text)),
      'dropped_frames': len(re.findall(r'drop', text)),
      'speed_samples': re.findall(r'speed=([0-9.]+)x', text),
      'bitrate_samples': re.findall(r'bitrate=([0-9.]+kbits/s)', text),
    }
    print(json.dumps(report, indent=2))
if __name__ == '__main__': main()
