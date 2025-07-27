#!/usr/bin/env python3
"""
Script to systematically identify and fix broken Jekyll links.
"""

import os
import re
import glob

def find_all_files():
    """Find all markdown files in the site."""
    md_files = []
    for root, dirs, files in os.walk('.'):
        # Skip hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))
    return md_files

def extract_link_references(content):
    """Extract all Jekyll link references from content."""
    pattern = r'\{% link ([^}]+) %\}'
    matches = re.findall(pattern, content)
    return matches

def file_exists(filepath):
    """Check if a file exists."""
    return os.path.exists(filepath)

def main():
    # Get all markdown files
    md_files = find_all_files()
    existing_files = set(md_files)
    
    # Normalize paths for comparison
    existing_files = {f.lstrip('./') for f in existing_files}
    
    # Track all link references
    all_links = set()
    broken_links = set()
    
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
                links = extract_link_references(content)
                
                for link in links:
                    all_links.add(link)
                    if link not in existing_files:
                        broken_links.add(link)
                        print(f"BROKEN: {link} (referenced in {md_file})")
        except Exception as e:
            print(f"Error reading {md_file}: {e}")
    
    print(f"\nSUMMARY:")
    print(f"Total link references found: {len(all_links)}")
    print(f"Broken links: {len(broken_links)}")
    print(f"Working links: {len(all_links) - len(broken_links)}")
    
    print(f"\nBROKEN LINKS:")
    for link in sorted(broken_links):
        print(f"  {link}")
    
    print(f"\nEXISTING FILES:")
    for file in sorted(existing_files):
        print(f"  {file}")

if __name__ == "__main__":
    main()
