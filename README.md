Rename Resource Bundles
=======================
A Sublime Text 3 plugin.
-------------------------

Given a suffix e.g. "_harry", rename all MavensMate resource bundle folders in the currently
open Force.com project from the format "my_bundle.resource" to "my_bundle_harry.resource". If
a bundle name already has the specified suffix then remove it.

This can be useful when a copy (branch) of a resource bundle needs to exist for development
purposes in Salesforce whist tracking a file in a remote repository.

Example keyboard shortcut:
{
  "caption": "Rename Resource Bundles",
  "command": "rename_resource_bundles",
  "args": {
      "suffix": "_harry"
  }
}