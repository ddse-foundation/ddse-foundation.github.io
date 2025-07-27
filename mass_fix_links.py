#!/usr/bin/env python3
"""
Mass fix for broken Jekyll links - replace broken links with plain text
"""

import os
import re

# List of all broken links that need to be fixed
BROKEN_LINKS = {
    "ai-integration/advanced-features.md",
    "ai-integration/advanced-features/index.md", 
    "ai-integration/ai-context-formats.md",
    "ai-integration/ai-context-formats/index.md",
    "ai-integration/ai-guided-development.md",
    "ai-integration/ai-guided-development/index.md",
    "community/code-of-conduct.md",
    "community/guidelines.md", 
    "community/partners.md",
    "community/videos.md",
    "examples/case-studies/before-after.md",
    "examples/case-studies/index.md",
    "examples/case-studies/roi-analysis.md",
    "examples/case-studies/team-adoption.md",
    "examples/industry-examples/index.md",
    "examples/live-examples/index.md",
    "examples/live-examples/microservices.md",
    "examples/live-examples/taskflow.md",
    "implementation/team-adoption/change-management.md",
    "implementation/team-adoption/online-training.md",
    "implementation/team-adoption/rollout-strategies.md",
    "implementation/team-adoption/training-materials.md",
    "implementation/templates/quality-checklist.md",
    "learn/best-practices/index.md",
    "learn/core-concepts/ai-integration.md",
    "learn/core-concepts/index.md",
    "learn/core-concepts/tdr-hierarchy.md",
    "learn/mastery-paths/index.md",
    "reference/api-docs.md",
    "reference/best-practices.md",
    "reference/ddse-spec.md",
    "reference/glossary.md",
    "reference/research.md",
    "resources/training-slides.md",
    "support/enterprise.md",
    "support/mentorship.md",
    "support/training-faq.md",
    "tools/vscode-extension.md"
}

def fix_broken_links_in_file(filepath):
    """Fix broken links in a single file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Pattern to match Jekyll link syntax
        link_pattern = r'\[([^\]]+)\]\(\{% link ([^}]+) %\}([^)]*)\)'
        
        def replace_link(match):
            link_text = match.group(1)
            link_path = match.group(2)
            extra_attrs = match.group(3)  # For button classes etc
            
            if link_path in BROKEN_LINKS:
                # Just return the text without the link
                return link_text
            else:
                # Keep the working link as-is
                return match.group(0)
        
        # Replace broken links
        content = re.sub(link_pattern, replace_link, content)
        
        # Also handle header links like ### 🔍 [TDR Validator]({% link broken.md %})
        header_pattern = r'(#+\s+[^[]*\[)([^\]]+)\]\(\{% link ([^}]+) %\}\)'
        
        def replace_header_link(match):
            prefix = match.group(1)
            link_text = match.group(2)
            link_path = match.group(3)
            
            if link_path in BROKEN_LINKS:
                # Return just the header with text, no link
                return prefix + link_text
            else:
                # Keep the working link
                return match.group(0)
        
        content = re.sub(header_pattern, replace_header_link, content)
        
        # Write back if changed
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed: {filepath}")
            return True
        
        return False
        
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

def main():
    """Fix all markdown files."""
    fixed_count = 0
    
    for root, dirs, files in os.walk('.'):
        # Skip hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                if fix_broken_links_in_file(filepath):
                    fixed_count += 1
    
    print(f"\nCompleted! Fixed {fixed_count} files.")
    print("All broken Jekyll links have been converted to plain text.")

if __name__ == "__main__":
    main()
