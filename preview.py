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
# preview MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
from tkinter import Label
from parser import render_markdown_to_html


# --------------------------------------------------
# real-time markdown preview (using Tkinter and markdown parsing)
# --------------------------------------------------
def create_preview(root):
    """Create and return the Markdown preview widget."""
    preview = Label(
        root, text="Preview will be here...",
        justify="left", font=("Arial", 12), anchor="nw"
    )
    preview.grid(row=0, column=2, padx=5, pady=5)
    return preview

def update_preview(editor, preview):
    """Update the preview section with the rendered HTML."""
    markdown_text = editor.get("1.0", "end-1c")
    html = render_markdown_to_html(markdown_text)
    # Update preview with the HTML content
    preview.config(text=html)
    # Recursively update every 100ms
    editor.after(100, update_preview, editor, preview)
