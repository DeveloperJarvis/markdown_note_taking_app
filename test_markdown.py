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
# test_markdown MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
import unittest
from parser import render_markdown_to_html

# --------------------------------------------------
# unit tests for core functionality
# --------------------------------------------------
class TestMarkdownApp(unittest.TestCase):

    def test_render_markdown_to_html(self):
        """Test converting Markdown to HTML."""
        markdown_input = "# Heading\nThis is a **bold** text and *italic*."
        expected_output = ("<h1>Heading</h1>\n<p>This is a <strong>bold</strong> " + 
                           "text and <em>Italic</em>.<p>\n")
        
        html_output = render_markdown_to_html(markdown_input)

        self.assertEqual(html_output, expected_output, 
                         "Markdown to HTML conversion failed!")
        
    def test_render_markdown_empty(self):
        """Test converting an empty string to HTML."""
        markdown_input = ""
        expected_output = ""

        html_output = render_markdown_to_html(markdown_input)

        self.assertEqual(html_output, expected_output, 
                         "Empty Markdown text should produce empty HTML!")
    
    def test_render_markdown_invalid(self):
        """Test converting invalid Markdown."""
        markdown_input = "### Invalid Markdown ** ["
        expected_output = "<h3>Invalid Markdown ** [</h3>\n"

        html_output = render_markdown_to_html(markdown_input)

        self.assertTrue(html_output.startswith("<h3>"),
                        "Invalid Markdown should still produce a valid HTML structure!")
        

if __name__ == "__main__":
    unittest.main()
