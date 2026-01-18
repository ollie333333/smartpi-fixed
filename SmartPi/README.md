# SmartPi

Offline AI chatbot for Raspberry Pi 3B+ with a ChatGPT-style GUI.

## Installation

1. Create and activate a Python virtual environment:
\`\`\`bash
python3 -m venv venv
source venv/bin/activate
\`\`\`

2. Install SmartPi:
\`\`\`bash
pip install .
\`\`\`

3. Run the chat interface:
\`\`\`bash
smartpi-chat
\`\`\`

## Customizing Responses

- Open \`smartpi/text_model.py\`.
- Add new text patterns inside \`self.responses\`.

