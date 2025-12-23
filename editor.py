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
# editor MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
from tkinter import Text, Scrollbar


# --------------------------------------------------
# markdown text editor (using Tkinter)
# --------------------------------------------------
def create_editor(root):
    """Create and return the Markdown text"""
    editor = Text(
        root, wrap="word", width=80, 
        height=20, font=("Courier", 12)
    )
    editor.grid(row=0, column=0, padx=5, pady=5)

    # Add vertical scrollbar
    scrollbar = Scrollbar(root, command=editor.yview)
    editor.config(yscrollcommand=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky="ns")

    return editor
