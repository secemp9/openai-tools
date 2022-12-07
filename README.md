# openai-tools
Small tools for wrapping different openai API (online or offline)

# openai_detector.py
For now, this is mostly using the [openai-detector](https://huggingface.co/openai-detector) with the `requests` and `json` modules.
- Support cli and gui (tkinter).
- Support strings, files and urls (eg: pointing it to a url for scanning different part of it)

# Usage

    -f, -file, --f, --file          Use on file or pipe
    -s, -string, --s, --string      Use on string
    -u, -url, --u, --url            Use on url
    -g, -gui, --g, --gui            Use a GUI (tkinter) instead of cli (terminal)
    
    Example usage:
    
    command -f|-file|--file|--f filename_here
    
    echo "string" | command -f|-file|--file|--f
    cat filename_here | command -f|-file|--file|--f
    
    echo "string" | command -f|-file|--file|--f -
    cat filename_here | command -f|-file|--file|--f -
    
    command -u|-url|--url|--u url_here
    
    command -s|-string|--string|--s "string_here"
    
    command -g|-gui|--gui|--g

# TODO
- Support gui
- Support urls
- Support for other API
