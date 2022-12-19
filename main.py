#!/usr/bin/env python3
import argparse
from sys import exit
from os import path, environ
try:
    from platform import system
    import rich
    from rich.table import Table
    from rich.console import Console
    import openai
    from dotenv import load_dotenv
    from os.path import join, dirname
except ImportError:
    print("Please install the requirements.txt file.\npip3 install -r requirements.txt")
    exit(1)



class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''


# ANSI Colors
color = bcolors()
if system() == "Windows":
    color.disable()




# Rich Console Object
console = Console()
# Load the .env file
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
# OpenAI Api Key
openai.api_key = environ.get("OPENAI_API_KEY")


def banner():
    banner = """
            [bold bright_red]
             ______   _______   ________        ________  __  __       
            /      \ /       \ /        |      /        |/  |/  |      
            /$$$$$$  |$$$$$$$  |$$$$$$$$/      $$$$$$$$/ $$ |$$ |   __ 
            $$ | _$$/ $$ |__$$ |   $$ | ______ $$ |__    $$ |$$ |  /  |
            $$ |/    |$$    $$/    $$ |/      |$$    |   $$ |$$ |_/$$/ 
            $$ |$$$$ |$$$$$$$/     $$ |$$$$$$/ $$$$$/    $$ |$$   $$<  
            $$ \__$$ |$$ |         $$ |        $$ |_____ $$ |$$$$$$  \ 
            $$    $$/ $$ |         $$ |        $$       |$$ |$$ | $$  |
            $$$$$$/   $$/          $$/         $$$$$$$$/ $$/ $$/   $$/       
            [/bold bright_red]
          :crossed_swords: [turquoise4 bold]GPT-ElK[/turquoise4 bold] - [dark_goldenrod bold]Simple Python Tool to play with OpenAI GPT-3 using API.[/dark_goldenrod bold]
                    
                        [green bold]Author: [/green bold][bright_white bold]@sc4rfurry[/bright_white bold]
                        [green bold]Version: [/green bold][bright_white bold]1.0[/bright_white bold]
                        [green bold]Github: [/green bold][bright_white bold]https://github.com/sc4rfurry[/bright_white bold]
    """
    console.print(banner + "\n" + "[purple bold]=[/purple bold]" * 90 + "[yellow2]>[/yellow2]\n")




def help():
    banner()
    console.print(
        """
    [yellow bold]Usage[/yellow bold]: [green bold]main.py[/green bold] (options)

    [red bold]Options[/red bold]:

        -m, --mode      Select the mode to use. ([yellow2]text[/yellow2]/[yellow1]code[/yellow1])
        -h, --help      Show this help message and exit.

    :arrow_forward: [dark_turquoise bold]Note[/dark_turquoise bold]: The [yellow2]Code Mode[/yellow2] has a rate limit. You have to check the OpenAI API docs for more info.
    """
    )
    exit(0)


def check_api_key():
    banner()
    console.print("\n\t\t:shinto_shrine: " + " [yellow2 bold]Checking OpenAI API Key[/yellow2 bold]...")
    if not openai.api_key:
        console.print(":old_key:" + " Please set the OPENAI_API_KEY in the .env file.")
        exit(1)
    else:
        try:
            openai.Completion.create(
                engine="davinci",
                prompt="Hello World",
                max_tokens=50,
                temperature=0.5,
            )
            console.print("\n\t\t:eye: " + " [green bold]OpenAI API Key is valid.[/green bold]")
        except openai.APIError as e:
            console.print("\n:arrow_right_hook:" + f"[red bold]OpenAI Error[/red bold]: {e}")
            exit(1)
        except KeyboardInterrupt:
            console.print("\n:arrow_right_hook:" + " [red bold]Exiting...[/red bold]")
            exit(1)
        except Exception as e:
            if "Incorrect API key provided" in str(e):
                console.print("\n\t\t:arrow_right_hook: " + "[red bold]The OpenAI API Key is invalid.[/red bold] " + ":skull:" + "\n")
                exit(1)
            else:
                print("\n:arrow_right_hook:" + f"[red bold]Error[/red bold]: {e}")
                exit(1)


