# --------------------------------------------------
# -*- Python -*- Compatibility Header
#
# Copyright (C) 2023 Developer Jarvis (Pen Name)
#
# This file is part of the markdown_note_taking_app Library. This library is free
# software; you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the
# Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# markdown_note_taking_app - Markdown preview, real-time rendering in Tkinter
#                       Skills: GUI building, markdown parsing
#
# Author: Developer Jarvis (Pen Name)
# Contact: https://github.com/DeveloperJarvis
#
# --------------------------------------------------

# --------------------------------------------------
# markdown_note_taking_app MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
from tkinter import Tk
from editor import create_editor
from preview import create_preview, update_preview


# --------------------------------------------------
# entry point and tkinter GUI
# --------------------------------------------------
def main():
    """Initialize the Tkinter window and run the app."""
    root = Tk()
    root.title("Markdown Note-Taking App")

    # Create the editor and preview widgets
    editor = create_editor(root)
    preview = create_preview(root)

    # Start the real-time preview update
    update_preview(editor, preview)

    # Run the Tkinter main loop
    root.mainloop()


if __name__ == "__main__":
    main()
