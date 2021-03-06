#!/usr/bin/env python3

"""This script allows you to perform an automated fingerprinting on a web server."""

import modules

ARGS = modules.init_arguments()

modules.display_header()

modules.verify_url(ARGS.url)

if ARGS.verbose:
	modules.get_headers_http(ARGS.url, verbose=True)
	modules.get_robots(ARGS.url, verbose=True)
	modules.get_meta_tag_generator(ARGS.url)
else:
	modules.get_headers_http(ARGS.url)
	modules.get_robots(ARGS.url)
	modules.get_meta_tag_generator(ARGS.url)
