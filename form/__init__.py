__all__ = ("form_command", "form")

import os
import subprocess

def _form_cmd() -> list[str]:
    this_dir = os.path.abspath(os.path.dirname(__file__))
    packages = os.path.join(os.path.dirname(this_dir), "form-packages")
    if not packages.endswith(os.path.sep):
        packages += os.path.sep
    form_path = os.path.join(this_dir, "tform")
    tmp_dir = os.environ.get("TMPDIR", "/tmp")
    form_tmp = os.environ.get("FORMTMP", tmp_dir)
    form_tmpsort = os.environ.get("FORMTMPSORT", tmp_dir)
    return [form_path, "-I", packages, "-t", form_tmp, "-ts", form_tmpsort]

def form(*args: tuple[str]) -> None:
    """Run the form binary with the given arguments."""
    subprocess.check_call(form_command + list(args))

form_command: str = _form_cmd()
