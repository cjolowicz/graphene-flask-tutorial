import nox


nox.options.sessions = "lint", "mypy", "pytype", "tests"

package = "graphene_flask_tutorial"
locations = "src", "tests", "noxfile.py"


@nox.session(python="3.7")
def lint(session):
    """Lint using flake8."""
    session.install("flake8", "flake8-bugbear", "flake8-import-order", "black")
    session.run("black", "--check", *locations)
    session.run("flake8", *locations)


@nox.session(python="3.7")
def mypy(session):
    """Type-check using mypy."""
    session.install("mypy")
    session.run("mypy", *locations)


@nox.session(python="3.7")
def pytype(session):
    """Type-check using pytype."""
    session.install("pytype")
    session.run("pytype", "--disable=import-error", *locations)


@nox.session(python="3.7")
def tests(session):
    """Run the test suite."""
    env = {"VIRTUAL_ENV": session.virtualenv.location}
    session.run("poetry", "install", external=True, env=env)
    session.run("pytest", f"--cov={package}", *session.posargs)


@nox.session(python="3.7")
def black(session):
    """Run black code formatter."""
    session.install("black")
    session.run("black", *locations)
