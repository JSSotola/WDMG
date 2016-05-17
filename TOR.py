
#Source: https://stem.torproject.org/tutorials/to_russia_with_love.
#Seems to work only the first time it is run, probably has to do with the way it stops the TOR service. Need to investigate.

from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
import time
def TOR(main, trigger):


    content = BoxLayout(orientation='vertical')

    popup = Popup(title="TOR connection.",
                  content=content,
                  size_hint=(0.9, 0.9))

    popup.open() #For some reason this does not execute imideatly, but waits for the connection to finish.
    # Seems like the problem is that the TOR connection process takes priority over the kivy process and thus the kivy process does not update anything.
    # I tried making the TOR process a secondary process with import threading, but it complained that it needs to be a main process. Not sure what to do.
    # I solved it by faking it. Just save all output to a list and when tor process is finished output it one by one.

    main.list_output = []

    def print_to_screen(text):
        if main.list_output == None:
            main.list_output = [str(text)+"\n"]
        else:
            main.list_output = main.list_output+[str(text)+"\n"]
        #content.add_widget(Label(text=str(text), color=[0,128,0, 1]))

    print_to_screen("Connecting to TOR...")

    def printing(list_output, bool):
        if len(list_output)>0:
            content.add_widget(Label(text=list_output[0], color=[0,128,0, 1]))
            main.list_output = list_output.remove(list_output[0])

            Clock.schedule_once(lambda dt:printing(list_output), main.parent.score.delta_TOR)
        else:
            button = Button(text="OK")
            content.add_widget(button)
            button.bind(on_press=popup.dismiss)
            main.parent.score.delta_TOR = 0.5 # decrease the time it takes to connect so that the players is not delayed in the future
            trigger(main, bool)

    try:
        import io
        import pycurl
        import stem.process
        from stem.util import term


        SOCKS_PORT = 7000


        def query(url):
          """
          Uses pycurl to fetch a site using the proxy on the SOCKS_PORT.
          """

          output = io.BytesIO()

          query = pycurl.Curl()
          query.setopt(pycurl.URL, url)
          query.setopt(pycurl.PROXY, 'localhost')
          query.setopt(pycurl.PROXYPORT, SOCKS_PORT)
          query.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_SOCKS5_HOSTNAME)
          query.setopt(pycurl.WRITEFUNCTION, output.write)

          try:
            query.perform()
            return output.getvalue()
          except pycurl.error as exc:
            print_to_screen("Unable to reach %s (%s)" % (url, exc))


        # Start an instance of Tor configured to only exit through Russia. This prints
        # Tor's bootstrap information as it starts. Note that this likely will not
        # work if you have another Tor instance running.

        def print_bootstrap_lines(line):
          if "Bootstrapped " in line:
            print_to_screen(term.format(line, term.Color.BLUE))


        print_to_screen(term.format("Starting Tor:\n", term.Attr.BOLD))
        print_to_screen("Starting an instance of Tor configured to only exit through Russia")

        print_to_screen("Estabilishing connection...")

        tor_process = stem.process.launch_tor_with_config(
          config = {
            'SocksPort': str(SOCKS_PORT),
            'ExitNodes': '{ru}',
          },
          init_msg_handler = print_bootstrap_lines,
        )

        print_to_screen("Success!")

        tor_process.kill()  # stops tor

        printing(main.list_output, True)


    except Exception as error:
        print_to_screen("Error. You probably need to install TOR.")
        try:
            tor_process.kill()  # stops tor
        except Exception:
            pass
        print_to_screen(error)

        printing(main.list_output, False)


