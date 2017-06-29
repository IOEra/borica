# Skeleton of a CLI

import click

import borica


@click.command('borica')
@click.argument('count', type=int, metavar='N')
def cli(count):
    """Echo a value `N` number of times"""
    for i in range(count):
        click.echo(borica.has_legs)