def text_query_model() -> dict:
    console.print("\n:japanese_secret_button: " + " [yellow2 bold]Enter the query to search for using OpenAI. [/yellow2 bold] [cyan1 bold]([purple bold]Example[/purple bold]: Explain quantum computing in simple terms?)[/cyan1 bold]]\n")
    console.print("[green bold]┌──[/green bold]([chartreuse2 bold]GPT_ElK[/chartreuse2 bold] [yellow1]㉿[/yellow1] [chartreuse2 bold]sc4rfutty[/chartreuse2 bold])-[cyan1 bold][:shark:][/cyan1 bold]")
    prompt = str(input(f"{color.OKGREEN}└─{color.ENDC}$ {color.WARNING}Enter the query{color.ENDC}: "))
    model = "text-davinci-003"
    try:
        response = openai.Completion.create(
            engine=model,
            prompt=prompt,
            max_tokens=3000,
            temperature=0.5,
        )
        return response.choices[0].text
    except openai.APIError as e:
            console.print("\n:arrow_right_hook:" + f"[red bold]OpenAI Error[/red bold]: {e}")
            exit(1)
    except KeyboardInterrupt:
        console.print("\n:arrow_right_hook:" + " [red bold]Exiting...[/red bold]")
        exit(1)
    except Exception as e:
        print("\n:arrow_right_hook:" + f"[red bold]Error[/red bold]: {e}")
        exit(1)
    


def get_code():
    console.print("\n:japanese_secret_button: " + " [yellow2 bold]Get the explanation of the code using OpenAI.[/yellow2 bold] [cyan1 bold]([purple bold]Example[/purple bold]: Explain me the following python code?)[/cyan1 bold]]\n")
    console.print("[green bold]┌──[/green bold]([chartreuse2 bold]GPT_ElK[/chartreuse2 bold] [yellow1]㉿[/yellow1] [chartreuse2 bold]sc4rfutty[/chartreuse2 bold])-[cyan1 bold](:shark:)[/cyan1 bold]")
    query = str(input(f"{color.OKGREEN}└─{color.ENDC}$ {color.HEADER}Enter the query{color.ENDC}: "))
    console.print("\n[green bold]┌──[/green bold]([chartreuse2 bold]GPT_ElK[/chartreuse2 bold] [yellow1]㉿[/yellow1] [chartreuse2 bold]sc4rfutty[/chartreuse2 bold])-[cyan1 bold](:shark:)[/cyan1 bold]")
    filename = str(input(f"{color.OKGREEN}└─{color.ENDC}$ {color.HEADER}Enter the Filename{color.ENDC}: "))
    try:
        if not path.exists(filename) or not path.isfile(filename):
            print(f"{filename} not found.")
            exit(1)
        else:
            with open(filename, "r") as handle:
                code = handle.read()
    except KeyboardInterrupt:
        console.print("\n:arrow_right_hook:" + " [red bold]Exiting...[/red bold]")
        exit(1)
    except Exception as e:
        print("\n:arrow_right_hook:" + f"[red bold]Error[/red bold]: {e}")
        exit(1)

    code_block = f"""
    {query}

    ```
    {code}
    ```
    """
    return code_block



def code_explanation_model() -> dict:
    prompt = get_code()
    model = "code-davinci-002"
    try:
        response = openai.Completion.create(
            engine=model,
            prompt=prompt,
            max_tokens=3000,
            temperature=0.5,
        )
        return response.choices[0].text
    except openai.APIError as e:
            console.print("\n:arrow_right_hook:" + f"[red bold]OpenAI Error[/red bold]: {e}")
            exit(1)
    except KeyboardInterrupt:
        console.print("\n:arrow_right_hook:" + " [red bold]Exiting...[/red bold]")
        exit(1)
    except Exception as e:
        print("\n:arrow_right_hook:" + f"[red bold]Error[/red bold]: {e}")
        exit(1)
    


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-m", "--mode", help="Select the mode to use. [text/code]")
    parser.add_argument("-h", "--help", action="store_true", help="Show this help message and exit.")
    args = parser.parse_args()
    mode = args.mode
    
    if not mode:
        help()
    else:
        if args.mode == "text":
            mode = "text"
        elif args.mode == "code":
            mode = "code"
        else:
            help()

    check_api_key()
    if mode == "text":
        try:
            results = text_query_model()
        except openai.APIError as e:
            print(f"OpenAI Error: {e}")
            exit(1)
        except KeyboardInterrupt:
            print("\nExiting...")
            exit(1)
        except Exception as e:
            print(f"Error: {e}")
            exit(1)
    else:
        try:
            results = code_explanation_model()
        except openai.APIError as e:
            print(f"OpenAI Error: {e}")
            exit(1)
        except KeyboardInterrupt:
            print("Exiting...")
            exit(1)
        except Exception as e:
            print(f"Error: {e}")
            exit(1)
    if mode == "text":
        _mode = "Text Query"
    else:
        _mode = "Code Explanation/Query"
    table = Table(show_header=True, header_style="bold magenta", title="OpenAI Results", title_style="bold green")
    table.add_column(f"[bright_green bold]OpenAI[/bright_green bold] - [bright_red bold]{_mode}[/bright_red bold]", style="cyan", no_wrap=False, justify="left")
    table.add_row(results, "\n", style="pale_turquoise1 bold")
    rich.print("\n\n" , table)


if __name__ == "__main__":
    main()
