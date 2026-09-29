# -*- coding: utf-8 -*-
"""Configura la consola para mostrar correctamente el castellano (UTF-8)."""

import sys


def configurar() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
            sys.stderr.reconfigure(encoding="utf-8")
        except Exception:
            pass
