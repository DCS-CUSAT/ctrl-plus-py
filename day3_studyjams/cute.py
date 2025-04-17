import csv
import os
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, FloatPrompt
from operator import itemgetter

FILENAME = "expenses.csv"
console = Console()


def add_expense():
    console.print("\n[bold magenta]Add a New Expense[/bold magenta]")

    date = Prompt.ask("📅 Date (YYYY-MM-DD)", default=datetime.today().strftime('%Y-%m-%d')) #Hey, I’m asking you for the date. If you don’t provide one, I’ll fill in today’s date in the format YYYY-MM-DD
    category = Prompt.ask("📂 Category (e.g., Food, Travel, etc.)")
    amount = FloatPrompt.ask("💰 Amount (in ₹)")
    description = Prompt.ask("📝 Description (optional)", default="-")

    # Make sure the file exists and has headers if it's new
    file_exists = os.path.isfile(FILENAME)
    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists or os.stat(FILENAME).st_size == 0:
            writer.writerow(["Date", "Category", "Amount", "Description"])
        writer.writerow([date, category, amount, description])
    
    console.print("[green]✅ Expense added successfully![/green]")

def view_expenses():
    console.print("\n[bold cyan]Your Expense History[/bold cyan]")

    try:
        with open(FILENAME, mode='r') as file:
            reader = csv.reader(file)
            expenses = [row for row in reader]

        if len(expenses) <= 1:
            console.print("[red]No expenses recorded yet![/red]")
            return

        # Remove headers before sorting and displaying
        headers = expenses.pop(0)

        # Ask how to sort
        sort_option = Prompt.ask("\n🔀 Sort by", choices=["date", "category", "amount", "none"], default="none")
        if sort_option == "date":
            expenses.sort(key=itemgetter(0))  # sort by date
        elif sort_option == "category":
            expenses.sort(key=itemgetter(1))  # sort by category
        elif sort_option == "amount":
            expenses.sort(key=lambda x: float(x[2]))  # sort by amount

        # Create pretty table
        table = Table(title="📊 Expense Tracker", show_lines=True)
        table.add_column("Date", style="dim")
        table.add_column("Category", style="magenta")
        table.add_column("Amount (₹)", justify="right", style="green")
        table.add_column("Description", style="yellow")

        total = 0
        for row in expenses:
            table.add_row(row[0], row[1], f"₹{row[2]}", row[3])
            total += float(row[2])

        console.print(table)
        console.print(f"\n[bold green]💸 Total Spent: ₹{total:.2f}[/bold green]")

    except FileNotFoundError:
        console.print("[red]No expenses file found yet. Try adding one first![/red]")

def main():
    console.print("[bold blue]\n💖 Welcome to Your Cute Expense Tracker 💖[/bold blue]")

    while True:
        console.print("\n[bold]What would you like to do?[/bold]")
        console.print("1️⃣ Add Expense")
        console.print("2️⃣ View Expenses")
        console.print("3️⃣ Exit")

        choice = Prompt.ask("Pick an option", choices=["1", "2", "3"], default="1")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            console.print("\n[italic]Bye bestie! Save that coin 💅[/italic]\n")
            break

if __name__ == "__main__":
    main()
