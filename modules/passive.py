"""This file brings together several passive functions to analyse the target"""

import requests
import modules

END = modules.COLORS["END"]
WHITE = modules.COLORS["WHITE"]
RED = modules.COLORS["RED"]
GREEN = modules.COLORS["GREEN"]
YELLOW = modules.COLORS["YELLOW"]
BLUE = modules.COLORS["BLUE"]

def get_headers_http(an_url, verbose=False):
    """Function to checks HTTP headers

        Args:
            an_url (string) : Target's URL
            verbose (optionnal boolean) : Enable or disable verbosity

        Return:
            None
    """

    print(WHITE + "HTTP headers recovery..." + END + "\n")

    headers = requests.get(an_url).headers

    for key, value in headers.items():
        color = ""

        if key in modules.HTTP_HEADERS_LEAKS:
            color += RED
        elif key in modules.HTTP_HEADERS_PROTECTION:
            color += GREEN
        else:
            color += WHITE

        if verbose:
            print("{color}{key} : {value}".format(color=color, key=key, value=value) + END)
        else:
            if color != WHITE:
                print("{color}{key} : {value}".format(color=color, key=key, value=value) + END)
