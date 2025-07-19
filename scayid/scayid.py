#!/usr/bin/env python3
"""
👤 Author & Rights
Tool Name: Scayid
Author: Scayar
All rights reserved © Scayar
🌐 Official Channels
🌍 Website: scayar.com
💬 Telegram Group: @im_scayar
📧 Email: Scayar.exe@gmail.com
☕ Buy Me a Coffee: buymeacoffee.com/scayar
"""
import argparse
from core.colours import green, end, bad, yellow, white, sarcastic
from core.simple import Person, _scayid_full_output
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress
import time

console = Console()
version = '0.0.1'

BANNER = """
[bold green]
               _,.---.---.---.--.._ 
            _.-' `--.`---.`---'-. _,`--.._
           /`--._ .'.     `.     `,`-.`-._\
          ||   \  `.`---.__`__..-`. ,'`-._/
     _  ,`\ `-._\   \    `.    `_.-`-._,``-.
  ,`   `-_ \/ `-.`--.\    _\_.-'\__.-`-.`-._`.
 (_.o> ,--. `._/'--.-`,--`  \_.-'       \`-._ \
  `---'    `._ `---._/__,----`           `-. `-\
            /_, ,  _..-'                    `-._\
            \_, \/ ._(
             \_, \/ ._\
              `._,\/ ._\
                `._// ./`-._
         Scayid      `-._-_-_.-'
[/bold green]
"""

HELP_PANEL = Panel("""
[bold cyan]Usage:[/bold cyan] scayid.py [options]

[bold cyan]Options:[/bold cyan]
  -g   Generate a new identity
  -p   Generate with profile picture
  -r   Set role/profession (requires value)
  -n   Set nationality (requires value)
  -s   Deploy social media presence
  -x   Hack mode (fun/animation)
  -b   Show the Scayid banner
  -a   About info
  -h   Show this help message
""", title="[bold green]Scayid CLI[/bold green]", style="bold magenta")

def args_func():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('-g', help='Generate a new identity', dest='simple', action='store_true')
    parser.add_argument('-p', help='Generate with profile picture', dest='simplewithpic', action='store_true')
    parser.add_argument('-r', help='Set role/profession', dest='profession')
    parser.add_argument('-n', help='Set nationality', dest='nationality')
    parser.add_argument('--gender', choices=['male', 'female'], help='Gender of the sock puppet', dest='gender')
    parser.add_argument('-f', help='Output format', dest='format', choices=['txt', 'json', 'csv'], default='txt')
    parser.add_argument('-b', help='Show the Scayid banner', dest='bannerfunction', action='store_true')
    parser.add_argument('-a', help='Show author and rights info', dest='about', action='store_true')
    parser.add_argument('-x', help='Initiate hack mode', dest='hack', action='store_true')
    parser.add_argument('-h', '--help', action='store_true', help='Show this help message')
    return parser.parse_args()

def bannerfunction():
    console.print(BANNER)

def about():
    console.print(Panel("""
👤 Author & Rights
Tool Name: Scayid
Author: Scayar
All rights reserved © Scayar
🌐 Official Channels
🌍 Website: scayar.com
💬 Telegram Group: @im_scayar
📧 Email: Scayar.exe@gmail.com
☕ Buy Me a Coffee: buymeacoffee.com/scayar
""", title="[bold green]About Scayid[/bold green]", style="bold magenta"))

def hack_mode():
    console.print(Panel("[bold red]HACK MODE INITIATED...[/bold red]", style="bold red"))
    with Progress() as progress:
        task = progress.add_task("[cyan]Bypassing firewalls...", total=100)
        for i in range(100):
            time.sleep(0.01)
            progress.update(task, advance=1)
    console.print("[bold green]Access Granted! Welcome, Operator.[/bold green]")

def main():
    args = args_func()
    if args.help:
        console.print(HELP_PANEL)
        return
    if args.about:
        about()
        return
    if args.hack:
        hack_mode()
        return
    if args.simple:
        bannerfunction()
        person = Person(target_gender=args.gender, nationality=args.nationality)
        _scayid_full_output(person, args.format)
        return
    if args.simplewithpic:
        bannerfunction()
        person = Person(target_gender=args.gender, nationality=args.nationality)
        _scayid_full_output(person, args.format)
        return
    if args.profession:
        bannerfunction()
        # simplewithprofession(args.profession, nationality=args.nationality, output_format=args.format) # This line was removed
        return
    if args.bannerfunction:
        bannerfunction()
        return
    # No arguments
    console.print(HELP_PANEL)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print(f'\n[bold magenta]Exiting... Stay stealthy, operator.[/bold magenta]')
