# Module:   docs
# Date:     03rd April 2013
# Author:   James Mills, j dot mills at griffith dot edu dot au

"""Documentation Tasks"""

from fabric.api import lcd, local, task

from .utils import pip, requires


PACKAGE = "circuits"


@task()
@requires("sphinx-apidoc")
def api():
    """Generate the API Documentation"""

    if PACKAGE is not None:
        local("sphinx-apidoc -f -T -o docs/source/api {0:s}".format(PACKAGE))


@task()
@requires("make")
def clean():
    """Delete Generated Documentation"""

    with lcd("docs"):
        local("make clean")


@task(default=True)
@requires("make")
def build(**options):
    """Build the Documentation"""

    pip(requirements="docs/requirements.txt")

    with lcd("docs"):
        local("make html")


@task()
def view(**options):
    """View the Documentation"""

    with lcd("docs"):
        import webbrowser
        webbrowser.open_new_tab("build/html/index.html")
