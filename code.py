print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

from kmk.modules.midi import MidiKeys
keyboard.modules.append(MidiKeys())


keyboard.col_pins = (board.GP4, board.GP3, board.GP2, board.GP1, board.GP0, board.GP19, board.GP18, board.GP17, board.GP16)
keyboard.row_pins = (board.GP5, board.GP8, board.GP6, board.GP7, board.GP9, board.GP10, board.GP11, board.GP12, board.GP13, board.GP14, board.GP15)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Empty keys
XXXXXXXXXX = KC.NO

keyboard.keymap = [
    [
        KC.MIDI_NOTE(0, 100),   XXXXXXXXXX,             XXXXXXXXXX,             XXXXXXXXXX,             KC.MIDI_NOTE(1, 100),   KC.MIDI_NOTE(2, 100),   KC.MIDI_NOTE(3, 100),   KC.MIDI_NOTE(4, 100),   XXXXXXXXXX,\
        XXXXXXXXXX,             XXXXXXXXXX,             XXXXXXXXXX,             KC.MIDI_NOTE(5, 100),   KC.MIDI_NOTE(6, 100),   KC.MIDI_NOTE(7, 100),   KC.MIDI_NOTE(8, 100),   KC.MIDI_NOTE(9, 100),   XXXXXXXXXX,\
        KC.MIDI_NOTE(10, 100),  KC.MIDI_NOTE(11, 100),  KC.MIDI_NOTE(12, 100),  KC.MIDI_NOTE(13, 100),  KC.MIDI_NOTE(14, 100),  KC.MIDI_NOTE(15, 100),  KC.MIDI_NOTE(16, 100),  XXXXXXXXXX,             XXXXXXXXXX,\
        KC.MIDI_NOTE(17, 100),  KC.MIDI_NOTE(18, 100),  KC.MIDI_NOTE(19, 100),  KC.MIDI_NOTE(20, 100),  KC.MIDI_NOTE(21, 100),  KC.MIDI_NOTE(22, 100),  KC.MIDI_NOTE(23, 100),  XXXXXXXXXX,             XXXXXXXXXX,\
        KC.MIDI_NOTE(24, 100),  KC.MIDI_NOTE(25, 100),  KC.MIDI_NOTE(26, 100),  KC.MIDI_NOTE(27, 100),  KC.MIDI_NOTE(28, 100),  KC.MIDI_NOTE(29, 100),  XXXXXXXXXX,             XXXXXXXXXX,             XXXXXXXXXX,\
        KC.MIDI_NOTE(30, 100),  KC.MIDI_NOTE(31, 100),  KC.MIDI_NOTE(32, 100),  KC.MIDI_NOTE(33, 100),  KC.MIDI_NOTE(34, 100),  KC.MIDI_NOTE(35, 100),  KC.MIDI_NOTE(36, 100),  XXXXXXXXXX,             XXXXXXXXXX,\
        KC.MIDI_NOTE(37, 100),  KC.MIDI_NOTE(38, 100),  KC.MIDI_NOTE(39, 100),  KC.MIDI_NOTE(40, 100),  KC.MIDI_NOTE(41, 100),  KC.MIDI_NOTE(42, 100),  KC.MIDI_NOTE(43, 100),  KC.MIDI_NOTE(44, 100),  KC.MIDI_NOTE(45, 100),\
        KC.MIDI_NOTE(46, 100),  KC.MIDI_NOTE(47, 100),  KC.MIDI_NOTE(48, 100),  KC.MIDI_NOTE(49, 100),  KC.MIDI_NOTE(50, 100),  KC.MIDI_NOTE(51, 100),  XXXXXXXXXX,             XXXXXXXXXX,             XXXXXXXXXX,\
        XXXXXXXXXX,             XXXXXXXXXX,             KC.MIDI_NOTE(52, 100),  KC.MIDI_NOTE(53, 100),  KC.MIDI_NOTE(54, 100),  KC.MIDI_NOTE(55, 100),  XXXXXXXXXX,             KC.MIDI_NOTE(56, 100),  XXXXXXXXXX,\
        KC.MIDI_NOTE(57, 100),  KC.MIDI_NOTE(58, 100),  KC.MIDI_NOTE(59, 100),  KC.MIDI_NOTE(60, 100),  KC.MIDI_NOTE(61, 100),  KC.MIDI_NOTE(62, 100),  KC.MIDI_NOTE(63, 100),  KC.MIDI_NOTE(64, 100),  KC.MIDI_NOTE(65, 100),\
        KC.MIDI_NOTE(66, 100),  XXXXXXXXXX,             KC.MIDI_NOTE(67, 100),  XXXXXXXXXX,             XXXXXXXXXX,             KC.MIDI_NOTE(68, 100),  XXXXXXXXXX,             KC.MIDI_NOTE(69, 100),  XXXXXXXXXX,\
    ]
]

if __name__ == '__main__':
    keyboard.go()
