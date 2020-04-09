# WebAsPyrator

## Project presentation

This project aims to facilitate fingerprinting on a web server.

It is presented as a command line script that allows you to choose between passive and active mode.

Passive mode allows you to perform mundane queries that a legitimate user could perform. The latter allow the collection of several pieces of information such as the technologies used by the site (web server, CMS, languages, etc.) as well as their version.

Active mode allows you to perform the same queries as passive mode, but also performs Nmap scanning, SSL scanning, etc.

Thus, the fingerprinting, which can sometimes take a certain amount of time, is automated and requires only the entry of the URL of the targeted site.
