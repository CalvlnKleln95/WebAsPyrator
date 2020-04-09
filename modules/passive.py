"""This file brings together several passive functions to analyse the target"""

import sys
import requests
from bs4 import BeautifulSoup
import modules

END = modules.COLORS["END"]
WHITE = modules.COLORS["WHITE"]
RED = modules.COLORS["RED"]
GREEN = modules.COLORS["GREEN"]
YELLOW = modules.COLORS["YELLOW"]
BLUE = modules.COLORS["BLUE"]
PURPLE = modules.COLORS["PURPLE"]

def get_headers_http(an_url, verbose=False):
    """Function to checks HTTP headers

        Args:
            an_url (string) : Target's URL
            verbose (optionnal boolean) : Enable or disable verbosity

        Return:
            None
    """

    print(PURPLE + "HTTP headers recovery..." + END + "\n")

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

def get_robots(an_url, verbose=False):
    """Function to get the robots.txt's content

        Args:
            an_url (string) : Target's URL
            verbose (optionnal boolean) : Enable or disable verbosity

        Return:
            None
    """

    print("\n" + PURPLE + "robots.txt recovery..." + END + "\n")

    robots_file = requests.get("{URL}/robots.txt".format(URL=an_url))

    if robots_file.status_code == 200:
        content = [item for item in robots_file.text.split("\n") if item != ""]

        for item in content:
            color = ""

            if item[:8] == "Disallow":
                color = BLUE
            else:
                color = WHITE

            if verbose:
                print("{color}{item}".format(color=color, item=item) + END)
            else:
                if color != WHITE:
                    print("{color}{item}".format(color=color, item=item) + END)
    else:
        print(YELLOW + "This site does not have a \"robots.txt file\"." + END + "\n", file=sys.stderr)
