import click
import os
from shutil import copyfile
import pytest
import requests
from dotenv import load_dotenv

@click.group()
def cli():
    click.echo('Welcome to AoC 2024 fun!')
    load_dotenv('.env')

@cli.command()
@click.argument('day', type=click.INT)
def new(day: int):
    if os.path.exists(f'.\\day_{day}'):
        click.echo(f'Day {day} already exists!')
        return
    
    os.makedirs(f'.\\day_{day}', exist_ok=True)
    template = open('.\\util\\day_template.py', 'r').read()
    for i in [1,2]:
        template = template.replace('day_i', f'day_{day}')
        open(f'.\\day_{day}\\solve_{i}.py', 'w').write(template)

    data_url = f"https://adventofcode.com/2024/day/{day}/input"
    data = requests.get(data_url, cookies={'session': os.getenv('AOC_SESSION')})
    with open(f'.\\day_{day}\\data.txt', 'w') as f:
        f.write(data.text.rstrip())
    
    click.echo(f'Created day {day}!')

@cli.command()
@click.argument('day', type=click.INT)
def run(day: int):
    click.echo(f'Running day {day}...')
    # os.chdir('.\\day_1')
    click.echo(f'Star 1:')
    os.system(f'python .\\day_{day}\\solve_1.py')
    click.echo(f'Star 2:')
    os.system(f'python .\\day_{day}\\solve_2.py')

@cli.command()
def runall():
    click.echo('Running all days...')
    for i in range(1, 26):
        click.echo(f'Day {i}:')
        if os.path.exists(f'.\\day_{i}'):
            os.system(f'python .\\day_{i}\\solve_1.py')
            os.system(f'python .\\day_{i}\\solve_2.py')

@cli.command()
@click.argument('day', type=click.INT)
def test(day: int):
    click.echo(f'Testing day {day}...')
    pytest.main([f'.\\day_{day}\\solve_1.py', f'.\\day_{day}\\solve_2.py'])

if __name__ == '__main__':
    cli()