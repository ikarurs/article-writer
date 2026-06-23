#!/usr/bin/env python3
"""Download one public URL to a file and print size plus SHA-256."""

from __future__ import annotations

import argparse
import hashlib
import os
import sys
import subprocess
import tempfile
import urllib.error
import urllib.request
from pathlib import Path


def parse_header(value: str) -> tuple[str, str]:
    if "=" not in value:
        raise argparse.ArgumentTypeError("headers must be NAME=VALUE")
    name, header_value = value.split("=", 1)
    if not name.strip():
        raise argparse.ArgumentTypeError("header name is empty")
    return name.strip(), header_value


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("output")
    parser.add_argument("--header", action="append", type=parse_header, default=[])
    parser.add_argument("--timeout", type=float, default=60.0)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        assert parse_header("Accept=text/csv") == ("Accept", "text/csv")
        return 0

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)

    if os.name == "nt" and args.url.startswith("https://"):
        # ponytail: native curl avoids bundled-Python OpenSSL failures on Windows.
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp_path = Path(tmp.name)
        command = [
            "curl.exe",
            "--location",
            "--fail",
            "--silent",
            "--show-error",
            "--ssl-no-revoke",
            "--max-time",
            str(args.timeout),
        ]
        for name, value in args.header:
            command.extend(["--header", f"{name}: {value}"])
        command.extend(["--output", str(tmp_path), args.url])
        result = subprocess.run(command, text=True, capture_output=True)
        if result.returncode != 0:
            tmp_path.unlink(missing_ok=True)
            print(result.stderr.strip() or f"error: curl exited {result.returncode}", file=sys.stderr)
            return 1
        data = tmp_path.read_bytes()
        tmp_path.unlink(missing_ok=True)
    else:
        request = urllib.request.Request(args.url, headers=dict(args.header))
        try:
            with urllib.request.urlopen(request, timeout=args.timeout) as response:
                status = getattr(response, "status", 200)
                if status < 200 or status >= 300:
                    print(f"error: HTTP {status}", file=sys.stderr)
                    return 1
                data = response.read()
        except urllib.error.HTTPError as error:
            print(f"error: HTTP {error.code} {error.reason}", file=sys.stderr)
            return 1
        except urllib.error.URLError as error:
            print(f"error: {error.reason}", file=sys.stderr)
            return 1

    output.write_bytes(data)
    digest = hashlib.sha256(data).hexdigest()
    print(f"{output.as_posix()}\t{len(data)}\t{digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
