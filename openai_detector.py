import requests
import json
import argparse
import sys
import os
import errno


def detector(x, url='https://huggingface.co/openai-detector/', ):
    data = {'text': str(x)}
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    result = requests.post(url, data=json.dumps(data), headers=headers)

    result_decoded = result.content.decode()
    result_dict = json.loads(result_decoded)

    total_token = result_dict["all_tokens"]
    used_token = result_dict["used_tokens"]
    real_probability = result_dict["real_probability"]
    fake_probability = result_dict["fake_probability"]

    print("This input has", format(total_token), "total token(s)")
    print("This input has", format(used_token), "used token(s)")
    print("This input is", format(real_probability, '.2%'), "real")
    print("This input is", format(fake_probability, '.2%'), "fake")


def gui():
    print('gui not built yet...')


def u():
    print("url not supported yet")


def h():
    print("""openai detector wrapper:
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
    """)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(add_help=False)

    parser.add_argument(
        '-h', '--h', '-help', '--help',
        default='', action="store_true",
    )

    parser.add_argument(
        '-f', '--f', '-file', '--file',
        default='', action="store_true",
    )

    parser.add_argument(
        '-s', '--s', '-string', '--string',
        default='',
    )

    parser.add_argument(
        '-u', '--u', '-url', '--url',
        default='',
    )

    parser.add_argument(
        '-g', '--g', '-gui', '--gui', action='store_true', default='',
    )

    parser.add_argument("PARAMS", nargs="*")  # for supporting pipe/stdout with and without "-"

    args = parser.parse_args()
    total_args = args.__dict__
    for i in total_args:
        if i == "f" and total_args[i] != "":
            if not sys.stdin.isatty():
                args.PARAMS.extend(sys.stdin.read().splitlines())
                if total_args["PARAMS"][0] == "-" and len(total_args["PARAMS"]) >= 2:
                    detector(total_args["PARAMS"][1])
                else:
                    detector(total_args["PARAMS"][0])
            else:
                # check if file exist or throw an error
                if os.path.isfile(total_args["PARAMS"][0]) and os.access(total_args["PARAMS"][0], os.R_OK):
                    with open(total_args["PARAMS"][0], "r") as f:
                        detector(f.read())
                else:
                    # https://stackoverflow.com/a/36077407/12349101
                    print(FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), total_args["PARAMS"][0]))
        elif i == "u" and total_args[i] != "":
            u()
        elif i == "s" and total_args[i] != "":
            detector(total_args[i])
        elif i == "g" and total_args[i] != "":
            gui()
        elif i == "h" and total_args[i] != "":
            h()
