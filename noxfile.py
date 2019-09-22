import nox


package = "graphene_flask_tutorial"


@nox.session(python="3.7")
def tests(session):
    """Run the test suite."""
    env = {"VIRTUAL_ENV": session.virtualenv.location}
    session.run("poetry", "install", external=True, env=env)
    session.run("pytest", f"--cov={package}", *session.posargs)
