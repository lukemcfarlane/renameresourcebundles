Rename Resource Bundles
=======================
A Sublime Text 3 plugin.
-------------------------

Given a suffix e.g. "\_harry", rename all MavensMate resource bundle folders in the currently
open Force.com project from the format "my_bundle.resource" to "my_bundle_harry.resource". If
a bundle name already has the specified suffix then remove it.

This can be useful when a copy (branch) of a resource bundle needs to exist for development
purposes in Salesforce whist tracking a file in a remote repository.

Example keyboard shortcut:

    {
      "keys": ["super+shift+h"],
      "command": "rename_resource_bundles",
      "args": {
          "suffix": "_harry"
      }
    }


Installation
------------

Copy the following files into a new folder "RenameResourceBundles" inside your Sublime Packages directory:
- RenameResourceBundlesCommand.py
- Default.sublime-commands

**Note:** to locate your Sublime Packages directory, from within Sublime Text go to the Sublime Text menu -> Preferences -> Browse Packages.