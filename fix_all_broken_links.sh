#!/bin/bash

# Script to replace all broken link references with GitHub links or remove them

echo "Replacing all broken references..."

# Replace community references
find . -name "*.md" -type f -exec sed -i 's|{% link community/index.md %}|https://github.com/ddse-foundation/ddse-foundation/discussions|g' {} +
find . -name "*.md" -type f -exec sed -i 's|{% link community/guidelines.md %}|https://github.com/ddse-foundation/ddse-foundation/discussions|g' {} +
find . -name "*.md" -type f -exec sed -i 's|{% link community/events.md %}|https://github.com/ddse-foundation/ddse-foundation/discussions|g' {} +

# Replace support references
find . -name "*.md" -type f -exec sed -i 's|{% link support/index.md %}|https://github.com/ddse-foundation/ddse-foundation/issues|g' {} +
find . -name "*.md" -type f -exec sed -i 's|{% link support/contact.md %}|https://github.com/ddse-foundation/ddse-foundation/issues|g' {} +
find . -name "*.md" -type f -exec sed -i 's|{% link support/faq.md %}|https://github.com/ddse-foundation/ddse-foundation/issues|g' {} +

# Replace tools references  
find . -name "*.md" -type f -exec sed -i 's|{% link tools/index.md %}|https://github.com/ddse-foundation/ddse-foundation/tree/main/tools|g' {} +
find . -name "*.md" -type f -exec sed -i 's|{% link tools/validation.md %}|https://github.com/ddse-foundation/ddse-foundation/tree/main/tools|g' {} +
find . -name "*.md" -type f -exec sed -i 's|{% link tools/cli.md %}|https://github.com/ddse-foundation/ddse-foundation/tree/main/tools|g' {} +

# Replace ai-integration references
find . -name "*.md" -type f -exec sed -i 's|{% link ai-integration/index.md %}|https://github.com/ddse-foundation/ddse-foundation/tree/main/ai|g' {} +
find . -name "*.md" -type f -exec sed -i 's|{% link ai-integration/prompts.md %}|https://github.com/ddse-foundation/ddse-foundation/tree/main/ai|g' {} +

# Replace integration-guides references
find . -name "*.md" -type f -exec sed -i 's|{% link implementation/integration-guides/index.md %}|https://github.com/ddse-foundation/ddse-foundation/tree/main/integrations|g' {} +
find . -name "*.md" -type f -exec sed -i 's|{% link implementation/integration-guides/github.md %}|https://github.com/ddse-foundation/ddse-foundation/tree/main/integrations|g' {} +
find . -name "*.md" -type f -exec sed -i 's|{% link implementation/integration-guides/jira.md %}|https://github.com/ddse-foundation/ddse-foundation/tree/main/integrations|g' {} +
find . -name "*.md" -type f -exec sed -i 's|{% link implementation/integration-guides/cicd.md %}|https://github.com/ddse-foundation/ddse-foundation/tree/main/integrations|g' {} +

echo "Done replacing all broken references!"
