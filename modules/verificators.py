"""This file brings together several verification functions"""

import sys
import requests
import modules

END = modules.COLORS["END"]
WHITE = modules.COLORS["WHITE"]
RED = modules.COLORS["RED"]
GREEN = modules.COLORS["GREEN"]
YELLOW = modules.COLORS["YELLOW"]
BLUE = modules.COLORS["BLUE"]

def verify_url(an_url):
    """Function to check the validity of URL

        Args:
            an_url (string) : Target's URL

        Return:
            None
    """

    try:
        request = requests.get(an_url)
    except requests.exceptions.MissingSchema:
        print(RED + "Invalid URL \"{URL}\"".format(URL=an_url) + END, file=sys.stderr)
        print(RED + "Perhaps you meant \"https://{URL}\" ?".format(URL=an_url) + END, file=sys.stderr)
    except requests.exceptions.ConnectionError:
        print(RED + "The site \"{URL}\" can’t be reached".format(URL=an_url) + END, file=sys.stderr)
