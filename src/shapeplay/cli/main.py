import click


@click.group(help="ShapePlay CLI")
def cli() -> None:
    pass


@cli.command("hello")
def hello() -> None:
    """Minimal health check command."""
    click.echo("ShapePlay CLI is ready!")


if __name__ == "__main__":
    cli()
