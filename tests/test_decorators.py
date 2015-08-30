"""
    Tests for botogram/utils.py

    Copyright (c) 2015 Pietro Albini <pietro@pietroalbini.io>
    Released under the MIT license
"""

import botogram.decorators
import botogram.utils


def test_pass_bot(bot, sample_update):
    @botogram.decorators.pass_bot
    def func(local_bot, *args, **kwargs):
        assert local_bot is bot

    decorators = [
        bot.before_processing,
        bot.process_message,
        bot.message_contains("test1"),
        bot.message_matches(r"^test2$"),
        bot.command("test3")
    ]

    for decorator in decorators:
        decorator(func)

    for msg in "test1", "test2", "/test3":
        sample_update.message.text = msg
        bot.process(sample_update)


def test_help_message_for():

    def func():
        """docstring"""
        pass

    assert botogram.utils.docstring_of(func) == "docstring"

    @botogram.decorators.help_message_for(func)
    def help_func():
        return "function"

    assert botogram.utils.docstring_of(func) == "function"
