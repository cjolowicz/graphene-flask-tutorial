import nox


package = "graphene_flask_tutorial"
locations = "src", "tests", "noxfile.py"


@nox.session(python="3.7")
def lint(session):
    """Lint using flake8."""
    session.install("flake8", "flake8-bugbear", "flake8-import-order", "black")
    session.run("black", "--check", *locations)
    session.run("flake8", *locations)


@nox.session(python="3.7")
def tests(session):
    """Run the test suite."""
    env = {"VIRTUAL_ENV": session.virtualenv.location}
    session.run("poetry", "install", external=True, env=env)
    session.run("pytest", f"--cov={package}", *session.posargs)
