import typer
from typing_extensions import Annotated


app = typer.Typer()


@app.command()
def main():
    print("hello!")


if __name__ == "__main__":
    app()
