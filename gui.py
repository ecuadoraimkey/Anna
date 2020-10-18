import PySimpleGUI as ui
from anna import Song
from library import Library

library = Library()
song_files = library.load_directory('C:\\Users\\Carter\\Desktop\\flobots\\library')
song = None

currentlyPlaying = 'Not bumpin\' any new shit by N.W.A as of now..'
ui.theme('DarkBlue9')

layout = [
    [ui.Text('Welcome to Anna.')],
    [ui.Text(currentlyPlaying, key='_CURRENTLY_PLAYING_')],
    [ui.Listbox(values=song_files, size=(40, 12), key='_SONG_SELECT_')],
    [ui.Button('Play'), ui.Button('Pause')],
    [ui.Frame('Control', [[
        ui.Text('Volume', font='Courier 8', justification='center'),
        ui.Slider(range=(1, 100), orientation='h', size=(34, 15), default_value=50, key='_VOLUME_')]])],

    [ui.Text('To the moon and back..', text_color='#999999', font='Courier 9')],
]

window = ui.Window('Anna', layout)

while True:
    event, values = window.read()
    if event == ui.WIN_CLOSED or event == 'Cancel':
        song.p.terminate()
        break
    
    if event == 'Play':
        currentlyPlaying = song_files[window.Element('_SONG_SELECT_').Widget.curselection()[0]]
        if song is None:
            song = Song('library/{}'.format(currentlyPlaying))
        else:
            song.stream.stop_stream()
            song = Song('library/{}'.format(currentlyPlaying))

        song.play()
        window['_CURRENTLY_PLAYING_'].Update(currentlyPlaying)
        window.Refresh()
    
    if event == 'Pause':
        song.pause()

window.close()