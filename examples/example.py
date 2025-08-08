"""Example usage of the text-to-curses library."""

import curses
from text_to_curses import TextRenderer, display_document


def basic_example():
    """Basic usage example."""
    # Simple one-liner
    display_document("test.docx")


def advanced_example():
    """Advanced usage with custom handling."""
    renderer = TextRenderer("test.docx")
    
    def custom_display(stdscr):
        # Display document
        renderer.display(stdscr)
        
        # Add custom overlay
        stdscr.addstr(0, 0, "Press any key to exit", curses.A_REVERSE)
        stdscr.refresh()
        stdscr.getch()
    
    curses.wrapper(custom_display)


def multi_document_example():
    """Example with multiple documents."""
    documents = ["doc1.docx", "doc2.pdf", "doc3.html"]
    renderers = []
    
    for doc in documents:
        try:
            renderers.append(TextRenderer(doc))
        except Exception as e:
            print(f"Failed to load {doc}: {e}")
    
    def slideshow(stdscr):
        current = 0
        while True:
            stdscr.clear()
            if renderers:
                renderers[current].display(stdscr, clear_screen=False)
                stdscr.addstr(0, 0, f"Document {current + 1}/{len(renderers)} - Press 'n' for next, 'q' to quit", curses.A_REVERSE)
            else:
                stdscr.addstr(0, 0, "No documents loaded", curses.A_REVERSE)
            
            stdscr.refresh()
            key = stdscr.getch()
            
            if key == ord('q'):
                break
            elif key == ord('n') and renderers:
                current = (current + 1) % len(renderers)
    
    curses.wrapper(slideshow)


if __name__ == "__main__":
    # Run basic example
    basic_example()
