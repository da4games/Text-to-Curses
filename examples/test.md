# Test Document

This is a simple test document for the **text-to-curses** library.

## Features

- Supports multiple formats
- Extracts colors from documents  
- Displays in terminal with curses

## Usage

```python
from text_to_curses import TextRenderer
import curses

renderer = TextRenderer("document.docx")
curses.wrapper(lambda stdscr: renderer.display_and_wait(stdscr))
```

### Supported Formats

1. **DOCX** - Word documents with color support
2. **PDF** - Text and color extraction
3. **HTML** - Inline CSS color support
4. **RTF** - Rich text (converted to plain text)
5. **TXT** - Plain text files
6. **MD** - Markdown (this file!)

Enjoy using the library!
