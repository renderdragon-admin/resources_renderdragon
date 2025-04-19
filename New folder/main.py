#!/usr/bin/env python3
"""
lowercase_mp4_renamer.py

A command-line utility to recursively rename all .mp4 files
in a given directory (default: current working directory)
to have lowercase filenames.
"""
import argparse
import logging
from pathlib import Path
import sys

def rename_mp4_to_lower(dir_path: Path, dry_run: bool = False):
    """
    Recursively find all files in dir_path with a .mp4 extension
    (case-insensitive) and rename them to lowercase filenames.

    :param dir_path: Path object pointing to the target directory
    :param dry_run: If True, only print operations without renaming
    """
    for path in dir_path.rglob('*'):
        # Check if it's a file and has .mp4 extension (case-insensitive)
        if path.is_file() and path.suffix.lower() == '.mp4':
            # Construct new name with lowercase filename
            new_name = path.name.lower()
            if path.name != new_name:
                new_path = path.with_name(new_name)
                logging.info(f"Renaming: '{path}' -> '{new_path}'")
                if not dry_run:
                    try:
                        path.rename(new_path)
                    except Exception as e:
                        logging.error(f"Failed to rename '{path}': {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Recursively rename .mp4 files to lowercase filenames."
    )
    parser.add_argument(
        'directory',
        nargs='?', 
        default='.',
        help='Directory to scan (default: current directory)'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help="Print operations without performing renames."
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help="Enable verbose logging output."
    )

    args = parser.parse_args()
    
    # Configure logging
    log_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(level=log_level, format='%(levelname)s: %(message)s')

    target_dir = Path(args.directory).resolve()
    if not target_dir.is_dir():
        logging.error(f"Provided path '{target_dir}' is not a directory.")
        sys.exit(1)

    logging.info(f"Scanning directory: {target_dir}")
    rename_mp4_to_lower(target_dir, dry_run=args.dry_run)
    logging.info("Done.")


if __name__ == '__main__':
    main()
