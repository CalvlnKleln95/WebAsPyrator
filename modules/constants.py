"""This file brings together several useful consants."""

COLORS = {
    "END": "\033[0m\033[0m",
    "WHITE": "\033[1m\033[89m",
    "RED": "\033[1m\033[91m",
    "GREEN": "\033[1m\033[92m",
    "YELLOW": "\033[1m033[93m",
    "BLUE": "\033[1m\033[94m"
}

HTTP_HEADERS_LEAKS = [
    "Server",
    "X-Powered-By",
    "X-AspNet-Version",
    "X-AspNetMvc-Version"
]

HTTP_HEADERS_PROTECTION = [
    "Expect-CT",
    "Feature-Policy",
    "X-Frame-Options",
    "Public-Key-Pins",
    "Referrer-Policy",
    "X-XSS-Protection",
    "X-Content-Type-Options",
    "Content-Security-Policy",
    "Strict-Transport-Security",
    "Access-Control-Allow-Origin",
    "X-Permitted-Cross-Domain-Policies"
]
