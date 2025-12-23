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
# parser MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
import markdown


# --------------------------------------------------
# markdown-to-HTML parsing logic
# --------------------------------------------------
def render_markdown_to_html(markdown_text):
    """Convert Markdown txt to HTML"""
    return markdown.markdown(markdown_text)
