from Kalkulator.kalkulator import menukalkulator
import pyfiglet
import curses

if __name__ == "__main__":
    #baner = pyfiglet.Figlet(font='block')
    #print(baner.renderText("KALKULATOR"))

    txt = "KALKULATOR"
    banner = pyfiglet.figlet_format(txt, font="block", justify="center")

    print(banner)
    #screen = curses.initscr()
    #screen.refresh()
    #screen.addstr("Działaj!!!", curses.A_BOLD)

    menukalkulator()
