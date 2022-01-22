# Sonix QMK Autobuild
This project attempts to provide an easier way to build Sonix QMK with your custom keymap. Rather than installing build tools and dependencies locally, you can fork this repository, modify it, and automagically get prebuilt firmware from your custom keymaps.

# Setup
1. Fork this repository. You'll need a GitHub account to do this.
2. In your new fork, go to the *Actions* tab and click the *I understand my workflows, go ahead and run them* button to turn on workflows.
3. Click the *Code* tab
4. Click the build.py file, then hit the pencil icon in the upper right corner of the section that shows the code
5. You should see a list of keyboards in the *BOARDS* array. Find yours and uncomment it by removing the # at the beginning of the line. If you have more than one keyboard you want to build keymaps for, feel free to uncomment more than one! You can add keymaps for all of the boards that are uncommented by following the steps under *Adding your keymap(s)* below.

# Adding your keymap(s)
Your keymaps will go in the keyboards directory. You can commit them locally using git if you're familiar with it, or use the Github web interface as described below.
1. Go to the *Code* tab in your fork of the repository
2. Click on the keyboards folder, then click *Add File* at the top and choose *Create new file*
3. Create your main keymap file. This will need to go into a folder that matches one of the available keyboards [here](https://github.com/SonixQMK/qmk_firmware/tree/sn32/keyboards). For example for the Keychron K2, I'd need to add the keymap at keyboards/keychron/k2/keymaps/my_new_keymap/keymap.c. To create that folder, I would type "keychron/k2/keymaps/my_new_keymap/keymap.c". Each time you type a slash, you should see the preceding text disappear from the text box and appear as a folder to the left of it.
4. Populate your main keymap file. You can open your keymap.c file in any text editor, copy the text, and paste it into GitHub's online editor.
5. Commit your main keymap file. To avoid using up your free Github Actions build minutes before your full keymap is uploaded, you should use the *Create a **new branch** for this commit and start a pull request* option. Feel free to name the branch something relevant (like "my-first-keymap") or just leave the default name, but make sure you remember the branch name for the next step! Once you click Commit, you can leave the Pull Request description as-is or enter any information you may want to reference later.
6. Go back to the *Code* tab and switch to the branch you created by clicking the dropdown in the upper left (below the tab bar) labeled *main* and then clicking the name of your new branch.
7. Navigate to the keymap folder we created in steps 3-5 (clicking a folder will open it). For our example of "keychron/k2/keymaps/my_new_keymap", I would click *keychron*, then *k2*, then *keymaps*, then *my_new_keymap*.
8. Upload the rest of your keymap files by clicking *Add file* at the top and choosing *Upload files*. You can drag your files in or click *choose your files* to pull up the open dialog and select them that way. Once you've chosen your files, click *Commit changes* at the bottom.
9. Almost there! We just need to merge the Pull Request we created and then the firmware will automatically be built. Click the *Pull requests* tab at the top, then click the name of your Pull Request. Scroll down to the bottom and click *Merge pull request*.
10. To watch the progress of your build (and download your files when it's done), click the *Actions* tab at the top. You should see the name of your Pull Request listed, with either a yellow spinner icon indicating that the build is in progress or a green checkmark indicating that it's done. Once you see the green checkmark, click the name of the pull request.
11. You should see an *Artifacts* panel at the bottom of the page with a link labeled *Pre-Compiled Firmware*. Click that link to download your firmware!
12. When you open the zip file, you'll see a few files. One should show the name of your keyboard and end in "default", and the other files should have similar names with "default" replaced by the names of your keymaps. You should now be able to flash the firmware file with the name of your desired keymap!