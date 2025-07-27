#!/bin/bash

# Script to replace all team-adoption link references with GitHub links

echo "Replacing all team-adoption references..."

# Replace all {% link implementation/team-adoption/xxx.md %} with GitHub links
find . -name "*.md" -type f -exec sed -i 's|{% link implementation/team-adoption/index.md %}|https://github.com/ddse-foundation/ddse-foundation/blob/main/adoption/README.md|g' {} +
find . -name "*.md" -type f -exec sed -i 's|{% link implementation/team-adoption/playbook.md %}|https://github.com/ddse-foundation/ddse-foundation/blob/main/adoption/README.md|g' {} +
find . -name "*.md" -type f -exec sed -i 's|{% link implementation/team-adoption/training.md %}|https://github.com/ddse-foundation/ddse-foundation/blob/main/adoption/README.md|g' {} +
find . -name "*.md" -type f -exec sed -i 's|{% link implementation/team-adoption/case-studies.md %}|https://github.com/ddse-foundation/ddse-foundation/blob/main/adoption/README.md|g' {} +
find . -name "*.md" -type f -exec sed -i 's|{% link implementation/team-adoption/toolkit.md %}|https://github.com/ddse-foundation/ddse-foundation/blob/main/adoption/README.md|g' {} +
find . -name "*.md" -type f -exec sed -i 's|{% link implementation/team-adoption/online-training.md %}|https://github.com/ddse-foundation/ddse-foundation/blob/main/adoption/README.md|g' {} +
find . -name "*.md" -type f -exec sed -i 's|{% link implementation/team-adoption/change-management.md %}|https://github.com/ddse-foundation/ddse-foundation/blob/main/adoption/README.md|g' {} +

echo "Done replacing team-adoption references!"
