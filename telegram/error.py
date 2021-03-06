#!/usr/bin/env python
#
# A library that provides a Python interface to the Telegram Bot API
# Copyright (C) 2015 Leandro Toledo de Souza <leandrotoeldodesouza@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser Public License for more details.
#
# You should have received a copy of the GNU Lesser Public License
# along with this program.  If not, see [http://www.gnu.org/licenses/].

"""This module contains a object that represents a Telegram Error"""

import re


class TelegramError(Exception):
    """This object represents a Telegram Error."""

    def __init__(self, message):
        """
        Returns:
            str:
        """
        super(TelegramError, self).__init__()

        api_error = re.match(r'^Error: (?P<message>.*)', message)
        if api_error:
            self.message = api_error.group('message').capitalize()
        else:
            self.message = message

    def __str__(self):
        return '%s' % (self.message)
