#!/usr/bin/env python3
import click
from assistant import start
from test import echo_said

@click.command()
@click.option('--debug', is_flag=True, help="Run Lyra in debug mode")
def cli(debug):
    """
    Lyra – Linux Voice-Controlled Personal Assistant
    """
    if debug:
        print("[DEBUG] Running Lyra in debug mode")
    start(debug)

if __name__ == "__main__":
    cli()
