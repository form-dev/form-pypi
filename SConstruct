import enscons
import os
import packaging.tags
import subprocess
import sys
import toml

def get_universal_platform_tag():
    """Return the wheel tag for universal Python 3, but specific platform."""
    tag = next(packaging.tags.sys_tags())
    return f"py3-none-{tag.platform}"

pyproject = toml.load("pyproject.toml")

env = Environment(
    tools=["default", "packaging", enscons.generate],
    PACKAGE_METADATA=pyproject["project"],
    WHEEL_TAG=get_universal_platform_tag(),
    ENV=os.environ
)

hepware = env.Command(
    "hepware/Makefile", [], "git clone https://github.com/magv/hepware"
)
hepware_form = env.Command(
    f"hepware/form.done", [hepware], "make -C hepware -j6 form.done"
)
env.Precious(hepware)
env.Precious(hepware_form)

files = [
    File("form-packages/README.md"),
    File("form/__main__.py"),
    env.Command(
        f"form/tform",
        [hepware_form],
        ["cp hepware/bin/form form/tform", "strip form/tform"],
    ),
]

platformlib = env.Whl("platlib", files, root="")
bdist = env.WhlFile(source=platformlib)

env.Alias("dist", bdist)
