 # Given a suffix e.g. "_harry", rename all MavensMate resource bundle folders in the currently
 # open Force.com project from the format "my_bundle.resource" to "my_bundle_harry.resource". If
 # a bundle name already has the specified suffix then remove it.
 #
 # Example keyboard shortcut:
 # {
 #   "keys": ["super+shift+h"],
 #   "command": "rename_resource_bundles",
 #   "args": {
 #       "suffix": "_harry"
 #   }
 # }
 # 
 # @author  Luke
 # @date    Feb 2014
import sublime, sublime_plugin, os.path, os, re

class RenameResourceBundlesCommand(sublime_plugin.WindowCommand):
    def run(self, suffix):
        basedir = self.window.project_data()["folders"][0]["path"]
        resourceBundlesPath = os.path.join(basedir, "resource-bundles")
        for dirName in os.listdir(resourceBundlesPath):
            fullPath = os.path.join(resourceBundlesPath, dirName)
            newDirName = fullPath
            if os.path.isdir(fullPath) and fullPath.find(".resource") > -1:
                if fullPath.find(suffix) > -1 and suffix != "":
                    newDirName = re.sub(suffix + "\.resource", ".resource", fullPath)
                else :
                    newDirName = re.sub("\.resource", suffix + ".resource", fullPath)
            print("Renaming '" + fullPath + "' to '" + newDirName)
            os.rename(fullPath, newDirName)