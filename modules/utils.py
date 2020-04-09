"""This file brings together several useful functions."""

import argparse
import modules

END = modules.COLORS["END"]
WHITE = modules.COLORS["WHITE"]
RED = modules.COLORS["RED"]
GREEN = modules.COLORS["GREEN"]
YELLOW = modules.COLORS["YELLOW"]
BLUE = modules.COLORS["BLUE"]

def init_arguments():
    """Function to handle arguments passed to the script

        Args:
            None

        Return:
            None
    """

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-a",
        "--active",
        action="store_true",
        help="Use active mode to footprint the target"
    )
    
    parser.add_argument(
        "-u",
        "--url",
        help="The URL of a target server",
        required=True
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Increase the verbosity of the script"
    )

    return parser.parse_args()

def display_header():
    """Function to display the script header

        Args:
            None
        Return:
            None
    """

    print(WHITE + "###########################################################################" + END)
    print(WHITE + "#                                                                         #" + END)
    print(WHITE + "#                                                                         #" + END)
    print(WHITE + "#  _       __     __    ___         ____                   __             #" + END)        
    print(WHITE + "# | |     / /__  / /_  /   |  _____/ __ \__  ___________ _/ /_____  _____ #" + END)
    print(WHITE + "# | | /| / / _ \/ __ \/ /| | / ___/ /_/ / / / / ___/ __ `/ __/ __ \/ ___/ #" + END)
    print(WHITE + "# | |/ |/ /  __/ /_/ / ___ |(__  ) ____/ /_/ / /  / /_/ / /_/ /_/ / /     #" + END)
    print(WHITE + "# |__/|__/\___/_.___/_/  |_/____/_/    \__, /_/   \__,_/\__/\____/_/      #" + END)
    print(WHITE + "#                                     /____/                              #" + END)
    print(WHITE + "#                                                                         #" + END)
    print(WHITE + "#                                                                         #" + END)
    print(WHITE + "#                            by  CalvlnKleln95                            #" + END)
    print(WHITE + "#                                                                         #" + END)
    print(WHITE + "#                                                                         #" + END)
    print(WHITE + "###########################################################################" + END + "\n")
