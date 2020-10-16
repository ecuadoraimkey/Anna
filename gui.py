import PySimpleGUI as ui
from anna import Song
from library import Library

library = Library()
currentlyPlaying = 'Not bumpin\' any new shit by N.W.A as of now..'
ui.theme('DarkAmber')
song = None

layout = [
    [ui.Text('Welcome to Anna.')],
    [ui.Text(currentlyPlaying, key='_CURRENTLY_PLAYING_')],
    [ui.Input(do_not_clear=False, size=(52,1), key='_FILENAME_'), ui.Button('Play'), ui.Button('Pause')],
    [ui.Text('To the moon and back..', text_color='#999999', font='Courier 9')],
]

window = ui.Window('Anna', layout)
while True:
    event, values = window.read()
    if event == ui.WIN_CLOSED or event == 'Cancel':
        break
    
    if event == 'Play':
        song = Song(values['_FILENAME_'])
        song.play()
        window['_CURRENTLY_PLAYING_'].Update(values['_FILENAME_'])
        window.Refresh()
    
    if event == 'Pause':
        song.pause()

window.close()