from rich import print
from rich.text import Text
from rich.panel import Panel

print("[bold green]Hi![/bold green] Welcome to [italic cyan]Rich![/italic cyan]")

my_text = Text("Program Warning: All system is operational")
my_text.stylize("bold magenta", 0, 16)

print(my_text)

panel_text = Text(
    "This panel have information about program status,\n"
    "errors or help for user"
)

my_panel = Panel(
    panel_text,
    title="[bold yellow]Program Status[/bold yellow]",
    subtitle="[dim]Version 1.0[/dim]",
    border_style="blue"
)

print("\n", my_panel)