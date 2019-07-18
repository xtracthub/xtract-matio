"""Utilities for working with parsers"""

from stevedore.extension import ExtensionManager
from stevedore.driver import DriverManager


def get_available_parsers():
    mgr = ExtensionManager(
        namespace='materialsio.parser',
    )

    # Get information about each parser
    output = {}
    for name, ext in mgr.items():
        plugin = ext.plugin()
        output[name] = {
            'description': plugin.__doc__.split("\n")[0],
            'version': plugin.version()
        }
    return output


def execute_parser(name, group, context=None):
    """Invoke a parser on a certain group of data

    Args:
        name (str): Name of the parser
        group ([str]): Paths to group of files to be parsed
        context (dict): Context of the files
    Returns:
        ([dict]): Metadata generated by the parser
    """

    # Load the parser
    mgr = DriverManager(
        namespace='materialsio.parser',
        name=name,
        invoke_on_load=True
    )

    # Execute it on the group
    return mgr.driver.parse(group, context)
