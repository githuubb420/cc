from pathlib import Path
from . import *


def load_module(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        import importlib
        import sys
        from pathlib import Path

        path = Path(f"main/plug/{shortname}.py")
        name = f"main.plug.{shortname}"
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        print("Starting Your Assistant Bot.")
        print(f"Assistant Sucessfully imported {shortname}")
    else:
        import importlib
        import sys
        from pathlib import Path

        path = Path(f"main/plug/{shortname}.py")
        name = f"main.plug.{shortname}"
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        sys.modules[f"main.plug{shortname}"] = mod
        print(f"import {shortname}")
